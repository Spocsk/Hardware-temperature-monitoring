import wmi
import serial
import time

port = 'COM3'
baud = 9600

a = serial.Serial(port,baud, timeout=.1)

data =''

print("""
           __   __             __   ___ 
|__|  /\  |__) |  \ |  |  /\  |__) |__  
|  | /~~\ |  \ |__/ |/\| /~~\ |  \ |___ 
                                        
 __   __       ___  __   __             
/  ` /  \ |\ |  |  |__) /  \ |          
\__, \__/ | \|  |  |  \ \__/ |___       
                                        
Developper :  COUTO DE OLIVEIRA Dylan 20/03/2020
""")
time.sleep(2)
print("Port initiale to : {}".format(port))
time.sleep(2)
print("Baud initiale to : {}".format(baud))

w = wmi.WMI(namespace="root\OpenHardwareMonitor")

time.sleep(2)
print("Obtaining from OpenHardwareMonitor...")
time.sleep(2)

print("Transmetting data to Arduino...")

while(True):

    temperature_infos = w.Sensor()



    for sensor in temperature_infos:

        if sensor.SensorType==u'Temperature':

            if sensor.Name == "GPU Core":
                temp_gpu = str(int(sensor.Value))
                #print("GPU {}".format(int(sensor.Value)))

            if sensor.Name == "CPU Package":
                temp_cpu = str(int(sensor.Value))
                #print("CPU {}".format(int(sensor.Value)))

        if sensor.SensorType==u'Data':
            if sensor.Name == "Available Memory":
                ram_free = str(round(sensor.Value,1))
            if sensor.Name == "Used Memory":
                ram_used = str(round(sensor.Value,1))

    data = data + temp_cpu + temp_gpu + ' ' + ram_used + ' ' + ram_free
    #print(data)
    a.write(data.encode('ascii'))
    
    time.sleep(3)

    data = ''

