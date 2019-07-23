import rospy
from std_msgs.msg import Int16

def turnRight(pulseValue, pulse, move):
    try:
        startMovementTurnRight(pulseValue,pulse, move)
    except rospy.ROSInnterruptException:
        pass

def startMovementTurnRight(pulseValue, pulse, move):
    #pulse = rospy.Publisher('pulse', Int16, queue_size=1)
    pulse.publish(pulseValue)
    #move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(95)
