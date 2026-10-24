# Black Jack

Bem-vindo ao Black Jack na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.
Se você ficar travado no exercício, confira o `HINTS.md`, mas tente resolvê-lo sem usar essas dicas primeiro :)

## Introduction

## Comparações

O Python oferece os seguintes operadores de comparação básicos:

| Operador | Operação                   | Descrição                                                                 |
| -------- | -------------------------- | ------------------------------------------------------------------------- |
| `>`      | "maior que"                | `a > b` é `True` se `a` for **estritamente** maior em valor que `b`       |
| `<`      | "menor que"                | `a < b` é `True` se `a` for **estritamente** menor em valor que `b`       |
| `==`     | "igual a"                  | `a == b` é `True` se `a` for **estritamente** igual a `b` em valor        |
| `>=`     | "maior ou igual a"         | `a >= b` é `True` se `a > b` OU `a == b` em valor                         |
| `<=`     | "menor ou igual a"         | `a <= b` é `True` se `a < b` ou `a == b` em valor                         |
| `!=`     | "diferente de"             | `a != b` é `True` se `a == b` for `False`                                 |
| `is`     | "identidade"               | `a is b` é `True` se **_e somente se_** `a` e `b` forem o mesmo _objeto_  |
| `is not` | "identidade negada"        | `a is not b` é `True` se `a` e `b` **não** forem o mesmo _objeto_         |
| `in`     | "teste de contenção"       | `a in b` é `True` se `a` for membro, subconjunto ou elemento de `b`       |
| `not in` | "teste de contenção negado"| `a not in b` é `True` se `a` não for membro, subconjunto ou elemento de `b` |

Todos eles têm a mesma prioridade (_que é maior que a das [operações Boolean][boolean operations], mas menor que a das operações aritméticas ou bit a bit_).

## Comparação entre tipos de dados diferentes

Objetos de tipos diferentes (_exceto tipos numéricos_) nunca são considerados iguais por padrão.
Instâncias não idênticas de uma `class` também _**não**_ serão consideradas iguais, a menos que a `class` defina métodos especiais de [comparação avançada][rich comparisons] que personalizam o comportamento padrão de comparação de `object`.
A personalização por meio de `rich comparisons` será abordada em um exercício seguinte.
Para obter (muito) mais detalhes sobre esse tópico, consulte [Comparações de valores][value comparisons] na documentação do Python.

Os tipos numéricos são (em sua maioria) uma exceção a essa regra de correspondência de tipos.
Um `integer` **pode** ser considerado igual a um `float` (_ou um [`octal`][octal] igual a um [`hexadecimal`][hex]_), desde que os tipos possam ser convertidos implicitamente para a comparação.

Para os outros tipos numéricos da biblioteca padrão do Python ([complex][complex numbers], [decimal][decimal numbers], [fractions][rational numbers]), os operadores de comparação são definidos onde "fazem sentido" (_onde a conversão implícita não altera o resultado_), mas lançam um `TypeError` se os objetos subjacentes não puderem ser convertidos com precisão para a comparação.
Para mais informações sobre as regras que o Python usa para _conversão numérica_, consulte [conversões aritméticas][arithmetic conversions] na documentação do Python.

```python
>>> import fractions

# A string cannot be converted to an int.
>>> 17 == '17'
False

# An int can be converted to float for comparison.
>>> 17 == 17.0
True

# The fraction 6/3 can be converted to the int 2
# The int 2 can be converted to 0b10 in binary.
>>> 6/3 == 0b10
True

# An int can be converted to a complex number with a 0 imaginary part.
>>> 17 == complex(17)
True

# The fraction 2/5 can be converted to the float 0.4
>>> 0.4 == 2/5
True

>>> complex(2/5, 1/2) == complex(0.4, 0.5)
True
```

Qualquer comparação ordenada de um número com um tipo `NaN` (_não é um número_) é `False`.
Um efeito colateral confuso da definição de `NaN` do Python é que `NaN` nunca é igual a `NaN` na comparação.

