import rospy
from std_msgs.msg import Int16

def stopMovement():
  try:
    stop()
  except rospy.ROSInnterruptException:
    pass

def stop():
  pulse = rospy.Publisher('pulse', Int16, queue_size=1)
  pulse.publish(0)
  stopY = rospy.Publisher('channel_y', Int16, queue_size=1)
  stopY.publish(135)
  stopX = rospy.Publisher('channel_x', Int16, queue_size=1)
  stopX.publish(135)
