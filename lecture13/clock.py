import time

# Demonstrate nested loops
for i in range(24): # index i loops over 24 hrs in the day
    for j in range(60): # index j loops over 60 mins in a hr
        for k in range(60): # index k loops over 60 secs in a min
            print(f"{i}:{j}:{k}") # print the output
            time.sleep(1) # pause 1 sec
