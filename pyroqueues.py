import Pyro4
import Queue
import sys
import time
import threading


class SharedQueues(object):

    def __init__(self):
        self.queues = {}

    def get_queue_names(self):
        return self.queues.keys()

    def new_queue(self ,key):
        self.queues[key] = Queue.Queue()

    def _get(self, queue):
        msg = self._queue_for(queue).get_nowait()
        return msg

    def _put(self, queue, message):
        self._queue_for(queue).put_nowait(message)

    def _size(self, queue):
        return self._queue_for(queue).qsize()

    def _delete(self, queue, *args):
        self.queues.pop(queue, None)

    def _purge(self, queue):
        q = self._queue_for(queue)
        size = q.qsize()
        q.queue.clear()
        return size

    def _queue_for(self, queue):
        if queue not in self.queues:
            self.queues[queue] = Queue.Queue()
        return self.queues[queue]



if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9090
    vhost = 'default'

    if len(sys.argv) > 1:
        address = sys.argv[1].split(":")
        host, port = address[0], address[1] if len(address) > 1 else 9090

    if len(sys.argv) > 2:
        vhost = sys.argv[2]


    #IMPORTANT! set security key to vhost
    Pyro4.config.HMAC_KEY=vhost

    # start request daemon and name server
    print "starting nameserver %s:%s" % (host,port)
    _, daemon, _ = Pyro4.naming.startNS(host=host, port=port)
    uri = daemon.register(SharedQueues())

    daemon.nameserver.register(vhost, uri)
    print "starting RequstLoop with HMAC_KEY = %s" % (vhost)
    daemon.requestLoop()
