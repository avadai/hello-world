hour_wage = int(input("Enter how much you make per hour: "))
total_hours = int(input("Enter how many hours you've worked this week: "))
over_time = int(input("How many overtime hours have you worked?: "))
overtime_pay = hour_wage * 1.5 * over_time
non_overtime_pay = total_hours - over_time
weekly_pay = non_overtime_pay * hour_wage + overtime_pay
print("Your pay for this week is: $", weekly_pay)