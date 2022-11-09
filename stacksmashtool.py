import sys
import os

beginstr = ""
addr = ""
num = 0

if (len(sys.argv) > 1):
    op = 0
    if(len(sys.argv) == 5):
        op += 1
    beginstr = sys.argv[1 + op]
    addr = sys.argv[2 + op]
    num = int(sys.argv[3 + op])
else:
    print("Enter the code you want to run:")
    beginstr = str(input())
    print("What is the address you want to jump to?")
    addr = str(input())
    print("How many entries do you want to overwrite?")
    num = int(input())

outstr = beginstr
for i in range(num):
    outstr = outstr + addr

if (len(sys.argv) == 5):
    if(sys.argv[1] == "-h"):
        print(outstr)
    elif(sys.argv[1] == "-f"):
        os.system("echo " + outstr + " | xxd -r -p ")
else:
    print("Your hex string:\n" + outstr) 
    print("Your formatted string:")
    os.system("echo " + outstr + " | xxd -r -p ")
