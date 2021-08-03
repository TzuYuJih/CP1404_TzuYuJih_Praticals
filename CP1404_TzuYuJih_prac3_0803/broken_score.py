"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
#
# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

import random
def main():
    score = get_user_score()
    if 0 <= score <= 100:
        if score >= 90:
            print("Your score is {}, Excellent!".format(score))
        elif score >= 50 :
            print("Your score is {}, Passable!".format(score))
        else:
            print("Your score is {}, Bad!".format(score))
    else:
        print("Invalid score")
    new_score = create_random_score()
    print(new_score)


def create_random_score():
    new_score = random.randrange(0, 100)
    return new_score


def get_user_score():
    score = float(input("Enter score: "))
    return score


main()