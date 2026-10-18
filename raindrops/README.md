# Gotas de chuva

Bem-vindo ao Gotas de chuva na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.

## Introduction

Gotas de chuva é uma versão um pouco mais complexa do desafio FizzBuzz, uma questão clássica de entrevistas.

## Instructions

Sua tarefa é converter um número nos sons correspondentes de gotas de chuva.

Se um determinado número:

- for divisível por 3, adicione "Pling" ao resultado.
- for divisível por 5, adicione "Plang" ao resultado.
- for divisível por 7, adicione "Plong" ao resultado.
- **não for** divisível por 3, 5 nem 7, o resultado deve ser o número como uma string.

## Exemplos

- 28 é divisível por 7, mas não por 3 nem por 5, então o resultado seria `"Plong"`.
- 30 é divisível por 3 e por 5, mas não por 7, então o resultado seria `"PlingPlang"`.
- 34 não é divisível por 3, 5 nem 7, então o resultado seria `"34"`.

~~~~exercism/note
Uma forma comum de testar se um número é divisível por outro é comparar o [resto][remainder] ou o [módulo][modulo] com zero.
A maioria das linguagens oferece operadores ou funções para um deles (ou para os dois).

[remainder]: https://exercism.org/docs/programming/operators/remainder
[modulo]: https://en.wikipedia.org/wiki/Modulo_operation
~~~~

## Como este exercício é estruturado em Python

Este exercício é melhor resolvido com o operador `%` ([módulo][modulo]) do Python, que retorna o resto da divisão de números inteiros positivos.
Ele tem um equivalente em forma de método, `operator.mod()`, no [módulo operator][operator-mod].


O Python também oferece outros métodos de 'resto' no [módulo math][math-module].
[`math.fmod()`][fmod] se comporta como `%`, mas opera com números de ponto flutuante.
[`math.remainder()`][remainder] implementa um algoritmo de "passo mais próximo de zero" para o resto da divisão.
Embora a gente incentive você a se familiarizar com esses métodos, nenhum dos dois corresponde exatamente ao resultado de `%`, então não são recomendados para este exercício.

A função embutida [`divmod()`][divmod] também dá um resto que corresponde ao de `%` quando usada com dois números inteiros positivos, mas retorna uma `tuple` que precisa ser desempacotada.

[divmod]: https://docs.python.org/3/library/functions.html#divmod
[fmod]: https://docs.python.org/3/library/math.html#math.fmod
[math-module]: https://docs.python.org/3/library/math.html
[modulo]: https://www.programiz.com/python-programming/operators#arithmetic
[operator-mod]: https://docs.python.org/3/library/operator.html#operator.mod
[remainder]: https://docs.python.org/3/library/math.html#math.remainder

## Source

### Contributed to by

- @behrtam
- @BethanyG
- @bsoyka
- @cmccandless
- @Dog
- @ikhadykin
- @kytrinyx
- @lowks
- @N-Parsons
- @pheanex
- @sjakobi
- @tqa236
- @yawpitch

### Based on

A variation on FizzBuzz, a famous technical interview question that is intended to weed out potential candidates. That question is itself derived from Fizz Buzz, a popular children's game for teaching division. - https://en.wikipedia.org/wiki/Fizz_buzz