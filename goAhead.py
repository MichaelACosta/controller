import rospy
from std_msgs.msg import Int16

def goAhead(pwmValue, pulseValue):
    try:
        startMovementAhead(pwmValue, pulseValue)
    except rospy.ROSInnterruptException:
        pass

def startMovementAhead(pwmValue, pulseValue):
    if pwmValue < 175:
        pwmValue = 175
    elif pwmValue > 205:
        pwmValue = 205
    pulse = rospy.Publisher('pulse', Int16, queue_size=1)
    pulse.publish(pulseValue)
    move = rospy.Publisher('channel_y', Int16, queue_size=1)
    move.publish(pwmValue)
