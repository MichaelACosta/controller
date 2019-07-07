import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

def turnLeft():
    try:
        startMovimentTurnLeft()
    except rospy.ROSInnterruptException:
        pass

def startMovimentTurnLeft():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(170)
