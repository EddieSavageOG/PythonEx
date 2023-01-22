# Magic 8 Ball done badly

name = input("What is your name? ")
question = input("What is your question? ")
answer = ""
lucky_number = ""

import random

result = random.randint (1, 20)

if result == 1: 
    answer = "It is decidedly so."
elif result == 2:
    answer = "It is certain."
elif result == 3: 
    answer = "Without a doubt."
elif result == 4:
    answer = "Yes, definitely."
elif result == 5:
    answer = "You may rely on it."
elif result == 6:
    answer = "As I see it, yes."
elif result == 7:
    answer = "Most likely."
elif result == 8:
    answer = "Outlook good."
elif result == 9:
    answer = "Yes."
elif result == 10:
    answer = "Signs point to yes."
elif result == 11:
    answer = "Reply hazy, try again."
elif result == 12:
    answer = "Ask again later."
elif result == 13:
    answer = "Better not tell you now."
elif result == 14:
    answer = "Cannot predict now."
elif result == 15:
    answer = "Concentrate and ask again."
elif result == 16:
    answer = "Don't count on it."
elif result == 17:
    answer = "My reply is no."
elif result == 18:
    answer = "My sources say no."
elif result == 19:
    answer = "Outlook not so good."
elif result == 20:
    answer = "Very doubtful."
else:
    answer = "OMG an error!"

print(name + " asks: " + question)
print("I am seeing... " + answer)

TODO: Add a lucky number too, duh!
TODO: Integrate into a website instead of the CLI
