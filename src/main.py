from src.HIDBase import HIDBase

objDev = None

try:
    objDev = HIDBase()
    # objDev.HID_Send_CMD_TopLight(111)

    objDev.open()

    if( input("Do you want test controlbox[0] or motors[1]=>") == "0" ) :

        objDev.HID_Send_CMD_SpotLight(input("Spot light, set value as 0=500 =>"))
        value = input("Top light, set value as 0=500 =>")
        objDev.HID_Send_CMD_TopLight(value)
        value = input("Back light, set value as 0=500 =>")
        objDev.HID_Send_CMD_BackLight(value)
        objDev.HID_Send_CMD_CoaxLight(input("Coax light, set value as 0=500 =>"))
        value = input("VibroTablet, set value as 0=500 =>")
        # objDev.HID_Send_CMD_TopLight(value)
        value = input("Frecency, set value as 0=500 =>")
        # objDev.HID_Send_CMD_TopLight(value)
    else:

        #var = input("Before need turn on power on[0]/off[1]=>")
        if( input("Before need turn on power on[0]/off[1]=>") == "0" ):
            try:
                objDev.power()
                is_loop   = True
                while (is_loop):
                    motor = int(input("Set current motor for test, as [ 0-2 / 9 exit]=>"))
                    if(motor != 9):
                        objDev.set_motor( motor)
                        objDev.set_position( int(input("Set needed position for motor =>")) )
                        if( input("Are you ready to GO [O yes/1 not]:") == "0" ):
                            objDev.JMinus()
                            #objDev.JMinus()
                            if ( input(  "Stop , press 0" ) == "0"):
                                objDev.Abort()
                            else:
                                objDev.Stop()
                    else:
                        is_loop = False

            except Exception as AnyError:
                print(f"Unexpected {AnyError} ")

            finally:
                objDev.power()

        else:
            input( "You don't turn on motor, without energy work not possible , press any key for exit")

except Exception as AnyError:
    print(f"Unexpected {AnyError} ")

finally:
    if objDev is None:
        pass
    else:
        objDev.stop()