def evaluateStop(state, leftValue, rightValue, distance):
  if state == 'firstStop':
    state = 'stop'
    stopMoviment.stopMoviment()
  elif state == 'turnRight' and stopMovement.stopMovement(leftValue, distance):
    stopMoviment.stopMoviment()
  elif state == 'turnLeft' and stopMovement.stopMovement(rightValue, distance):
  	stopMoviment.stopMoviment()
  elif state == 'goAhead' and (stopMovement.stopMovement(rightValue, distance) or stopMovement.stopMovement(leftValue, distance)):
    stopMoviment.stopMoviment()