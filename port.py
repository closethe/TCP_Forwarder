import socket,asyncore,random
import time,ConfigParser
from sender import TCP_Sender as sender
from receiver import TCP_Receiver as receiver
from forwarder import TCP_Forwarder as forwarder



if __name__=='__main__':
    # localhost
    # local port
    # remote ip
    # remote port
    forwarder("127.0.0.1",8899,"192.168.1.112",3389)
    asyncore.loop()
