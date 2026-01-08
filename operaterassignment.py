price=1500
gst=price*18/100
total_bill=price+gst
print("product price :",price)
print("gst amount :",gst)
print("total bill amount :",total_bill)

student=53
groups=5
remainder=student%groups
print("remaing students :",remainder)

power=2
time=3
consumption=power**time
print("power consumption :",consumption)

#relational operater
age=20
if age>=18:
    print("eligibale to vote")
else:
    print("not eligibale")

salary1=450000
salary2=300000
if salary1>salary2:
    print("employee1 earns more ")
else: 
    print("employee2 earns more")

saved_pin=1234
entered_pin=1234

print("pin correct :",saved_pin==entered_pin)


#logical operater

marks=65
attendence=80
if marks>40 and attendence>75 :
    print("student passed")
else:
    print("student failed")

is_suspended=False
if not is_suspended:
    print("acess granted")
else:
    print("acess blocked")

#assignment operaters

wallet=2000
wallet -=750
print("remaining wallet balance :",wallet)

#identity operaters
a=10
b=10
c=20

print(a is b)
print(a is not b)
