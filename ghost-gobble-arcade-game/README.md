# O jogo de fliperama do fantasma comilão

Bem-vindo ao O jogo de fliperama do fantasma comilão na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.
Se você ficar travado no exercício, confira o `HINTS.md`, mas tente resolvê-lo sem usar essas dicas primeiro :)

## Introduction

Python representa valores verdadeiros e falsos com o tipo [`bool`][bools], que é uma subclasse de `int`.
Há apenas dois valores nesse tipo: `True` e `False`.
Esses valores podem ser atribuídos a uma variável:

```python
>>> true_variable = True
>>> false_variable = False
```

Podemos avaliar expressões Boolean usando os operadores `and`, `or` e `not`:

```python
>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True
```

[bools]: https://docs.python.org/3/library/stdtypes.html#typebool

## Instructions

Neste exercício, você precisa implementar algumas regras do [Pac-Man][Pac-Man], o clássico jogo de fliperama dos anos 1980.

Você tem quatro regras para implementar, todas relacionadas aos estados do jogo.

> _Não se preocupe em como os argumentos são derivados, apenas concentre-se em combinar os argumentos para retornar o resultado esperado._

## 1. Defina se o Pac-Man come um fantasma

Defina a função `eat_ghost()` que recebe dois parâmetros (_se o Pac-Man tem uma pastilha de poder ativa_ e _se o Pac-Man está tocando um fantasma_) e retorna um valor Boolean se o Pac-Man consegue comer um fantasma.
 A função deve retornar `True` apenas se o Pac-Man tiver uma pastilha de poder ativa e estiver tocando um fantasma.

```python
>>> eat_ghost(False, True)
...
False
```

## 2. Defina se o Pac-Man pontua

Defina a função `score()` que recebe dois parâmetros (_se o Pac-Man está tocando uma pastilha de poder_ e _se o Pac-Man está tocando um ponto_) e retorna um valor Boolean se o Pac-Man pontuou.
 A função deve retornar `True` se o Pac-Man estiver tocando uma pastilha de poder ou um ponto.

```python
>>> score(True, True)
...
True
```

## 3. Defina se o Pac-Man perde

Defina a função `lose()` que recebe dois parâmetros (_se o Pac-Man tem uma pastilha de poder ativa_ e _se o Pac-Man está tocando um fantasma_) e retorna um valor Boolean se o Pac-Man perde.
 A função deve retornar `True` se o Pac-Man estiver tocando um fantasma e não tiver uma pastilha de poder ativa.

```python
>>> lose(False, True)
...
True
```

## 4. Defina se o Pac-Man vence

Defina a função `win()` que recebe três parâmetros (_se o Pac-Man comeu todos os pontos_, _se o Pac-Man tem uma pastilha de poder ativa_, e _se o Pac-Man está tocando um fantasma_) e retorna um valor Boolean se o Pac-Man vence.
 A função deve retornar `True` se o Pac-Man comeu todos os pontos e não perdeu com base nas regras definidas na parte 3.

```python
>>> win(False, True, False)
...
False
```

[Pac-Man]: https://en.wikipedia.org/wiki/Pac-Man

## Source

### Created by

- @neenjaw

### Contributed to by

- @cmccandless
- @BethanyG