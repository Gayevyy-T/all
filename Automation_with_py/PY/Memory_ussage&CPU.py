import shutil
du = shutil.disk_usage("/")
print(du)
du.free / du.total * 100
du_percentage = du.free / du.total * 100
print("Free space on C: {:.2f}%".format(du_percentage))

import psutil
cpu = psutil.cpu_percent(0.1)
print("CPU memory ussed {}".format(cpu))