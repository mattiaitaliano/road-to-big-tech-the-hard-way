from math import factorial

def birthday_probability(n_people):
    s = 365**n_people
    a = factorial(365)/factorial(365-n_people)
    p = 1 - ( a / s )
    return p

if __name__ == '__main__':
    is_input_ok = False
    while (not is_input_ok):
        try:
            n_people = int(input("Total people in the room: "))
            is_input_ok = True
        except ValueError:
            print("Please insert a valid number!")

    p = birthday_probability(n_people)
    print(f"The probability of having 2 birthdays equal between {n_people} people is: {round(p*100, 2)}%")
