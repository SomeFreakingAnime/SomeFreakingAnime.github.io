import os,time
os.system('git add *')
os.system('git commit -a -m "'+str(time.localtime())+'"')
os.system('git push')