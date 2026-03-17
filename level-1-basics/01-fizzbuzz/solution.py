# fizzbuzz
# while True:
#     number = int(input("Numero: "))
#     if number == 0:
#         break
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#          print("Buzz")
#     else:
#         print(number)


number = int(input("num:"))
if number == 0:
    print("not")
    exit()

for i in range(1, number):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
         print("Buzz")
    else:
        print(i)