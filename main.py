import time
import scheduler
from task1 import *
from task2 import *

scheduler = scheduler.Scheduler()
scheduler.SCH_Init()
task1 = Task1(0)
task2 = Task1(1)


scheduler.SCH_Add_Task(task1.Task1Run, 1000, 5000)
scheduler.SCH_Add_Task(task2.Task1Run, 2000, 4000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)




    # max 40 different tasks


