# Determine the height of the tower that can be reached by the ladder, given the length and angle in which the ladder has to be leaned on the tower.
# Write PAC, flowchart and python code for determining the height of the tower.
# Length of the ladder is given in feet and angle to lean the ladder is given in degrees.
# Display the height of the tower, with two decimal places.

import math

ladder_length = int(input())
deg_angle = int(input())

rad_angle = (math.pi / 180) * deg_angle

ladder_reach = ladder_length * math.sin(rad_angle)

print(round(ladder_reach, 2))