```python
>>> x = float('NaN')

>>> 3 < x
False

>>> x < 3
False

# NaN never compares equal to NaN
>>> x == x
False
```

## Comparação de strings

Diferentemente dos números, as strings (`str`) são comparadas [_lexicograficamente_][lexographic order], usando seus pontos de código Unicode individuais (_o resultado de passar cada ponto de código da `str` para a função embutida [`ord()`][ord], que retorna um `int`_).
Se todos os pontos de código das duas strings coincidirem e estiverem _**na mesma ordem**_, as duas strings serão consideradas iguais.
Essa comparação é feita de forma "aos pares": primeiro com primeiro, segundo com segundo, e assim por diante.
No Python 3.x, `str` e `bytes` não podem ser convertidos/comparados diretamente.

```python
>>> 'Python' > 'Rust'
False

>>> 'Python' > 'JavaScript'
True

# Examples with Mandarin.
# hello < goodbye
>>> '你好' < '再见'
True

# ord() of first characters
>>> ord('你'), ord('再')
(20320, 20877)

# ord() of second characters
>>> ord('好'), ord('见')
(22909, 35265)

# And with Korean words.
# Pretty < beautiful.
>>> '예쁜' < '아름다운'
False

>>> ord('예'), ord('아')
(50696, 50500)
```

## Encadeamento de comparações

Os operadores de comparação podem ser encadeados _arbitrariamente_, ou seja, podem ser usados em qualquer combinação e com qualquer comprimento.
Observe que a avaliação de uma expressão acontece de `left` para `right`.

Como exemplo, `x < y <= z` é equivalente a `x < y` `and` `y <= z`, exceto que `y` é avaliado **apenas uma vez**.
Nos dois casos, `z` _não_ é avaliado **de forma alguma** quando `x < y` é considerado `False`.
Isso costuma ser chamado de `short-circuit evaluation`: a avaliação para se o valor de verdade da expressão já tiver sido determinado.

O `Short circuiting` é suportado por vários operadores Boolean, funções e também pelo encadeamento de comparações no Python.
Diferentemente de muitas outras linguagens de programação, incluindo `C`, `C++`, `C#` e `Java`, expressões encadeadas como `a < b < c` no Python têm uma [interpretação matemática][three way boolean comparison] convencional e precedência.

```python
>>> x = 2
>>> y = 5
>>> z = 10

>>> x < y < z
True

>>> x < y > z
False

>>> x > y < z
False
```

## Comparação de identidade de objetos

Os operadores `is` e `is not` testam a [_identidade_][object identity] do objeto, em oposição ao _valor_ do objeto.
A identidade de um objeto nunca muda após a criação e pode ser obtida com a função [`id()`][id function].

`<apple> is <orange>` resulta em `True` se _**e somente se**_ `id(<apple>)` == `id(<orange>)`.
`<apple> is not <orange>` produz o inverso.

Devido ao seu status de singleton, `None` e `NotImplemented` devem sempre ser comparados a itens usando `is` e `is not`.
Consulte a documentação de referência do Python sobre [comparações de valores][value comparisons none] e o [PEP8][pep8 programming recommendations] para mais detalhes sobre essa convenção.

```python
>>> my_fav_numbers = [1, 2, 3]

>>> your_fav_numbers = my_fav_numbers

>>> my_fav_numbers is your_fav_numbers
True

# The returned id will differ by system and python version.
>>> id(my_fav_numbers)
4517478208

# your_fav_numbers is only an alias pointing to the original my_fav_numbers object.
# Assigning a new name does not create a new object.
>>> id(your_fav_numbers)
4517478208


>>> my_fav_numbers is not your_fav_numbers
False

>>> my_fav_numbers is not None
True

>>> my_fav_numbers is NotImplemented
False
```

## Comparações de pertinência

