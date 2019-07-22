#!/usr/bin/env python
import rospy
import goAhead
import turnLeft
import turnRight
import stopMovement
import degreeToMeters
import meterToPulse

from std_msgs.msg import String

state = 'init'

def callbackWalk(data):
  global state
  value = data.data
  command = value.split(" ")
  if state == 'init':
    stopMovement.stopMovement()
    state = 'stop'
  elif command[0] == 'goAhead':
    pulse = meterToPulse.meterToPulse(float(command[1]))
    goAhead.goAhead(int(command[2]), int(pulse))
  elif command[0] == 'turnLeft':
    distance = degreeToMeters.degreeToMeters(float(command[1]))
    pulse = meterToPulse.meterToPulse(float(distance))
    turnLeft.turnLeft(int(pulse))
  elif command[0] == 'turnRight':
    distance = degreeToMeters.degreeToMeters(float(command[1]))
    pulse = meterToPulse.meterToPulse(float(distance))
    turnRight.turnRight(int(pulse))
  elif command[0] == 'stop':
    stopMovement.stopMovement()

def listener():
  rospy.Subscriber("walk", String, callbackWalk)
  rospy.spin()

if __name__ == '__main__':
  rospy.init_node('test', anonymous=True)
  listener()
