#Write a program to print the sum of the polygon angle side in degree . Take
#side of angle input from console


def polygon_angle():
    n = int(input("Enter the number of sides: "))
    ans = (n-2) * 180
    statement = "The sum of interior angles of a polygon is : " + str(ans) 
    return statement
print(polygon_angle())