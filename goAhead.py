import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

def goAhead():
    try:
        startMovimentAhead()
    except rospy.ROSInnterruptException:
        pass

def startMovimentAhead():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_y', Int16, queue_size=1)
    move.publish(175)