Os operadores `in` e `not in` testam a _pertinência_.
`<fish> in <soup>` resulta em `True` se `<fish>` for um membro de `<soup>` (_se `<fish>` for um subconjunto de `<soup>` ou estiver contido nele_), e resulta em `False` caso contrário.
`<fish> not in <soup>` retorna a negação, ou o _oposto de_ `<fish> in <soup>`.

Para os tipos string e bytes, `<name> in <fullname>` é `True` _**se e somente se**_ `<name>` for uma substring de `<fullname>`.

```python
# A set of lucky numbers.
>>> lucky_numbers = {11, 22, 33}
>>> 22 in lucky_numbers
True

>>> 44 in lucky_numbers
False

# A dictionary of employee information.
>>> employee = {'name': 'John Doe', 
                'id': 67826, 'age': 33, 
                'title': 'ceo'}

# Checking for the membership of certain keys.
>>> 'age' in employee
True

>>> 33 in employee
False

>>> 'lastname' not in employee
True

# Checking for substring membership
>>> name = 'Super Batman'
>>> 'Bat' in name
True

>>> 'Batwoman' in name
False
```

[arithmetic conversions]: https://docs.python.org/3/reference/expressions.html?highlight=number%20conversion#arithmetic-conversions
[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[complex numbers]: https://docs.python.org/3/library/functions.html#complex
[decimal numbers]: https://docs.python.org/3/library/decimal.html
[hex]: https://docs.python.org/3/library/functions.html?highlight=hex#hex
[id function]: https://docs.python.org/3/library/functions.html#id
[lexographic order]: https://en.wikipedia.org/wiki/Lexicographic_order
[object identity]: https://docs.python.org/3/reference/datamodel.html
[octal]: https://docs.python.org/3/library/functions.html?#oct
[ord]: https://docs.python.org/3/library/functions.html#ord
[pep8 programming recommendations]: https://pep8.org/#programming-recommendations
[rational numbers]: https://docs.python.org/3/library/fractions.html
[rich comparisons]: https://docs.python.org/3/reference/datamodel.html#object.__lt__
[three way boolean comparison]: https://en.wikipedia.org/wiki/Three-way_comparison
[value comparisons none]: https://docs.python.org/3/reference/expressions.html?highlight=none#value-comparisons
[value comparisons]: https://docs.python.org/3/reference/expressions.html?highlight=nan#value-comparisons

## Instructions

Neste exercício, você vai implementar algumas regras do [Blackjack][blackjack], como a forma de jogar e pontuar.

**Observação**: neste exercício, _`A`_ significa ás, _`J`_ significa valete, _`Q`_ significa dama, e _`K`_ significa rei.
Os coringas são descartados.
Assume-se um [baralho padrão de 52 cartas com naipes franceses][standard_deck], mas na maioria das versões, vários baralhos são embaralhados juntos para o jogo.

## 1. Calcule o valor de uma carta

No Blackjack, fica a critério de cada jogador se um ás vale 1 ou 11 pontos (_mais sobre isso depois_).
As cartas figuras (`J`, `Q`, `K`) valem 10 pontos, e qualquer outra carta vale o seu valor "pip" (_numérico_).

Defina a função `value_of_card(<card>)` com o parâmetro `card`.
A função deve retornar o _valor numérico_ da string de carta recebida.
Como um ás pode assumir vários valores (1 **ou** 11), por enquanto essa função deve fixar o valor de uma carta ás em 1.
Mais adiante, você vai implementar uma função para determinar o valor de uma carta ás, dada uma mão existente.

```python
>>> value_of_card('K')
10

>>> value_of_card('4')
4

>>> value_of_card('A')
1
```

## 2. Determine qual carta tem o valor mais alto

Defina a função `higher_card(<card_one>, <card_two>)` com os parâmetros `card_one` e `card_two`.
Para fins de pontuação, o valor de `J`, `Q` ou `K` é 10.
A função deve retornar qual carta tem o valor mais alto para a pontuação.
Se as duas cartas tiverem o mesmo valor, retorne as duas.
Retornar as duas cartas pode ser feito usando uma vírgula na instrução `return`:

```python
# Using a comma in a return creates a Tuple.  Tuples will be covered in a later exercise.
>>> def returning_two_values(value_one, value_two):
        return value_one, value_two

>>> returning_two_values('K', '3')
('K', '3')
```

Um ás pode assumir vários valores, então vamos fixar as cartas `A` em um valor de 1 para esta tarefa.

```python
>>> higher_card('K', '10')
('K', '10')

>>> higher_card('4', '6')
'6'

>>> higher_card('K', 'A')
'K'
```

## 3. Calcule o valor de um ás

Como mencionado antes, um ás pode valer _tanto_ 1 **quanto** 11 pontos.
Os jogadores tentam chegar o mais perto possível de 21 pontos, sem _passar_ de 21 (_"estourar"_).

Defina a função `value_of_ace(<card_one>, <card_two>)` com os parâmetros `card_one` e `card_two`, que são um par de cartas já na mão _antes_ de receber uma carta ás.
Sua função terá que decidir se o próximo ás vai receber o valor 1 ou o valor 11, e retornar esse valor.
Lembre-se: o valor da mão com o ás precisa ser o mais alto possível _sem_ passar de 21.

**Dica**: se já tivermos um ás na mão, o valor do próximo ás seria 1.

```python
>>> value_of_ace('6', 'K')
1

>>> value_of_ace('7', '3')
11
```

## 4. Determine uma mão "natural" ou "blackjack"

Se um jogador receber um ás (`A`) e uma carta de dez (10, `K`, `Q` ou `J`) como suas duas primeiras cartas, ele terá uma pontuação de 21.
Isso é conhecido como uma mão de **blackjack**.


Defina a função `is_blackjack(<card_one>, <card_two>)` com os parâmetros `card_one` e `card_two`, que são um par de cartas.
Determine se a mão de duas cartas é um **blackjack**, e retorne o Boolean `True` se for, `False` caso contrário.

**Observação**: o _cálculo_ da pontuação pode ser feito de várias formas.
Mas, se possível, gostaríamos que você verificasse se há um ás e uma carta de dez **_na_** mão (_ou em uma certa posição_), em vez de _somar_ os valores da mão.

```python
>>> is_blackjack('A', 'K')
True

>>> is_blackjack('10', '9')
False
```

## 5. Dividir pares

Se as duas primeiras cartas de uma mão tiverem o mesmo valor (_por exemplo, dois seis ou um `Q` e um `K`_), um jogador pode escolher tratá-las como duas mãos separadas.
Isso é conhecido como "dividir pares".

Defina a função `can_split_pairs(<card_one>, <card_two>)` com os parâmetros `card_one` e `card_two`, que são um par de cartas.
Determine se essa mão de duas cartas pode ser dividida em dois pares.
Se a mão puder ser dividida, retorne o Boolean `True`; caso contrário, retorne `False`

```python
>>> can_split_pairs('Q', 'K')
True

>>> can_split_pairs('10', 'A')
False
```

## 6. Dobrar a aposta

Quando as duas cartas iniciais distribuídas somam 9, 10 ou 11 pontos, o jogador pode fazer uma aposta adicional igual à aposta original.
Isso é conhecido como "dobrar a aposta".

Defina a função `can_double_down(<card_one>, <card_two>)` com os parâmetros `card_one` e `card_two`, que são um par de cartas.
Determine se a mão de duas cartas pode ser "dobrada", e retorne o Boolean `True` se puder, `False` caso contrário.

```python
>>> can_double_down('A', '9')
True

>>> can_double_down('10', '2')
False
```

[blackjack]: https://bicyclecards.com/how-to-play/blackjack/
[standard_deck]: https://en.wikipedia.org/wiki/Standard_52-card_deck

## Source

### Created by

- @Ticktakto
- @Yabby1997
- @limm-jk
- @OMEGA-Y
- @wnstj2007
- @pranasziaukas
- @bethanyG

### Contributed to by

- @PaulT89