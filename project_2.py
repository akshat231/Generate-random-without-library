# This is the function which generate Random Number without using any library function
#It works on time module, which gives CPU time.
#HERE IS THE WORKING:
#1. Generate time
#2. Add some number to time to differentiate previously generated time with new time, as sometime it loops very fast and then you will encounter same time
#3. Now we use only the floating digits as these react to even a small change done in previous step
#4. Now we convert floating digits of previous step to integer
#5. We divide it by 1001 to get values between (0- 1000) as remainder of 1001 gives values between [0,1000]
#6. Return the number generated

import time
fg=1
def generate_random_number():
    random=time.time()
    random=random+(fg*0.1)
    random=random-int(random)
    length=len(str(random))
    random=random*pow(10,(length-2))
    random=int(random)
    random=random%1001
    return random

####################################################################################################################################

# This is Visualization of the function by using matplotlib library




import matplotlib.pyplot as plt
list1=[];


for i in range(0,100):
    list1.append(generate_random_number())
    fg=fg+0.5
xs = [x for x in range(len(list1))]
plt.plot(xs,list1)
plt.show()
plt.close()

######################################################################################################################################

#Predict the values of PI

#STEPS TO FIND THE VALUE OF PI
#1. Firstly, we generate random number between 0-9
#2. Then assuming, that radius is 9 as maximum is 9
#3. Now, we apply the formula for PI
#PI generated on my side is 3.09912 on one try, which is preety close to 3.14

jk=1
def generate_close_number():
    random=time.time()
    random=random+(jk*0.1)
    random=random-int(random)
    length=len(str(random))
    random=random*pow(10,(length-2))
    random=int(random)
    random=random%10
    return random

pointsincircle=0

for i in range(0,100000):
    x=generate_close_number()
    jk=jk+1
    y=generate_close_number()
    jk=jk+1
    distanceofpoints=(x*x+y*y)**0.5
    if distanceofpoints<9:
        pointsincircle=pointsincircle+1
pi=4*(pointsincircle/100000)
print(pi)

###################################################################################################################################