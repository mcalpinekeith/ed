# with open(r"D:\glove.840B.300d.txt", encoding="utf") as f:
#     for line in f:    
#         l = line.split()
#         print(l[0] + ', ' + str(list(map(float, l[1:]))))
import tensorflow
from tensorflow.python.client import device_lib

local_device_protos = device_lib.list_local_devices()

for x in local_device_protos:
    print(x)

#def get_available_gpus():
#    local_device_protos = device_lib.list_local_devices()
#    return [x.name for x in local_device_protos if x.device_type == 'GPU']