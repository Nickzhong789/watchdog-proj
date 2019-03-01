#!/usr/bin/env python
# coding: utf-8

# In[1]:


from watchdog.observers import Observer
from watchdog.events import *
import time


class myFileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
        
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            if event.src_path is "C:\soft\ASAP\build\ASAP\Debug\ASAP_d.exe":
                print("file deleted:{0}".format(event.src_path))
    
    def on_modified(self, event):
        if event.is_directory:
            pass
        else:
            pass


if __name__ == "__main__":
    observer = Observer()
    event_handler = myFileEventHandler()
    observer.schedule(event_handler, "C:\soft\ASAP", True)
    observer.start()
    
    try:
        while(True):
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# In[ ]:




