'''!
@file main.py
This is the main file for Lab 1, where two motor driver and encoder driver objects are created to run functions,
such as setting duty cycles for the motors and printing encoder position.
@author Corey Agena
@author Luisa Chiu
@date 1-26-2022
'''

# Import the required modules to run the motor and encoder 
import motor_agena_chiu
import encoder_agena_chiu
import controller_agena_chiu
import pyb
import utime

if __name__ == '__main__':
    ## A variable that creates a encoder driver for encoder 1.
    encoder_drv1 = encoder_agena_chiu.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    ## A variable that creates a encoder driver for encoder 2.
#    encoder_drv2 = encoder_agena_chiu.EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    ## A variable that creates a motor driver for motor 1.
    motor_drv1 = motor_agena_chiu.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    ## A variable that creates a motor driver for motor 2.
#    motor_drv2 = motor_agena_chiu.MotorDriver(pyb.Pin.cpu.C1, pyb.Pin.cpu.A0, pyb.Pin.cpu.A1, 5)
    controller = controller_agena_chiu.ControllerDriver(0, 0)
    
    # Enable both motors.
    motor_drv1.enable()
#    motor_drv2.enable()
    # Set the duty cycle for both motors.

    #Encoder: 256 ticks/ 1 rev
    #pos = input('Choose a setpoint')
    pos = 256*16*4
    controller.set_setpoint(pos) #change this to user input later
    # While loop to continuously print the position of both encoders.    
    #gain = input('Choose a gain')
    gain = 0.3
    controller.set_gain(gain) #change this to user input later
    start = utime.ticks_ms()
    difference = 0
    time = []
    enc_pos = []
    while True:
        x = input('Input Kp to run step response, input s to stop')
        try:
            float(x)
        except:
            while difference <= 1000:
                current = utime.ticks_ms()
                difference = current - start
        #        print('Encoder 2 position: ' + str(encoder_drv2.read()))
                duty_cycle = controller.run(encoder_drv1.read())
                motor_drv1.set_duty_cycle(duty_cycle)
                utime.sleep_ms(10)
                time.append(difference)
                enc_pos.append(encoder_drv1.read())
            i = 0
            for x in time:
                print(time[i], enc_pos[i])
                i += 1
        else:
            if x == 's':
                break
