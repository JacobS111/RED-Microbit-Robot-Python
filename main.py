# PYTHON MICROBIT

# RADIO ROUTINES OUT
def send_left():
   radio.send_value("left", 90)
def send_right():
   radio.send_value("right", 90)
def send_forwards():
   radio.send_value("forward", 1)
def send_stop():
   radio.send_value("stop", 0)

# INPUT RESPONDS
def on_button_pressed_a():
   send_left()
def on_button_pressed_ab():
   send_forwards()
def on_button_pressed_b():
   send_right()
def on_stop_movement():
   send_stop()

#DEFINEFOREVER
def on_forever():
   if input.button_is_pressed(Button.AB):
       on_button_pressed_ab()
   elif input.button_is_pressed(Button.A):
       on_button_pressed_a()
   elif input.button_is_pressed(Button.B):
       on_button_pressed_b()
   else:
       on_stop_movement()

# RADIO RESPONDS
def on_received_value(name, value):
   if name == "left":
       Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.LEFT, 50)
   elif name == "right":
       # basic.show_number(-1)
       # basic.show_number(1)
       Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.RIGHT, 50)
   elif name == "forward":
       Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 50)
   elif name == "stop":
       Kitronik_Move_Motor.stop()
   else:
       basic.show_string("E")
       print("ERROR")


# RADIO TRIGGER
radio.on_received_value(on_received_value)


#SETUP
radio.set_group(5)
basic.show_number(0)



#DOFOREVER
basic.forever(on_forever)


