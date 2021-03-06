#!/usr/bin/env python3
from ev3dev.ev3 import *
import os

os.system('setfont Lat15-TerminusBold14')
L = LargeMotor('outB'); mL.stop_action = 'hold'
R = LargeMotor('outC'); mR.stop_action = 'hold'

msg = 'Hello, my name is EV3!'
print(msg)
Sound.speak(msg).wait()

L.run_to_rel_pos(position_sp= 840, speed_sp = 250)
R.run_to_rel_pos(position_sp=-840, speed_sp = 250)
L.wait_while('running')
R.wait_while('running')