new_vids = 3.00
old_vids = 2.00
num_new = int(input("How many new videos are you renting? "))
num_old = int(input("How many old videos are you renting? "))
new_tot = new_vids * num_new
old_tot = old_vids * num_old
total = new_tot + old_tot
print("Your total is: ", total)