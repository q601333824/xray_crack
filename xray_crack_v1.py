# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time,sys,os,threading

class crack(threading.Thread):
    def __init__(self,curr_time):
        threading.Thread.__init__(self)
        self.curr_time = curr_time
    def run(self):
        time.sleep(5)
        os.system("date "+self.curr_time)
    
if __name__ == '__main__':
    print("""               
                   嗯~ o(*￣▽￣*)o  
                xray_crack By:Mi_Tian
    """)
    try:
        argv=" "
        for i in range(len(sys.argv)):
            if i !=0:
                argv=argv+" "+str(sys.argv[i])
        curr_time=time.strftime('%Y-%m-%d', time.localtime(time.time()))
        os.system("date 2022-02-09")
        thread1 = crack(curr_time)
        thread1.start()
        os.system("xray.exe"+argv)
    except BaseException:
        input("error!!!!!!!!press Enter key to end")
    




