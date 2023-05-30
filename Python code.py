import paho.mqtt.client as mqttimport 
RPi.GPIO as GPIO
import smbusimport time as t
mqttc=mqtt.Client()
mqttc.connect("test.mosquitto.org",1883,60)
mqttc.loop_start()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
Motor1A = 18 #24
Motor1B = 16 #23
Motor1E = 22 #25
bus = smbus.SMBus(1)
ADDRESS1 = 0x48
def reading1(): 
  a= bus.read_byte(ADDRESS1) 
  return a
GPIO.setup(31,GPIO.IN)
GPIO.setup(33,GPIO.IN)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
x="Motor on“
y="Motor off"
while True:
  temp = reading1() 
  temp = float(temp)  
  temperature = ((temp / 256)* 5.13 * 1000/10)  
  temperature = int(temperature)  
  if GPIO.input(31)==1:    
    if GPIO.input(33)==1:    
    GPIO.output(Motor1A,GPIO.HIGH)   
    GPIO.output(Motor1B,GPIO.LOW)     
    GPIO.output(Motor1E,GPIO.HIGH)
    (result,mid)=mqttc.publish("paho/old123","*Rain not detected\n*Soil is             dry\n*temperature in degree celsius= %d'C\n*Motor on"%temperature,2)   
    print("*Rain not detected \n*Soil is dry")     
    print("*temperature in degree celsius= %d'C"%temperature) 
    print("*Motor on")  
   else:    
     GPIO.output(Motor1E,GPIO.LOW)      
    (result,mid)=mqttc.publish("paho/old123","*Rain not detected\n*Soil is wet\n*temperature    in degree celsius= %d'C\n*Motor off"%temperature,2)
    print("*Rain not detected \n*Soil is wet ")      
    print("*temperature in degree celsius= %d'C"%temperature)   
    print("*Motor off")  
else:   
   GPIO.output(Motor1E,GPIO.LOW) 
   (result,mid)=mqttc.publish("paho/old123","*Rain is detected\n*temperature 
in degree celsius= %d'C\n*Motor off"%temperature,2)    print("*Rain is detected")   
   print("*temperature in degree celsius is %d'C"%temperature)   
   print("*Motor off")  
   print("\n\n") 
     t.sleep(2)
