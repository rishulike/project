import os
import sys
print(os.path.dirname(sys.argv[0]))
print(os.path.basename(sys.argv[0]))
print(os.path.exists(sys.argv[0]))
print(os.path.isdir("E:\RISHABH JAIN"))
print(os.path.isfile("E:\RISHABH JAIN"))
#file=sys.argv[0]
#print(os.path.getsize(file))
'''
print(dir(os))
help(os)
import random
help(random)'''
#os.mkdir("E:\\official")
#os.removedirs("E:\\official")
#os.removedirs()
#os.rename("E:\dow\program/calci.py","E:\dow\program/calci1.py")
os.stat("E:\dow\program/calci1.py").st_size
print(os.stat("E:\dow\program/calci1.py").st_mtime)
import datetime
date=os.stat("E:\dow\program/calci1.py").st_mtime
print(datetime.datetime.fromtimestamp(date))

