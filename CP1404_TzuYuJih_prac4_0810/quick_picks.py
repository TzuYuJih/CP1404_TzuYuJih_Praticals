import random

picks = int(input("How many picks: "))
list_for_a_pick = []
for i in range(picks):
    while len(list_for_a_pick) < 6:
        # list_for_a_pick.append(random.randint(1, 45))
        # list_for_a_pick = sorted(list_for_a_pick)
            created_random = random.randint(1, 45)
            if created_random not in list_for_a_pick:
                list_for_a_pick.append(created_random)
            else:
                created_random = random.randint(1,45)
            list_for_a_pick = sorted(list_for_a_pick)
    print(list_for_a_pick)
    list_for_a_pick.clear()