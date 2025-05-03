drive_motor = "6_5169793973449801317"
arm_motor = "6_1121225532052018424"
servo = "4_1833482520634428295"
deadband = 0.1
servo_status = 0
arm_position = 0

def teleop_setup():
    global servo_status
    # global arm_position
    servo_status = 0
    arm_position = 0
    #Robot.set_value(arm_motor, "velocity_a", 1.0)
    #Robot.set_value(arm_motor, "velocity_b", 1.0)
    #print(Robot.get_value(arm_motor, "velocity_a"))
    #print(Robot.get_value(arm_motor, "velocity_b"))
    print ("Tele-operated mode has started!")

def teleop_main():
    # if y is negavite or down check x
    right_y = Gamepad.get_value("joystick_right_y")
    if abs(right_y) < deadband:
        right_y = 0
    right_x = Gamepad.get_value("joystick_right_x")
    if abs(right_x) < deadband:
        right_x = 0
       
    up = Gamepad.get_value("dpad_up")
    down = Gamepad.get_value("dpad_down")
  
    if right_y > 0:
        #if x is below -0.1 go left if it is above 0.1 go right if nether go down
        if right_x < -0.1:
            Robot.set_value(drive_motor, "velocity_a", -1)
            Robot.set_value(drive_motor, "velocity_b", -1)
        elif right_x > 0.1:
            Robot.set_value(drive_motor, "velocity_a", 1)
            Robot.set_value(drive_motor, "velocity_b", 1)
        else:
            Robot.set_value(drive_motor, "velocity_a", 1)
            Robot.set_value(drive_motor, "velocity_b", -1)
# if y is positve or up check x
    elif right_y < 0:
        #if x is below -0.1 go left if it is above 0.1 go right if nether go up
        if right_x < -0.1:
            Robot.set_value(drive_motor, "velocity_a", -1)
            Robot.set_value(drive_motor, "velocity_b", -1)
        elif right_x > 0.1:
            Robot.set_value(drive_motor, "velocity_a", 1)
            Robot.set_value(drive_motor, "velocity_b", 1)
        else:
            Robot.set_value(drive_motor, "velocity_a", -1)
            Robot.set_value(drive_motor, "velocity_b", 1)
#else do nothing
    else:
        Robot.set_value(drive_motor, "velocity_a", 0)
        Robot.set_value(drive_motor, "velocity_b", 0)
    
    if up == True:
        Robot.set_value(arm_motor, "velocity_a", -1)
        Robot.set_value(arm_motor, "velocity_b", -1)
        
        
    elif down == True:
        Robot.set_value(arm_motor, "velocity_a", 1)
        Robot.set_value(arm_motor, "velocity_b", 1)
        
    else:
        Robot.set_value(arm_motor, "velocity_a", 0)
        Robot.set_value(arm_motor, "velocity_b", 0)

# AUTONOMOUS

def autonomous_setup():
    print ("Autonomous mode has started!")
    Robot.set_value(drive_motor,"pid_enabled_a", False)
    Robot.set_value(drive_motor,"pid_enabled_b", False)
    Robot.run(autonomous_actions)
        # robot.sleep()
# autonomous_actions

def autonomous_main():
    pass

def autonomous_actions():
    starttime = time.time()
    print ("Autonomous action sequence started")
    print ("1 second has passed in autonomous mode")
    #driving
    Robot.set_value(drive_motor, "velocity_a", -1)
    Robot.set_value(drive_motor, "velocity_b", 1)
    # number is time in seconds
    while time.time() - starttime < 1:
        pass
    Robot.set_value(drive_motor, "velocity_a", 0)
    Robot.set_value(drive_motor, "velocity_b", 0)
    

