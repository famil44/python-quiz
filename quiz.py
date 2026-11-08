import random
class Quiz:
    def __init__(self):
        self.score = 0
        self.questions = []
        with open('questions.txt','r') as q:
            for line in q:
                line = line.strip()    # To remove extra spaces
                line = line.split(',')
                self.questions.append(line)
            self.questions=random.sample(self.questions,5)   # takes 5 random questions
        
    def display_question(self):
        for qnum,i in enumerate(self.questions,start=1):
            print(qnum,i[0])
            print(i[1])
            print(i[2])
            print(i[3])
            print(i[4])
            while True:
                user_ans=input("Enter your answer (A/B/C/D):")
                if user_ans in ['A','B','C','D','a','b','c','d']:
                    break
                print('Invalid Option')
            self.check_answer(user_ans,i[5])
    
    def check_answer(self,answer,correct_answer):
        if answer.upper()==correct_answer:
            self.score+=1
            print("Correct Answer!!!")
        else:
            print("Wrong Answer!!!")
            print('Correct Answer was:',correct_answer)
        print()
            
    def show_score(self):
        if self.score==5:
            print('You scored:5/5 Perfect Score!!!')
        elif self.score==4:
            print('You scored:4/5 Great Job!!')
        elif self.score==3:
            print('You scored:3/5 Good effort!')
        else:
            print('You scored:',self.score,'/',5,'Keep Practicing')
                
                

print('Welcome to the Python Quiz!')
while True:
    quiz = Quiz()
    quiz.display_question()
    quiz.show_score()
    again = input('Do you want to play again? (y/n):').lower()
    if again!='y':
        print('Thanks For Playing.Good Bye!')
        break