import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

def stopMovement():
  try:
    stop()
  except rospy.ROSInnterruptException:
    pass

def stop():
  pub = rospy.Publisher('pattern', Bool, queue_size=1)
  pub.publish(True)
  stopy = rospy.Publisher('channel_y', Int16, queue_size=1)
  stopy.publish(135)
  stopx = rospy.Publisher('channel_x', Int16, queue_size=1)
  stopx.publish(135)
