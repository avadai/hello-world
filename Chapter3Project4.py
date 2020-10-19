dropHeight = float(input("Enter how high you're dropping the ball, in feet: "))
bounceHeight = float(input("How high does the ball bounce?: "))
numBounce = int(input("How many times does the ball bounce?: "))

bounceIndex = bounceHeight / dropHeight
distance = 0

while numBounce > 0:
    distance = distance + dropHeight
    dropHeight = dropHeight * bounceIndex
    distance = distance + dropHeight
    numBounce -= 1

print("The ball travelled", distance, "feet.")
