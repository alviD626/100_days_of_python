def life_in_weeks(age):
    you_lived =  age * 52
    total = 90 *52
    left = total - you_lived
    return f"You have {left} weeks left."

age = int(input())
life_in_weeks(age)