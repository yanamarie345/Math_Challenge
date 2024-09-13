import random

print("Welcome to Math Challenge!")
level = input("\nLevel? Enter Easy(e), Average(a) or Hard(h): ")
no_ques = int()
count = 0
score2 = 0



#for addition
def op_add(start, end):
    ops = "+"
    int1 = random.randint(start, end)
    int2 = random.randint(start, end)
    return int1, int2, ops

#for subtraction
def op_sub(start, end):
    ops = "-"
    while True:
        int1 = random.randint(start, end)
        int2 = random.randint(start, end)
        if int1 > int2:
            return int1, int2, ops

#for multiplication
def op_mul(start, end):
    ops = "*"
    int1 = random.randint(start, end)
    int2 = random.randint(start, end)
    return int1, int2, ops

#for division
def op_div(start, end):
    ops = "/"
    while True:
        int1 = random.randint(start, end)
        int2 = random.randint(start, end)
        if int1 % int2 == 0 and int1 > int2:
            return int1, int2, ops

#for equation
def equation(num1, num2, ops, num_question):
        score = 0
        question = f"{num1} {ops} {num2}"
        answer = eval(question)
        your_ans = int(input(f"{num_question}) {question} = "))
        if answer == your_ans:
            print(f"    {question} = {your_ans} : CORRECT")
            score += 1
            return score
        else:
            print(f"    {question} = {your_ans} : Answer is {answer}")

def repeat2():
    print(f"\nYour total score is: {score2}/{no_ques}")
    again = input("\nContinue? Yes(y) or No(n): ")
    if again == "y":
        level2 = input("Level? Enter Easy(e), Average(a) or Hard(h): ")
        count2 = 0
        return level2, count2
    else:
        print("\nThank you!")
        exit()


while True:
    if level == "e":
        print("\nYou have 10 math questions to answer!")
        no_ques =  10

        while count != no_ques:
            count += 1
            operation = [op_add(1, 30), op_sub(1, 30), op_mul(2, 10), op_div(2, 30)]
            random_ops = random.choice(operation)

            num1_1, num2_1, opera = random_ops
            score1 = equation(num1_1, num2_1, opera, count)
            if score1 == 1:
                score2 += 1

        level, count = repeat2()

    elif level == "a":
        print("\nYou have 25 math questions to answer!")
        no_ques = 25

        while count != no_ques:
            count += 1
            operation = [op_add(11, 100), op_sub(11, 100), op_mul(10, 30), op_div(10, 50)]
            random_ops = random.choice(operation)

            num1_1, num2_1, opera = random_ops
            score1 = equation(num1_1, num2_1, opera, count)
            if score1 == 1:
                score2 += 1

        level, count = repeat2()

    elif level == "h":
        print("\nYou have 50 math questions to answer!")
        no_ques = 50
        while count != no_ques:
            count += 1
            operation = [op_add(100, 1000), op_sub(100, 1000), op_mul(10, 50), op_div(10, 50)]
            random_ops = random.choice(operation)

            num1_1, num2_1, opera = random_ops
            score1 = equation(num1_1, num2_1, opera, count)
            if score1 == 1:
                score2 += 1

        level, count = repeat2()

    else:
        reenter = input("Please enter level, Easy, Medium or Hard: ")
        level = reenter





