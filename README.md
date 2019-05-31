# TCP_Forwarder


```
1、 modify "port.py"  
  line14: forwarder("127.0.0.1",8899,"192.168.1.112",3389)
  this samples show ,create a tcpforwarder from 127.0.0.1:8899 to 192.168.1.112:3389

2、start a forwarder
  python port.py

3、 test forwarder, connect 127.0.0.1:8899 it will forwarder to 192.168.1.112:3389
  mstsc 127.0.0.1:8899

```
