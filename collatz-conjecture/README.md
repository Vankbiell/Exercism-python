# Conjectura de Collatz

Bem-vindo ao Conjectura de Collatz na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.

## Introduction

Certa noite, você encontrou um caderno antigo cheio de rabiscos enigmáticos, como se alguém estivesse perseguindo uma ideia de forma obsessiva.
Em uma das páginas, uma única pergunta se destacava: **Todo número consegue encontrar o caminho até 1?**
Ela estava ligada a algo chamado **Conjectura de Collatz**, um enigma que confunde pensadores há décadas.

As regras eram enganosamente simples.
Escolha qualquer número inteiro positivo.

- Se for par, divida por 2.
- Se for ímpar, multiplique por 3 e some 1.

Depois, repita esses passos com o resultado, continuando indefinidamente.

A curiosidade venceu: você escolheu o número 12 para testar e começou a jornada:

12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1

Contando a partir do segundo número (6), foram 9 passos até chegar a 1, e a cada vez que as regras se repetiam, o número continuava mudando.
No início, a sequência parecia imprevisível: subia, descia e pulava de um lado para o outro.
Ainda assim, a conjectura afirma que, não importa o número inicial, sempre vamos terminar em 1.

Era fascinante, mas também intrigante.
Por que isso parece sempre funcionar?
Será que existe um número em que o processo se quebra, repetindo para sempre ou escapando para o infinito?
O caderno sugeria que resolver isso poderia revelar algo profundo. E, com isso, fama, [fortuna][collatz-prize] e um lugar na história esperam por quem conseguisse desvendar seus segredos.

[collatz-prize]: https://mathprize.net/posts/collatz-conjecture/

## Instructions

Dado um número inteiro positivo, retorne o número de passos necessários para chegar a 1 de acordo com as regras da Conjectura de Collatz.

## Mensagens de exceção

Às vezes é necessário [lançar uma exceção](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). Quando você faz isso, deve sempre incluir uma **mensagem de erro significativa** para indicar qual é a origem do erro. Isso deixa seu código mais legível e ajuda bastante no debug. Em situações em que você sabe que a origem do erro será de um tipo específico, você pode escolher lançar um dos [tipos de erro internos](https://docs.python.org/3/library/exceptions.html#base-classes), mas ainda deve incluir uma mensagem significativa.

A Conjectura de Collatz lida apenas com **números inteiros estritamente positivos**, então este exercício espera que você use a [instrução raise](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) e "lance" um `ValueError` na sua solução se o valor dado for zero ou um número inteiro negativo. Os testes só vão passar se você fizer `raise` da `exception` e incluir uma mensagem junto.

Para lançar um `ValueError` com uma mensagem, escreva a mensagem como argumento do tipo `exception`:

```python
# example when argument is zero or a negative integer
raise ValueError("Only positive integers are allowed")
```

## Source

### Created by

- @zwaltman

### Contributed to by

- @BethanyG
- @cmccandless
- @Dog
- @ikhadykin
- @K4cePhoenix
- @N-Parsons
- @smt923
- @Stigjb
- @thomasjpfan
- @tqa236

### Based on

Wikipedia - https://en.wikipedia.org/wiki/Collatz_conjecture