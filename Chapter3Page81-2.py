score = int(input("What is your high score (out of 1000)?: "))
if score > 900:
    reaction = 'YOU ARE A CHAMPION!!!'
elif score > 700:
    reaction = 'Great job!'
elif score > 500:
    reaction = 'Nice!'
elif score > 250:
    reaction = 'Better luck next time.'
elif score > 0:
    reaction = 'Peeeeeeyew, you stink!'
print(reaction)