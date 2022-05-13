#!/usr/bin/env python3
#usage
#python3 install_split_apk <path_containing_splitted_apks>
#tested on OSX

import os
import random,sys

splitted_apks_directory=sys.argv[1]
os.chdir(splitted_apks_directory)

arr = os.listdir()
print (arr)
total_size=0


for apk in arr:
    #if(apk.endswith(".apk") and ("arm64" not in apk) ): //you may try your chance for x86 devices
    if(apk.endswith(".apk") ):
        total_size=total_size+os.path.getsize(apk)
        #print (os.system("ls -la "+apk))
        print("apk to pushed =>"+apk +" size= "+str(os.path.getsize(apk)))
print ("total= "+str(total_size))


result = os.popen("adb shell pm install-create -S "+str(total_size)).read()
#print(result)

sessionid=result[result.index("[")+1:result.index("]")]
print("sessionid= "+sessionid)

index=0
#print(os.getcwd())
tmppath="/data/local/tmp/"+str(random.randint(1,999999))
print(os.popen("adb shell mkdir {0}".format(tmppath)).read())
for apk in arr:
    #if (apk.endswith(".apk") and ("arm64" not in apk) ): //you may try your chance for x86 devices
    if (apk.endswith(".apk")):
        #print(os.getcwd())
        apk_size=os.path.getsize(apk)
        apkpath=os.getcwd()+"/"+apk
        command1="adb push {0} {1}".format(apkpath,tmppath)
        result = os.popen(command1).read()
        #print(result)
        tmp_apkpath=tmppath+"/"+apk
        command2="adb shell pm install-write -S {0} {1} {2} {3} ".format(apk_size,sessionid,index,tmp_apkpath)
        index=index+1
        result = os.popen(command2).read()
        print (result)
        #print(command1)
        #print (command2)

result = os.popen("adb shell pm install-commit {0}".format(sessionid)).read()
print(result)





