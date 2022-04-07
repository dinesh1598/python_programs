#1-hour =3600
#method 1(using funtion)
def hours_2_seconds(hours):
    sec= hours * 3600
    return sec
convert_hours=int(input("(Method1)Enter the number to convert:"))
print(hours_2_seconds(convert_hours))

#method 2(Normal)
hour=int(input("(method2)Enter the number:"))
seconds = hour * 3600
print(seconds)