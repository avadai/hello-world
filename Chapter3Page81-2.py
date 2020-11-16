score = int(input("What is your high score (out of 100)?: "))
if score > 90:
    reaction = 'YOU ARE A CHAMPION!!!'
elif score > 70:
    reaction = 'Great job!'
elif score > 50:
    reaction = 'Nice!'
elif score > 25:
    reaction = 'Better luck next time.'
elif score > 0:
    reaction = 'Peeeeeeyew, you stink!'
print(reaction)
