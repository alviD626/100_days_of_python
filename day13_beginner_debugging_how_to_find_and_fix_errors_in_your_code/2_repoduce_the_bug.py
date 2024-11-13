from random import randint

dice_images = ['a', 'b', 'c', 'd', 'e', 'f']
# wrong format
# dice_num = randint(1,6)
dice_num = randint(0, 5)
# print(dice_num)
print(dice_images[dice_num])