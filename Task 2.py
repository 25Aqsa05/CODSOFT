
num1=int(input("Enter 1st Number :"))
num2=int(input("Enter 2nd Number :"))

def calc_menu():
    print("\n--CALCULATOR MENU--")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISON")
    print("5. MODULUS")
    print("6. POWER")
    print("7. Exit")
def calc_add(a,b):
    add_result= a + b
    print(f"Addition of [{a}] and [{b}] is: { add_result}. ")
def calc_sub(a,b):
    sub_result= a - b
    print(f"Substraction of [{a}] and [{b}] is: { sub_result}. ")
def calc_mul(a,b):
    mult_result = a * b
    print(f"Multiplication of [{a}] and [{b}] is: { mult_result}. ")
def calc_div(a,b):
    div_result = a / b
    print(f"Divison of [{a}] and [{b}] is: { div_result}. ")
def calc_mod(a,b):
    mod_result = a % b
    print(f"Modulus of [{a}] and [{b}] is: { mod_result}. ")
def calc_pow(a,b):
    pow_result = a ** b
    print(f"Power of [{a}] and [{b}] is: { pow_result}. ")
while True:
    calc_menu()
    user_choice = input("Choose an option (1 to 6): ")

    if user_choice == '1':
       calc_add(num1,num2)
    elif user_choice == '2':
       calc_sub(num1,num2)
    elif user_choice == '3':
       calc_mul(num1,num2)
    elif user_choice == '4':
        calc_div(num1,num2)
    elif user_choice == '5':
        calc_mod(num1,num2)
    elif user_choice == '6':
        calc_pow(num1,num2)
    elif user_choice == '7':
        print("Thanks for using Calculator.")
        break
