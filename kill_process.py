# First run below in terminal  
# fuser -v /dev/nvidia* > tmp.txt  

import os 
file1 = open('tmp.txt', 'r') 
Lines = file1.readlines() 
Lines = [line.rstrip() for line in Lines] 

# Assume only one line  
PIDs = Lines[0].split() 
for pid in PIDs: 
    pid = int(pid) 
    print(f'kill {pid}') 
    os.kill(pid, 9)
