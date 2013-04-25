pyroqueue
=========

Shared queue service specifically designed for use with pyro transport in kombu

deps:
https://pypi.python.org/pypi/Pyro4

run:
python pyroqueues.py  <host:port> <vhost> 

test:
python pyroqueues.py  127.0.0.1 default &
python pyroqueuestest.py 
pyro queueinfo.py 
