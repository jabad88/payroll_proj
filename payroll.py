#Student: Joshua Abadies

num_employee = int(input("Enter the number of employees: "))

employees=[]

total_gross = 0
total_deductions = 0
total_net = 0

for x in range(num_employee):
    #collect data
    name = input("Enter the employees name: ")
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))

    #compute gross wages, deductions and net wages
    if hours > 40:
        gross = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        gross = (hours * rate)

    total_gross += gross

    if gross > 200:
        deductions = (gross* .15)
    else:
        deductions = 0

    total_deductions += deductions

    net = (gross - deductions)

    total_net += net

    emp = [name,hours,rate,gross,deductions,net]
    employees.append(emp)

print("\n")

#Payroll Report
print("Payroll Report","\n")
print("--------------------------")

print("Name Hours Rate Gross Deductions Net")
for x in employees:
    print(f"{x[0]}  {x[1]}  {x[2]}  {x[3]}  {x[4]}  {x[5]}")

print("\n")

#Final Totals
print(f"Total Gross for all employees: {total_gross}")
print(f"Total Deductions for all employees: {total_deductions}")
print(f"Total Net for all employees: {total_net}")



