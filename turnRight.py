import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

def turnRight(pulseValue):
    try:
        startMovimentTurnRight(pulseValue)
    except rospy.ROSInnterruptException:
        pass

def startMovimentTurnRight(pulseValue):
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    pulse = rospy.Publisher('pulse', Int16, queue_size=1)
    pulse.publish(pulseValue)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(100)
