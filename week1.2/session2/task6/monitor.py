# Week 1.2, Session 2: Task 6



temp = int(input(f"Enter Temperature \u00B0C:"))
pressure = int(input("Enter Pressure PSI: "))
status = int(input("Enter Operating Status (1 for operating, 0 for stopped): "))

if temp > 80:
    print("Temperature is too high.")
elif temp >= 50:
    print("Temperature is within safe limits.")
else:
    print("Temperature is low, no action needed")

if pressure > 100:
    print("High pressure detected, Maintenance recommended.")
elif pressure >= 70:
    print("Pressure is stable")
else: 
    print("Pressure is low, system is operating normally.")

if status == 1:
    if temp > 80 or pressure > 100:
        print("Machine operating in unsafe conditions. Shut Down recommended")
    else:
        print("Machine running Normally")
elif status == 0:
    print("Machine stopped no immediate action is needed.")
else:
    print("Invalid Status")
