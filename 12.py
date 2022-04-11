#Convert Hours and Minutes into Seconds

#method 1
def call_convert(time_str):
    h,m,s=time_str.split(":")
    return int(h)*3600+int(m)*60+int(s)
print("Converting into seconds:",call_convert('1:00:00'))
print("Converting into seconds:",call_convert('1:08:57'))
print("Converting into seconds:",call_convert('12:00:00'))
print("Converting into seconds:",call_convert('13:01:50'))


#Method 2

hours=int(input("Enter the hours:"))
min=int(input("Enter the min:"))
sec=int(input("Enter the seconds:"))
time_in_sec=(hours*3600)+(min*60)+sec
print("time in sec:",time_in_sec)
