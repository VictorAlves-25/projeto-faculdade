from app import soma, subtracao, multiplicacao, divisao, saudacao

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(5, 2) == 3

def test_multiplicacao():
    assert multiplicacao(4, 3) == 12

def test_divisao():
    assert divisao(10, 2) == 5

def test_saudacao():
    assert saudacao("João") == "Olá, João!"
