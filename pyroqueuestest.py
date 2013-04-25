import sys
import Pyro4

def run_test(host,port,vhost):
    Pyro4.config.HMAC_KEY=vhost
    nameserver = Pyro4.locateNS(host=host, port=port)
    uri = nameserver.lookup(vhost)
    qs = Pyro4.Proxy(uri)

    print "Queues %s" % qs.get_queue_names()
    q1="abc"
    qs.new_queue(q1)
    print "Queues %s" % qs.get_queue_names()
    qs._put(q1, "disdat")
    qs._put(q1, "datndata")
    qs._put(q1, "jumperella")
    print "Get: %s" % qs._get(q1)
    print "Get: %s" % qs._get(q1)
    print "Size: %s" % qs._size(q1)
    print "Delete: %s" % qs._delete(q1)
    print "Queues %s" % qs.get_queue_names()
    qs.new_queue(q1)
    print "Queues %s" % qs.get_queue_names()
    qs._put(q1, "disdat")
    qs._put(q1, "datndata")
    qs._put(q1, "jumperella")
    print "%s Items Purged" % qs._purge(q1)

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9090
    vhost = 'default'

    if len(sys.argv) > 1:
        address = sys.argv[1].split(":")
        host, port = address[0], address[1] if len(address) > 1 else 9090

    if len(sys.argv) > 2:
        vhost = sys.argv[2]

    run_test(host, port, vhost)
