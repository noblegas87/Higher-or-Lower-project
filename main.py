



import art
import game_data
import random

score=0
person_1 = random.choice(game_data.data)
person_2 = random.choice(game_data.data)
while True:
    print(art.logo)
    #print(game_data.data)




    print(f"Compare A:  {person_1['name']}, {person_1['country']}, {person_1['description']}")

    print(art.vs)




    print(f"Compare B:  {person_2['name']}, {person_2['country']}, {person_2['description']}")

    who_has=input("Who has more followers? A or B : ")
    if who_has == 'A' and person_1['follower_count'] > person_2['follower_count']:
        score=score+1
        print(f"You are right. Your current score is {score} ")

        print(f"{person_1['name']} has more follower and they have {person_1['follower_count']} followers")

        person_1=person_2
        person_2 = random.choice(game_data.data)

    elif who_has == 'B' and person_2['follower_count'] > person_1['follower_count']:
        print(f"{person_2['name']} has more follower and they have {person_2['follower_count']} followers")
        score=score+1
        print(f"You are right. Your current score is {score} ")
        person_1=person_2
        person_2=random.choice(game_data.data)

    elif who_has=="A" and person_1['follower_count'] < person_2['follower_count']:
        print("You lose game over")
        break
    elif who_has=="B" and person_1['follower_count'] > person_2['follower_count']:
        print("You lose game over")
        break
    elif who_has=="A" and person_1['follower_count'] == person_2['follower_count']:
        print("Same follower count")
    elif who_has=="B" and person_1['follower_count'] == person_2['follower_count']:
        print("Same follower count")
    else:
        print("Invalid input ")

print(f"Final score is {score}")

