from art import logo, vs
from data import data
import random,os

def dataprint(a,b):
    print(logo)
    print(f"{a['name']} a {a['description']} based in {a['country']}."  ) 
    print(vs)
    print(f"{b['name']} a {b['description']} based in {b['country']}."  ) 

def compare(a,b):
    users_ans = str(input("Which of these do you think has higher followers? A or B : ").lower())
    
    print(users_ans)
    if users_ans != "a" and users_ans != "b":
        print("wrong input! try again")
        return compare(a,b)


    max = "a" if a['follower_count'] > b['follower_count'] else "b"
    # print(max)
    if users_ans == max:
        return True
    else:
        return False

def main():
    points = 0
    x = random.choice(data)
    y = random.choice(data)

    notlost = True
    while notlost:
        x = y 
        y = random.choice(data)
        
        while x == y:
            y = random.choice
        os.system('clear')
        print(f"Your current points = {points}")
        dataprint(x,y)
        
        cmp = compare(x,y)
        if cmp:
            print("great job you're right")
            points += 1
            print(f"Your points = {points}")
        else:
            print("You're wrong\nYou lost") 
            print(f"Your points at the end = {points}")
            if points == 0:
                print("Damn! you lost at 0 pts :(\nBetter luck next time")
            elif points > 5:
                print("Damn! thats a great score :)\nThe average is 3.")
            if input("You wanna try again? if yes enter 'y' : ") == "y":
                      main()
            break

main()
