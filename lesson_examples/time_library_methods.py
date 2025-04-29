# Imported library
import time


# Get the timezone at the Unix epoch
print(time.gmtime(0))


# Get the current time in seconds since the epoch
current_time_since_epoch = time.time()

print("Current time in seconds since epoch =", current_time_since_epoch)


# Get the time string from seconds
current_time = time.ctime(current_time_since_epoch)

print("Current time:", current_time) 


# Delay execution of programs
time.sleep(6)



# Convert struct_time of gmtime or localtime 
# To string as specified by format argument
from time import gmtime, strftime

s = strftime("%a, %d %b %Y %H:%M:%S", 
             gmtime(current_time_since_epoch))

print(s)

# To the form: Day Mon Date Hour:Min:Sec Year
obj = time.gmtime(current_time_since_epoch)

time_str = time.asctime(obj)

print(time_str)
