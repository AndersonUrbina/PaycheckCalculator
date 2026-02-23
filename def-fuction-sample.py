#def-function-sample.py
#Created by: Anderson Urbina
#Description: This function calculates your gross income, net pay, taxes, and deductions based on
# your hourly wage and weekly hours worked, and programs you are enroll in..

print("\nHello, This program will calculate your gross income, net pay, taxes, and deductions based on"
    " your hourly wage, weekly hours worked, and programs you are enroll in.")

#This part validates the input in both payment and hours
while True:
    try:
        payment = float(input("\nPlease enter your weekly hourly payment: "))
        break
    except ValueError:
        print("\nInvalid. Input Please enter a number (ex, 18).")
while True:
    try:
        hours = float(input("Please enter the hours worked: "))
        break
    except ValueError:
        print("\nInvalid Input. Please enter a number (ex, 40).")

#Function that validates the answer
def get_answer(prompt):
    while True:
        answer = input(prompt).strip().lower()[:3]
        if answer in {"y", "yes"}:
            return "y"
        elif answer in {"n", "no",}:
            return "n"
        else:
            print('\nInvalid Input. Please enter a valid answer "y" or "n".')

#This part ask about programs
charity_program = get_answer("Are you in the charity program? y/n: ")
celebrations_program = get_answer("Are you in the celebrations program? y/n: ")

#def function to calculate gross income
def gross_income(payment, hours):
    return payment * hours

#def function to calculate taxes
def taxes(gross):
    return gross * 0.12

#def function to calculate deductions and add in enroll in any program
def deductions(charity_program, celebrations_program):
    total_deduction = 0
    if celebrations_program in {"y"}:
        total_deduction += 1.0
    if charity_program in {"y"}:
        total_deduction += 0.5
    return total_deduction

#def function to calculate net pay
def net_pay(gross, tax, deduction):
    return gross - tax - deduction

#Main calculations
gross = gross_income(payment, hours)
tax =  taxes(gross)
deduct = deductions(charity_program, celebrations_program)
net = net_pay(gross, tax, deduct)

#Print entire pay summary
print("\nHere is your pay summary:")
print(f"Your weekly gross income is ${gross:.2f} ")
print(f"Your weekly taxes are ${tax:.2f} ")
print(f"Your weekly deductions are ${deduct:.2f} ")
print(f"Your Net pay is ${net:.2f}")