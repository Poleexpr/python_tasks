number = 123456

number_path = number // 1000
one = number_path // 100
two = number_path // 10 % 10
three = number_path % 10

number_path_two = number % 1000
four = number_path_two // 100
five = number_path_two // 10 % 10
six = number_path_two % 10

if one + two + three == four + five + six:
	print("Счастливый билет")
else: 
	print("Несчастливый билет")
