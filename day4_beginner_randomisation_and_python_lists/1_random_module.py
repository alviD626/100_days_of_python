import random 


random_integer = random.randint(1,10)
print(f"Random Integer: {random_integer}")


random_number_0_to_1 = random.random()
print(f"Random Number between 0 and 1: {random_number_0_to_1}")


random_float = random.uniform(1,10)
print(f"Random float number between 1 and 10: {random_float}")


print("Heads or Tails")
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")


num_list = [1,2,4,6,8,3]
random_num = random.choice(num_list)
print(random_num)