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

    def get_answer(self):
        with open('q.txt', 'r', encoding='utf-8') as f:
            que_list = f.read().splitlines()
        num_question = random.randrange(0, len(que_list))
        que_answer = str(que_list[num_question])
        for i in range(0, len(que_answer)):
            if que_answer[i] == ';':
                answer = que_answer[i+1:len(que_answer)]
        return answer

    def outputinfo(self, answer):
        curent_view = []
        for i in range(0,len(answer)):
            curent_view.append('*')
        print(''.join(curent_view))

        while True:
            user = input('Введите букву или назовите слово: ')
            if user == answer:
                print('Вы правильно назвали слово!');break
            if (user in answer):
                print('Есть такая буква!')
                for i in range(0,len(answer)):
                    if answer[i]==user:
                        curent_view[i]=user
                        user_answer = ''.join(curent_view)
            else:
                print('Такой буквы нет!')
            if user_answer == answer:
                print('Вы правильно назвали все буквы!');break

            print(user_answer)

# new_game = Game()
# que, ans = new_game.get_question()
# print(que)
# print(new_game.outputinfo(ans))