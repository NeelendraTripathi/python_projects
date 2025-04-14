import random

word =["programming","python","hangaman","javascript","java"]
computer_choice=random.choice(word)
chances = 6
display = ''
for i in computer_choice:
    print(i)
    display+='_ '
    
while chances>0 and '_' in display:
    print(display)
    chances = -1
    userinput=input("Guess the word!: ").lower()
    

   