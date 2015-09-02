# iris-webapp

This is a demo web application, powered by Flask in the backend and AngularJS in the frontend. It demonstrates how to handle file validation and parsing in the frontend, i.e. CSV file parsing and how to use this parsed data in the backend to perform a machine learning task k-means clustering using scikit-learn) on it.

It consists of two parts: the `server` and the `client`:

## iris-server

The server is just a small Flask application that accepts the parsed CSV data and returns the results from the k-means clustering.

For the installation you need to have a running version of Python (tested with 3.4). Then follow these steps:

```
$ cd iris-server
$ pip install -r requirements.txt
$ python server.py
```

Now the server is running on `http://localhost:5000`.

## iris-client

This is the AngularJS app that powers the frontend of the webapp. To install its dependencies you need [bower](http://bower.io/) (the installation of bower is out-of-scope for this document). Install the dependencies like this:

```
$ cd iris-client
$ bower install
```

To actually serve the frontend you need a webserver. Since you need Python anyway for the `iris-server` its easiest to use Python's built-in HTTP server:

```
python -m http.server
```

Now you have a running web server on `http://localhost:8000`. Visit this link and start playing around with the app.
