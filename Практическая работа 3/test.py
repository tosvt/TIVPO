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

if __name__ == '__main__':
    pytest.main()