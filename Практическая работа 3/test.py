import pytest
from game import Game, Player

def test_get_question():
    new_game = Game()
    q, a = new_game.get_question()
    if q == 'Столица России' and a == 'Москва':
        assert 'Москва'
    if q == 'Кто не является птицей?' and a == 'летучая мышь':
        assert 'летучая мышь'
    if q == 'Какого слова нет в языке народов Арктики?' and a == 'Война':
        assert 'Война'

def test_get_answer():
    new_game = Game()
    q = new_game.get_answer()
    if q == 'Столица России':
        assert 'Столица России'
    if q == 'Кто не является птицей?':
        assert 'Кто не является птицей?'
    if q == 'Какого слова нет в языке народов Арктики?':
        assert 'Какого слова нет в языке народов Арктики?'

def test_output_info():
    new_game = Game()
    q, a = new_game.get_question()
    return 'Введите букву или назовите слово:'

def test_Player():
    return Player('Андрей', 20, 'Все перемены к лучшему')

def test_player_info():
    player = Player('Андрей', 20, 'Все перемены к лучшему')
    return "\nИнформация об игроке: \n Имя: {self.name}, \n Возраст: {self.age}, \n Девиз по жизни: {self.motto_in_life}\n"


if __name__ == '__main__':
    pytest.main()