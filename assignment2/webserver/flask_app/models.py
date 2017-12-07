from flask_login import UserMixin, logout_user, current_user
from flask_app.instances import bcrypt, login_manager, redis_store

__all__ = ["User"]


class User(UserMixin):
    prefix = "users"

    def __init__(self, name, password, superuser=False):
        self.name = name
        self.password = password
        self.superuser = superuser if superuser else ""

    @property
    def id(self):
        return self.name

    @property
    def is_admin(self):
        return self.superuser == "True"

    def to_dict(self):
        return {"password": self.password,
                "superuser": self.superuser}

    @classmethod
    def to_obj(cls, user_dict, name):
        return User(name=name, **user_dict)

    def create(self):
        redis_key = "%s:%s" % (self.prefix, self.name)
        redis_store.hmset(redis_key, self.to_dict())

    def update(self, form):
        if self.name != form.name.data:
            self.delete()
            self.name = form.name.data
        if form.password.data:
            self.password = bcrypt.generate_password_hash(form.password.data)
        self.superuser = form.superuser.data
        self.create()

    def delete(self):
        redis_key = "%s:%s" % (self.prefix, self.name)
        redis_store.delete(redis_key)
        if current_user.name == self.name:
            logout_user()

    @classmethod
    def get(cls, name):
        redis_key = "%s:%s" % (cls.prefix, name)
        user_dict = redis_store.hgetall(redis_key)
        return cls.to_obj(user_dict, name) if user_dict else None

    @classmethod
    def all(cls):
        redis_keys = redis_store.keys(pattern="%s*" % cls.prefix)
        users = []
        for redis_key in redis_keys:
            user_dict = redis_store.hgetall(redis_key)
            name = redis_key.split(":")[1]
            users.append(cls.to_obj(user_dict, name))
        return users


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

