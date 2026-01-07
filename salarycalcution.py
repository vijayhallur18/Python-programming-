name=input("enter the employee name:")
emp_id=input("enter the employee id :")
basic_salary=float(input("enter the basic salary :"))

hra=0.20*basic_salary
da=0.10*basic_salary
pf=0.12*basic_salary

net_salary=basic_salary+hra+da-pf

print(" salary summary : ")
print(" employee name :",name)
print("employee_id :",emp_id)
print("basic salary :",basic_salary)
print("HRA (20%):",hra)
print("DA (10%):",da)
print("PF (12%):",pf)
print(" net salary :",net_salary)

