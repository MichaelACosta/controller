import rospy
from std_msgs.msg import Int16

def turnLeft(pulseValue, pulse, move):
    try:
        startMovementTurnLeft(pulseValue, pulse, move)
    except rospy.ROSInnterruptException:
        pass

def startMovementTurnLeft(pulseValue, pulse, move):
    #pulse = rospy.Publisher('pulse', Int16, queue_size=1)
    pulse.publish(pulseValue)
    #move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(170)
