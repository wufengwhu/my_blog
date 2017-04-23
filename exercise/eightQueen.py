def conflict(state, nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i] - nextX) in (0, nextY - i):
			return True
		return False 