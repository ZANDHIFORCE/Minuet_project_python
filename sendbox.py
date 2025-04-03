from datetime import time
from datetime import datetime

datetime1 = datetime(2025, 4,3)
time1 = time(13,30)

print(datetime1.weekday())
print(time1.strftime("%H:%M"))