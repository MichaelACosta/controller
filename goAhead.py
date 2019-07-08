import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

def goAhead(pwmValue):
    try:
        startMovimentAhead(pwmValue)
    except rospy.ROSInnterruptException:
        pass

def startMovimentAhead(pwmValue):
    if pwmValue < 175:
        pwmValue = 175
    elif pwmValue > 205:
        pwmValue = 205
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_y', Int16, queue_size=1)
    move.publish(pwmValue)
