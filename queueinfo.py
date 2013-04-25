import sys
import Pyro4

def print_queue_info(host,port,vhost):
    Pyro4.config.HMAC_KEY=vhost
    nameserver = Pyro4.locateNS(host=host, port=port)
    uri = nameserver.lookup(vhost)
    qs = Pyro4.Proxy(uri)

    print "Queues Info"
    print "----------"
    for q in qs.get_queue_names():
        print "%s: %s" % (q, qs._size(q))


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9090
    vhost = 'default'

    if len(sys.argv) > 1:
        address = sys.argv[1].split(":")
        host, port = address[0], address[1] if len(address) > 1 else 9090

    if len(sys.argv) > 2:
        vhost = sys.argv[2]

    print_queue_info(host,port,vhost)

