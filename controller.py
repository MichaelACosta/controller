#!/usr/bin/env python
import rospy
import goAhead
import turnLeft
import turnRight
import stopMovement
import degreToMeters
import meterToPulse

from std_msgs.msg import String

def callbackWalk(data):
  value = data.data
  command = value.split(" ")
  if command[0] == 'goAhead':
    pulse = meterToPulse.meterToPulse(float(command[1]))
    goAhead.goAhead(int(command[2]), pulse)
  elif command[0] == 'turnLeft':
    distance = degreToMeters.degreToMeters(float(command[1]))
    pulse = meterToPulse.meterToPulse(distance)
    turnLeft.turnLeft(pulse)
  elif command[0] == 'turnRight':
    distance = degreToMeters.degreToMeters(float(command[1]))
    pulse = meterToPulse.meterToPulse(distance)
    turnRight.turnRight(pulse)
  elif command[0] == 'stop':
    stopMovement.stopMovement()

def listener():
  rospy.Subscriber("walk", String, callbackWalk)
  rospy.spin()

if __name__ == '__main__':
  rospy.init_node('test', anonymous=True)
  listener()
