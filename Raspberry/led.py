import RPi.GPIO as GPIO                 
import time                             
                                        
def breath(port=12,step=3):             
    GPIO.setmode(GPIO.BOARD)            
    GPIO.setup(port,GPIO.OUT)           
                                        
    pwm = GPIO.PWM(port,50)             
    pwm.start(0)                        
                                        
    try:                                
        while(True):                    
            for i in range(0,101,2):    
                pwm.ChangeDutyCycle(i)  
                time.sleep(step/100.)   
                                        
            for i in range(100,-1,-2):  
                pwm.ChangeDutyCycle(i)  
                time.sleep(step/100.)   
                                        
    except KeyboardInterrupt:           
        pwm.stop()                      
        GPIO.cleanup()                  
                                        
if __name__ == '__main__':              
    breath()                            
