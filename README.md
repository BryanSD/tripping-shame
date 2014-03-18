tripping-shame
==============

Test with: gunicorn_pecan config.py -k eventlet

Issue two concurrent requests against the server.

A hook uses eventlet.sleep(5) to sleep for 5 seconds. If properly working, the requests should finish executing in ~5-6 seconds instead of 10+ seconds.
