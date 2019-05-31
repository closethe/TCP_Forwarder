import socket,asyncore,random

class TCP_Receiver(asyncore.dispatcher):
    def __init__(self,conn,key,forward):
        asyncore.dispatcher.__init__(self,conn)
        self.from_remote_buffer=''
        self.to_remote_buffer=''
        self.sender=None
        self.key = key
        self.username=""
        self.type = ""
        self.forward = forward
        self.forward.TCP_connects[key]["receiver"] = self

    def handle_connect(self):
        pass

    def handle_read(self):
        try:
            read = self.recv(4096)
            self.from_remote_buffer += read
        except Exception as e:
            print "receiver_read Excepton: ",e.__str__()

    def writable(self):
        return (len(self.to_remote_buffer) > 0)

    def handle_write(self):
        sent = self.send(self.to_remote_buffer)
        # print '%04i <--'%sent
        self.to_remote_buffer = self.to_remote_buffer[sent:]

    def handle_close(self):
        #print "receiver close"
        if self.forward.TCP_connects.has_key(self.key):
            del self.forward.TCP_connects[self.key]
        self.close()
        if self.sender:
            self.sender.close()

