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
import pyb

if __name__ == '__main__':
    ## A variable that creates a encoder driver for encoder 1.
    encoder_drv1 = encoder_agena_chiu.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    ## A variable that creates a encoder driver for encoder 2.
    encoder_drv2 = encoder_agena_chiu.EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    ## A variable that creates a motor driver for motor 1.
    motor_drv1 = motor_agena_chiu.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    ## A variable that creates a motor driver for motor 2.
    motor_drv2 = motor_agena_chiu.MotorDriver(pyb.Pin.cpu.C1, pyb.Pin.cpu.A0, pyb.Pin.cpu.A1, 5)
    # Enable both motors.
    motor_drv1.enable()
    motor_drv2.enable()
    # Set the duty cycle for both motors.
    motor_drv1.set_duty_cycle(50)
    motor_drv2.set_duty_cycle(50)
    # While loop to continuously print the position of both encoders.
    while True:
        print('Encoder 1 position: ' + str(encoder_drv1.read()))
        print('Encoder 2 position: ' + str(encoder_drv2.read()))