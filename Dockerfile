FROM node
COPY . /tmp
RUN  npm install
CMD  node server.js
