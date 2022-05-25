#!/usr/bin/env python3
#usage
#python3 pull_apk_from_device.py <path_to_write_splitted_apks> <packegename_or_some_part_of_it>
#tested on OSX
#twitter.com/@mustafaran

import os
import sys

splitted_apks_directory=sys.argv[1]
package_to_pull=sys.argv[2]
os.chdir(splitted_apks_directory)

full_name_of_package = os.popen("adb shell pm list packages | grep  {0} ".format(package_to_pull)).read().split(':')[1].replace('\n','')
print (full_name_of_package)
result= os.popen("adb shell pm path  {0} ".format(full_name_of_package)).read().split('\n')
print(result)
apk=""
command0="adb shell mkdir {0}".format("/data/local/tmp/"+full_name_of_package)
print(command0)
print(os.popen(command0).read())
for line in result:
    try :
        apk=line.split(':')[1].replace('\n','')

        command1="adb shell cp {0} {1}/".format(apk,"/data/local/tmp/"+full_name_of_package)

        print(command1)
        print(os.popen(command1).read())

    except:
        pass
#print(splitted_apks_directory)
command3="adb pull /data/local/tmp/{0}/ {1}".format(full_name_of_package,splitted_apks_directory)
print(command3)
print(os.popen(command3).read())
