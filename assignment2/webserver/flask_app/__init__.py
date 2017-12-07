from flask import abort, flash, redirect, request, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_app.forms import CreateForm, DeleteForm, UpdateForm
from flask_app.instances import app, bcrypt
from flask_app.models import User


@app.before_first_request
def createsuperuser():
    name, password = app.config["ADMIN_USER"].split(":")
    user = User(name=name,
                password=bcrypt.generate_password_hash(password),
                superuser=True)
    user.create()


@app.route("/", methods=["GET"])
def home():
    return "Rajani's Flask App: Hello World!\n", 200


@app.route("/protected/", methods=["GET"])
def authentication():
    token = request.headers.get("Authorization", request.args.get("token"))
    if token is not None:
        try:
            name, password = token.split(":")  # raise ValueError on bad request
            user = User.get(name)
            if user is not None:
                if current_user.is_authenticated:
                    logout_user()
                if bcrypt.check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for("user_list"))
        except ValueError:
            abort(400)
    abort(401)


@app.route("/protected/list/", methods=["GET"])
@login_required
def user_list():
    users = User.all()
    return render_template("user/list.html", obj_list=users)


@app.route("/protected/create/", methods=["GET", "POST"])
@login_required
def user_create():
    if not current_user.is_admin:
        return redirect(url_for("user_list"))
    form = CreateForm(request.form)
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    password=bcrypt.generate_password_hash(form.password.data),
                    superuser=form.superuser.data)
        user.create()
        flash("User successfully created")
        return redirect(url_for("user_list"))
    return render_template("user/upsert.html", form=form)


@app.route("/protected/update/<string:name>", methods=["GET", "POST"])
@login_required
def user_update(name):
    if not current_user.is_admin:
        return redirect(url_for("user_list"))
    user = User.get(name)
    form = UpdateForm(request.form, obj=user)
    if form.validate_on_submit():
        user.update(form)
        flash("User successfully updated")
        return redirect(url_for("user_list"))
    return render_template("user/upsert.html", form=form)


@app.route("/protected/delete/<string:name>", methods=["GET", "POST"])
@login_required
def user_delete(name):
    if not current_user.is_admin:
        return redirect(url_for("user_list"))
    user = User.get(name)
    form = DeleteForm(request.form, obj=user)
    if form.validate_on_submit():
        user.delete()
        flash("User successfully deleted")
        return redirect(url_for("user_list"))
    return render_template("user/delete.html", form=form)


@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("home"))

