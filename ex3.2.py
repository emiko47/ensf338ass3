import json
import random
import time
import matplotlib.pyplot as plt

x = open('ex2tasks.json')
y = open('ex2data.json')

tasks = json.load(x)
data = json.load(y)

print (len(data))

def binary_search(arr, target, start):

    left, right = 0, len(arr) - 1
    
    mid = start
    
    while left <= right:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
        mid = (left + right) // 2
            
    return -1


midpoint = []
taskstr = []
for task in tasks:
    taskstr.append(str(task))
    points = []
    times = []

    for i in range(0,100):
        
        point = random.randint(0, 999999)

        start_time = time.time()

        binary_search(data,task,point);

        end_time = time.time()


        times.append(end_time-start_time)
        points.append(str(point))
   

    datadict = dict(zip(points,times))
    datasort = sorted(datadict)
    midpoint.append(int(datasort[0]))

plt.scatter(taskstr,midpoint)
plt.xlabel("Tasks")
plt.ylabel("Starting Midpoints")
plt.title("Midpoints vs Tasks")
plt.xticks(rotation=90)
plt.show()


x.close()
y.close()