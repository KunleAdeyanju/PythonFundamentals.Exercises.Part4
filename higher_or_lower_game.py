from random import randrange


keep_gooing = True

def rand_number():
    return randrange(10)

def compare_numbers(x,y):
    if x > y:
        print("Too high")
    elif y > x:
        print("Too Low")
    elif x == y:
        print("You guessed correct")

b = int (rand_number())

while(keep_gooing):
    a = int (input("Provide a number between 0 and 10 \n"))   
    compare_numbers(a,b)
    if a == b:
        keep_gooing = False

