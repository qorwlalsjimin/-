#math = __import__("math")
#from math import *

#print(pi)
#print(sin(10))

#import sys

## 명령 매개변수
#print(sys.argv)

#from datetime import datetime
#now = datetime.now()
#now = datetime(2000, 1, 1, 1, 1, 1)
#print(now)
#
#print(now.year)
#print(now.month)
#print(now.day)
#print(now.hour)
#print(now.minute)
#print(now.second)

#import time
#
#print("A")
#time.sleep(2)
#print("B")

#from urllib import request
#
#target = request.urlopen("http://naver.com")
#content = target.read()
#
#print(content)

from random import *
print(random())
print(int(uniform(10, 20))+1)
print(uniform(10, 20))
print(choice(["이것도","되려낭","궁금","요요","맨맨"]))
print(shuffle([1,2,3,4,5]))
print(sample([1,2,3,4,5], k=2))

hi = [1, 2, 3, 4,]
shuffle(hi)
print(hi)