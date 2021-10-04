import random

class Game:

    def get_question(self):
        with open('q.txt', 'r', encoding='utf-8') as f:
            question_list = f.read().splitlines()
        number_question = random.randrange(0, len(question_list))
        question_answer = str(question_list[number_question])
        for i in range(0, len(question_answer)):
            if question_answer[i] == ';':
                answer = question_answer[i + 1:len(question_answer)]
                question = question_answer[0:i]
        return question, answer

# new_game = Game()
# que, ans = new_game.get_question()
# print(que)
# print(new_game.outputinfo(ans))