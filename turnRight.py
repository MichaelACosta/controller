import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

def turnRight():
    try:
        startMovimentTurnRight()
    except rospy.ROSInnterruptException:
        pass

def startMovimentTurnRight():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(100)
