hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
if h<=40:
    print(h*float(rate))
else:
	print(40*float(rate)+(h-40)*1.5*float(rate))
	
