import socket,asyncore,random

class NotFindSqlException(Exception):
    pass  
class TCP_Sender(asyncore.dispatcher):
    def __init__(self, receiver, remoteaddr,remoteport,key,forward):
        asyncore.dispatcher.__init__(self)
        self.receiver=receiver
        receiver.sender=self
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((remoteaddr, remoteport))
        self.key = key
        self.username = ""
        self.type = ""
        self.dict ={}
        self.forward = forward
        self.forward.TCP_connects[key]["sender"] = self

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(4096)
        # print '<-- %04i'%len(read)
        #print "sender_read",self.username
        self.receiver.to_remote_buffer += read

    def writable(self):
        return (len(self.receiver.from_remote_buffer) > 0)

                    
    def handle_write(self):
        try:
            data = self.receiver.from_remote_buffer
            result = self.fixpacket(data)
            self.receiver.from_remote_buffer = result
        except Exception as e:
            print "sender_write: ",e.__str__()
        sent = self.send(self.receiver.from_remote_buffer)
        #print '--> %04i'%sent
        self.receiver.from_remote_buffer = self.receiver.from_remote_buffer[sent:]

    def handle_close(self):
        if self.forward.TCP_connects.has_key(self.key):
            del self.forward.TCP_connects[self.key]
        self.close()
        self.receiver.close()
        
    def fixpacket(self,data):
        result = data
        return result
