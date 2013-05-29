RESTdev
=======
A repro for developing Web Services written in Python, using Bottle (http://bottlepy.org/)

Bottle is brilliant- if for nothing other than prototyping-
It offers request dispatching (Routes) with url parameter support, templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines - all in a single file and with no dependencies other than the
Python Standard Library.

hmac_test.py is a simple python-only implementation of HMAC using the hmac module.
testrestapi.py is a simple Bottle implementation of RESTful API using HMAC for authentication.