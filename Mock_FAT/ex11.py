# A particle is projected from the surface of the earth with a speed of u m/s at an angle of 𝛳 (in degrees).

# Calculate the time of the flight, range, and maximum height using the following formulae:

# t (time of flight) = 2*u*sin(theta)/g
# r (range) = u^2*(sin(2*theta))/g
# h (maximum height) = u^2*(sin^2(theta))/2g
# g = 10m^2/s^2

# Use math module to convert theta from degrees to radians (math.radians), and calculating the sin(𝛳)

# Sample input
# 20
# 30
# Sample output
# 2.0
# 34.64
# 5.0

def projectile_calc(input_speed0, input_angle_deg0):
    t = (2 * input_speed0 * math.sin(math.radians(input_angle_deg0))) / 10
    r = ((input_speed0 ** 2) * math.sin(2 * math.radians(input_angle_deg0))) / 10
    h = ((input_speed0 ** 2) * (math.sin(math.radians(input_angle_deg0)) ** 2 )) / (2 * 10)  
    
    return [t, r, h]


def main():
    input_speed = float(input())
    input_angle = float(input())
    result = projectile_calc(input_speed, input_angle)
    for element in result:
        print(round(element, 2))


if __name__ == "__main__":
    import math
    main()
    
