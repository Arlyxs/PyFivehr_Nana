from datetime import datetime

user_input = input(
    "enter your goal with a deadline separated by colon\n e.g. learn python:12.04.2025"
)
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# calculate how many days from now till deadline
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)


print(
    f"\n Dear user! Time remaining for you goal: {goal}, is: {time_till.days} days \n"
)

print(f" Dear user! Time remaining till your goal: {goal}, is {hours_till} hours\n")


print(input_list)
print(datetime.strptime(deadline, "%d.%m.%Y"))
print(today_date)
