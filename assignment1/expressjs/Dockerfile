FROM node:boron
MAINTAINER Rajani Saini "rajani.saini@student.ufv.ca"

# Create app directory
RUN mkdir /code
WORKDIR /code

# Install app dependencies
COPY package.json /code/
RUN npm install

# Bundle app source
COPY . /code

# Listen on port 9000
EXPOSE 9000

# Start app
CMD [ "npm", "start" ]
