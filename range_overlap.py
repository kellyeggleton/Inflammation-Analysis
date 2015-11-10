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
  assert range_overlap([  (0.0, 1.0) ] ) == (0.0, 1.0)
  assert range_overlap([  (0.0, 1.0) ] ) == (0.0, 1.0)
  assert range_overlap([  (2.0, 3.0) , (2.0, 4.0) ]) == None

test_range_overlap()


import xml.etree.ElementTree as tree
print " "
print "Source"
planets_tree = tree.parse('planets.xml')
root=planets_tree.getroot()
print root.attrib['name']
print " "
print "list of planets"
for child in root:
     print "tag=",child.tag, " attrib=", child.attrib['name']
print " "
print "list of moons"
for element  in planets_tree.iter(tag='moon'):
    print element.attrib
print " "
print "Length of Year"
for element in planets_tree.iter(tag='period'):
    print element.text
