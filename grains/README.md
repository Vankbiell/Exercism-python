# Grãos

Bem-vindo ao Grãos na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.

## Introduction

Era uma vez um servo sábio que salvou a vida de um príncipe.
O rei prometeu pagar o que o servo fosse capaz de imaginar.
Sabendo que o rei adorava xadrez, o servo disse ao rei que gostaria de receber grãos de trigo.
Um grão na primeira casa de um tabuleiro de xadrez, com o número de grãos dobrando a cada casa seguinte.

## Instructions

Calcule o número de grãos de trigo em um tabuleiro de xadrez.

Um tabuleiro de xadrez tem 64 casas.
A casa 1 tem um grão, a casa 2 tem dois grãos, a casa 3 tem quatro grãos, e assim por diante, dobrando a cada vez.

Escreva um código que calcule:

- o número de grãos em uma determinada casa
- o número total de grãos no tabuleiro de xadrez

## Mensagens de exceção

Às vezes é preciso [levantar uma exceção](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). Quando você fizer isso, deve sempre incluir uma **mensagem de erro significativa** para indicar qual é a origem do erro. Isso deixa seu código mais legível e ajuda bastante na depuração. Em situações em que você sabe que a origem do erro será de um tipo específico, você pode optar por levantar um dos [tipos de erro embutidos](https://docs.python.org/3/library/exceptions.html#base-classes), mas ainda assim deve incluir uma mensagem significativa.

Este exercício específico pede que você use a [instrução raise](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) para "lançar" um `ValueError` quando a entrada do quadrado estiver fora do intervalo. Os testes só vão passar se você `raise` a `exception` e incluir uma mensagem junto com ela.

Para levantar um `ValueError` com uma mensagem, escreva a mensagem como argumento para o tipo `exception`:

```python
# when the square value is not in the acceptable range        
raise ValueError("square must be between 1 and 64")
```

## Source

### Contributed to by

- @behrtam
- @BethanyG
- @cmccandless
- @denislooby
- @Dog
- @kytrinyx
- @lowks
- @MojitoMonday
- @N-Parsons
- @pheanex
- @sdublish
- @sjakobi
- @smalley
- @tqa236
- @yawpitch

### Based on

The CodeRanch Cattle Drive, Assignment 6 - https://web.archive.org/web/20240908084142/https://coderanch.com/wiki/718824/Grains