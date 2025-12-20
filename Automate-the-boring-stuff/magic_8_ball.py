import random


def get_answer(answer_no):
    if answer_no == 1:
        return "It is certain"
    elif answer_no == 2:
        return "It is decidedly so"
    elif answer_no == 3:
        return "Yes"
    elif answer_no == 4:
        return "Reply hazy try again"
    elif answer_no == 5:
        return "Ask again later"
    elif answer_no == 6:
        return "Concentrate and ask again"
    elif answer_no == 7:
        return "My reply is no"
    elif answer_no == 8:
        return "Outlook not so good"
    elif answer_no == 9:
        return "Very doubtful"


r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)
