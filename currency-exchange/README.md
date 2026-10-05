# Câmbio de moedas

Bem-vindo ao Câmbio de moedas na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.
Se você ficar travado no exercício, confira o `HINTS.md`, mas tente resolvê-lo sem usar essas dicas primeiro :)

## Introduction

## Números

Existem três tipos diferentes de números embutidos no Python: `ints`, `floats` e `complex`. No entanto, neste exercício você vai lidar apenas com `ints` e `floats`.

### ints

`ints` são números inteiros. Por exemplo: `1234`, `-10`, `20201278`.

Os inteiros em Python têm [precisão arbitrária][arbitrary-precision]: o número de dígitos é limitado apenas pela memória disponível do sistema hospedeiro.

### floats

`floats` são números que contêm um ponto decimal. Por exemplo: `0.0`,`3.14`,`-9.01`.

Números de ponto flutuante geralmente são implementados em Python usando um `double` em C (_15 casas decimais de precisão_), mas a representação varia conforme o sistema hospedeiro e outros detalhes de implementação. Isso pode gerar algumas surpresas ao trabalhar com números de ponto flutuante, mas é "bom o suficiente" para a maioria das situações.

Você pode ver mais detalhes e discussões nos seguintes recursos:

- [Documentação dos tipos numéricos do Python][numeric-type-docs]
- [O Tutorial do Python][floating point math]
- [Documentação do `int()` embutido][`int()` built in]
- [Documentação do `float()` embutido][`float()` built in]
- [0.30000000000000004.com][0.30000000000000004.com]

## Aritmética

O Python dá suporte total à aritmética entre `ints` e `floats`. Ele converte números mais restritos para corresponder às suas contrapartes menos restritas quando usados com os operadores aritméticos binários (`+`, `-`, `*`, `/`, `//` e `%`).

O Python considera `ints` mais restritos que `floats`. Então, usar um número de ponto flutuante em uma expressão garante que o resultado também será um número de ponto flutuante. No entanto, ao fazer divisão, o resultado sempre será um número de ponto flutuante, mesmo que apenas números inteiros sejam usados.

```python
# The int is widened to a float here, and a float type is returned.
>>> 3 + 4.0
7.0
>>> 3 * 4.0
12.0
>>> 3 - 2.0
1.0
# Division always returns a float.
>>> 6 / 2
3.0
>>> 7 / 4
1.75
# Calculating remainders.
>>> 7 % 4
3
>>> 2 % 4
2
>>> 12.75 % 3
0.75
```

Se você precisar de um resultado inteiro, pode usar `//` para truncar o resultado.

```python
>>> 6 // 2
3
>>> 7 // 4
1
```

Para converter um número de ponto flutuante em um número inteiro, use `int()`. Para converter um número inteiro em um número de ponto flutuante, use `float()`.

```python
>>> int(6 / 2)
3
>>> float(1 + 2)
3.0
```

[0.30000000000000004.com]: https://0.30000000000000004.com/
[`float()` built in]: https://docs.python.org/3/library/functions.html#float
[`int()` built in]: https://docs.python.org/3/library/functions.html#int
[arbitrary-precision]: https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic#:~:text=In%20computer%20science%2C%20arbitrary%2Dprecision,memory%20of%20the%20host%20system.
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html
[numeric-type-docs]: https://docs.python.org/3/library/stdtypes.html#typesnumeric

## Instructions

Seu amigo Chandler planeja visitar países exóticos pelo mundo todo. Infelizmente, Chandler não é bom em matemática. Ele está bastante preocupado em ser enganado pelas casas de câmbio durante a viagem, e quer que você faça uma calculadora de câmbio para ele. Aqui estão as especificações dele para o aplicativo:

## 1. Estimar o valor após a troca

Crie a função `exchange_money()`, que recebe 2 parâmetros:

1. `budget` : a quantia de dinheiro que você planeja trocar.
2. `exchange_rate` : a quantia de moeda nacional equivalente a uma unidade de moeda estrangeira.

Essa função deve retornar o valor da moeda trocada.

**Nota:** Se a sua moeda for USD e você quiser trocar USD por EUR com uma taxa de câmbio de `1.20`, então `1.20 USD == 1 EUR`.

```python
>>> exchange_money(127.5, 1.2)
106.25
```

## 2. Calcular o valor restante após uma troca

Crie a função `get_change()`, que recebe 2 parâmetros:

1. `budget` : a quantia de dinheiro antes da troca.
2. `exchanging_value` : a quantia de dinheiro que é *retirada* do orçamento para ser trocada.

Essa função deve retornar a quantia de dinheiro que *sobra* do orçamento.

```python
>>> get_change(127.5, 120)
7.5
```

## 3. Calcular o valor das cédulas

Crie a função `get_value_of_bills()`, que recebe 2 parâmetros:

1. `denomination` : o valor de uma única cédula.
2. `number_of_bills` : o número total de cédulas.

Essa casa de câmbio só trabalha com dinheiro em determinados incrementos.
O total que você recebe precisa ser divisível pelo valor de uma "cédula" ou unidade, o que pode deixar uma fração ou um resto.
Sua função deve retornar apenas o valor total das cédulas (_excluindo valores fracionados_) que a casa de câmbio devolveria.
Infelizmente, a casa de câmbio fica com o resto/troco como bônus extra.

```python
>>> get_value_of_bills(5, 128)
640
```

## 4. Calcular o número de cédulas

Crie a função `get_number_of_bills()`, que recebe `amount` e `denomination`.

Essa função deve retornar o _número de cédulas_ que você pode receber dentro do _amount_ informado.
Em outras palavras: quantas _cédulas inteiras_ cabem no valor inicial?
Lembre-se: você só pode receber _cédulas inteiras_, não frações de cédulas, então não se esqueça de dividir de acordo.
Na prática, você está arredondando _para baixo_ até a cédula/denominação inteira mais próxima.

```python
>>> get_number_of_bills(127.5, 5)
25
```

## 5. Calcular o que sobra após trocar por cédulas

Crie a função `get_leftover_of_bills()`, que recebe `amount` e `denomination`.

Essa função deve retornar a _quantia restante_ que não pode ser devolvida a partir do _amount_ inicial, dada a denominação das cédulas.
É muito importante saber exatamente quanto a casa de câmbio fica.

```python
>>> get_leftover_of_bills(127.5, 20)
7.5
```

## 6. Calcular o valor após a troca

Crie a função `exchangeable_value()`, que recebe `budget`, `exchange_rate`, `spread` e `denomination`.

O parâmetro `spread` é a *porcentagem cobrada* como taxa de câmbio, escrita como um número inteiro.
É preciso convertê-la para decimal dividindo-a por 100.
Se `1.00 EUR == 1.20 USD` e o *spread* for `10`, a taxa de câmbio real será: `1.00 EUR == 1.32 USD`, porque 10% de 1.20 é 0.12, e essa taxa adicional é somada à troca.

Essa função deve retornar o valor máximo da nova moeda depois de calcular a *taxa de câmbio* mais o *spread*.
Lembre-se de que a *denominação* da moeda é um número inteiro e não pode ser subdividida.

**Nota:** O valor retornado deve ser do tipo `int`.

```python
>>> exchangeable_value(127.25, 1.20, 10, 20)
80
>>> exchangeable_value(127.25, 1.20, 10, 5)
95
```

## Source

### Created by

- @Ticktakto
- @Yabby1997
- @limm-jk
- @OMEGA-Y
- @wnstj2007
- @J08K

### Contributed to by

- @BethanyG
- @kytrinyx
- @pranasziaukas