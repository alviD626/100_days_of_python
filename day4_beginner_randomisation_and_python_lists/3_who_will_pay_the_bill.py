import random

friends = ["Alice","Bob","Charlie","David","Emanuel"]
# random_friend_list = random.shuffle(friends)

# option1
random_friend = random.choice(friends)
print(random_friend)



# option2 
find_billed_person = random.randint(0,4)
print(friends[find_billed_person])