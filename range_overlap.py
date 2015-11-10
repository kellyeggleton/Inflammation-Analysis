def range_overlap(ranges):
  '''Return common overlap among a set of [low,high] ranges.'''
  lowest = 0.0
  highest = 1.0
  for (low, high) in ranges:
	lowest = max(lowest, low)
	highest = min(highest, high)
  return (lowest, highest)     


def test_range_overlap():
  assert range_overlap([  (0.0, 1.0) , (5.0, 6.0)]) == None


test_range_overlap()


