import rospy
import goAhead
import turnLeft
import turnRight
import stopMoviment

from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import String

leftValue = 0
rightValue = 0
state = 'firstStop'
circumference = 3.14*0.34

def callbackLeft(data):
  global leftValue
  leftValue = int(data.data)
  evaluateStop()

def callbackRight(data):
  global rightValue
  rightValue = int(data.data)
  evaluateStop()

def callbackWalk(data):
  global state
  if data.data == 'go ahead':
    state = 'goAhead'
    goAhead.goAhead()
  elif data.data == 'turn left':
    state = 'turnLeft'
    turnLeft.turnLeft()
  elif data.data == 'turn right':
    state = 'turnRight'
    turnRight.turnRight()
  elif data.data == 'stop':
    state = 'stop'
    stopMoviment.stopMoviment()

def stopGoAhead(value, distance):
  global circumference
  return (value/300.0)*circumference >= distance

def stopTurn(value):
  return value >= 100

def evaluateStop():
  global state
  global leftValue
  global rightValue

  if state == 'firstStop':
    state = 'stop'
    stopMoviment.stopMoviment()
  elif state == 'turnRight' and stopTurn(leftValue):
    stopMoviment.stopMoviment()
  elif state == 'turnLeft' and stopTurn(rightValue):
  	stopMoviment.stopMoviment()
  elif state == 'goAhead' and (stopGoAhead(rightValue, 1.0) or stopGoAhead(leftValue, 1.0)):
    stopMoviment.stopMoviment()

def listener():
  rospy.Subscriber("left_sensor", Int16, callbackLeft)
  rospy.Subscriber("right_sensor", Int16, callbackRight)
  rospy.Subscriber("walk", String, callbackWalk)
  rospy.spin()

if __name__ == '__main__':
  rospy.init_node('test', anonymous=True)
  listener()