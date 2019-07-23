#!/usr/bin/env python
import rospy
import goAhead
import turnLeft
import turnRight
import stopMovement
import degreeToMeters
import meterToPulse

from std_msgs.msg import Int16
from std_msgs.msg import String

#pattern_pub = rospy.Publisher('pattern', Bool, queue_size=10)
pulse_pub = rospy.Publisher('pulse', Int16, queue_size=10)
move_ahead_pub = rospy.Publisher('channel_y', Int16, queue_size=10)
move_side_pub = rospy.Publisher('channel_x', Int16, queue_size=10)

#state = 'init'

def callbackWalk(data):
  #global state
  value = data.data
  command = value.split(" ")
  # if state == 'init':
  #   stopMovement.stopMovement()
  #   state = 'stop'
  # elif command[0] == 'goAhead':
  if command[0] == 'goAhead':
    pulse = meterToPulse.meterToPulse(float(command[1]))
    goAhead.goAhead(int(command[2]), int(pulse), pulse_pub, move_ahead_pub)
  elif command[0] == 'turnLeft':
    distance = degreeToMeters.degreeToMeters(float(command[1]))
    pulse = meterToPulse.meterToPulse(float(distance))
    turnLeft.turnLeft(int(pulse), pulse_pub, move_side_pub)
  elif command[0] == 'turnRight':
    distance = degreeToMeters.degreeToMeters(float(command[1]))
    pulse = meterToPulse.meterToPulse(float(distance))
    turnRight.turnRight(int(pulse), pulse_pub, move_side_pub)
  elif command[0] == 'stop':
    stopMovement.stopMovement(move_ahead_pub, move_side_pub)

def listener():
  rospy.Subscriber("walk", String, callbackWalk)
  rospy.spin()

if __name__ == '__main__':
  rospy.init_node('test', anonymous=True)
  listener()
