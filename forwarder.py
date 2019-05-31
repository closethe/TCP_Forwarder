import socket,asyncore,random
from sender import TCP_Sender as sender
from receiver import TCP_Receiver as receiver

class TCP_Forwarder(asyncore.dispatcher):
    TCP_connects = {}
    def __init__(self,ip, port, remoteip,remoteport,backlog=5):
        asyncore.dispatcher.__init__(self)
        self.remoteip=remoteip
        self.remoteport=remoteport
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip,port))
        self.listen(backlog)

    def handle_accept(self):
        conn, addr = self.accept()
        print '--- Connect --- '
        print self.TCP_connects
        print "key (addr) :",addr
        key = addr
        TCP_Forwarder.TCP_connects[key] = {}.fromkeys(['sender','receiver','attribute'])
        TCP_Forwarder.TCP_connects[key]["attribute"] = {}
        sender(receiver(conn,key,self),self.remoteip,self.remoteport,key,self)
        
    def handle_connect(self):
        print "for connect"
        pass

    def handle_close(self):
        print "for close"
        self.close()

    def handle_read(self):
        print "for read"

    def handle_write(self):
        print "for write"

