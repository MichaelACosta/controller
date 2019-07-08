import rospy
import goAhead
import turnLeft
import turnRight
import stopMovement
import degreToMeters
import evaluateStop

from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import String

leftValue = 0
rightValue = 0
distance = 0.0
state = 'firstStop'

def callbackLeft(data):
  global leftValue, state, leftValue, rightValue, distance
  leftValue = int(data.data)
  evaluateStop.evaluateStop(state, leftValue, rightValue, distance)

def callbackRight(data):
  global rightValue, state, leftValue, rightValue, distance
  rightValue = int(data.data)
  evaluateStop.evaluateStop(state, leftValue, rightValue, distance)

def callbackWalk(data):
  global state, distance
  value = data.data
  command = value.split(" ")
  if command[0] == 'goAhead':
    state = 'goAhead'
    distance = float(command[1])
    goAhead.goAhead(int(command[2]))
  elif command[0] == 'turnLeft':
    state = 'turnLeft'
    distance = degreToMeters.degreToMeters(float(command[1]))
    turnLeft.turnLeft()
  elif command[0] == 'turnRight':
    state = 'turnRight'
    distance = degreToMeters.degreToMeters(float(command[1]))
    turnRight.turnRight()
  elif command[0] == 'stop':
    state = 'stop'
    stopMovement.stopMovement()

def listener():
  rospy.Subscriber("left_sensor", Int16, callbackLeft)
  rospy.Subscriber("right_sensor", Int16, callbackRight)
  rospy.Subscriber("walk", String, callbackWalk)
  rospy.spin()

if __name__ == '__main__':
  rospy.init_node('test', anonymous=True)
  listener()
