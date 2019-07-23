import rospy
from std_msgs.msg import Int16

def stopMovement(ahead, side):
  try:
    stop(ahead, side)
  except rospy.ROSInnterruptException:
    pass

def stop(ahead, side):
  # pulse = rospy.Publisher('pulse', Int16, queue_size=1)
  # pulse.publish(0)
  # stopY = rospy.Publisher('channel_y', Int16, queue_size=1)
  ahead.publish(135)
  # stopX = rospy.Publisher('channel_x', Int16, queue_size=1)
  side.publish(135)
