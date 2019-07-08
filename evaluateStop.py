import stopMovement
import evaluateMovement

def evaluateStop(state, leftValue, rightValue, distance):
  if state == 'firstStop':
    state = 'stop'
    stopMovement.stopMovement()
  elif state == 'turnRight' and evaluateMovement.evaluateMovement(leftValue, distance):
    stopMovement.stopMovement()
  elif state == 'turnLeft' and evaluateMovement.evaluateMovement(rightValue, distance):
  	stopMovement.stopMovement()
  elif state == 'goAhead' and (evaluateMovement.evaluateMovement(rightValue, distance) or evaluateMovement.evaluateMovement(leftValue, distance)):
    stopMovement.stopMovement()
