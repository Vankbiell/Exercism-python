# O vocabulário da irmãzinha

Bem-vindo ao O vocabulário da irmãzinha na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.
Se você ficar travado no exercício, confira o `HINTS.md`, mas tente resolvê-lo sem usar essas dicas primeiro :)

## Introduction

Uma `str` em Python é uma [sequência imutável][text sequence] de [pontos de código Unicode][unicode code points].
Isso pode incluir letras, sinais diacríticos, caracteres de posicionamento, números, símbolos de moeda, emoji, pontuação, espaços e caracteres de quebra de linha, entre outros.
Por ser imutável, o valor de um objeto `str` na memória não muda; métodos que parecem modificar uma string retornam uma nova cópia ou instância desse objeto `str`.


Um literal `str` pode ser declarado com aspas simples `'` ou duplas `"`. O caractere de escape `\` está disponível quando necessário.


```python

>>> single_quoted = 'These allow "double quoting" without "escape" characters.'

>>> double_quoted = "These allow embedded 'single quoting', so you don't have to use an 'escape' character."

>>> escapes = 'If needed, a \'slash\' can be used as an escape character within a string when switching quote styles won\'t work.'
```

Strings de várias linhas são declaradas com `'''` ou `"""`.


```python
>>> triple_quoted =  '''Three single quotes or "double quotes" in a row allow for multi-line string literals.
  Line break characters, tabs and other whitespace are fully supported.

  You\'ll most often encounter these as "doc strings" or "doc tests" written just below the first line of a function or class definition.
    They\'re often used with auto documentation ✍ tools.
    '''
```

Strings podem ser concatenadas usando o operador `+`.
 Esse método deve ser usado com moderação, pois não é muito performático nem fácil de manter.


```python
language = "Ukrainian"
number = "nine"
word = "дев'ять"

sentence = word + " " + "means" + " " + number + " in " + language + "."

>>> print(sentence)
...
"дев'ять means nine in Ukrainian."
```

Se uma `list`, `tuple`, `set` ou outra coleção de strings individuais precisar ser combinada em uma única `str`, [`<str>.join(<iterable>)`][str-join] é uma opção melhor:


```python
# str.join() makes a new string from the iterables elements.
>>> chickens = ["hen", "egg", "rooster"] # Lists are iterable.
>>> ' '.join(chickens)
'hen egg rooster'

# Any string can be used as the joining element.
>>> ' :: '.join(chickens)
'hen :: egg :: rooster'

>>> ' 🌿 '.join(chickens)
'hen 🌿 egg 🌿 rooster'


# Any iterable can be used as input.
>>> flowers = ("rose", "daisy", "carnation")  # Tuples are iterable.
>>> '*-*'.join(flowers)
'rose*-*daisy*-*carnation'

>>> flowers = {"rose", "daisy", "carnation"}  # Sets are iterable, but output order is not guaranteed.
>>> '*-*'.join(flowers)
'rose*-*carnation*-*daisy'

>>> phrase = "This is my string"  # Strings are iterable, but be careful!
>>> '..'.join(phrase)
'T..h..i..s.. ..i..s.. ..m..y.. ..s..t..r..i..n..g'


# Separators are inserted **between** elements, but can be any string (including spaces).
# This can be exploited for interesting effects.
>>> under_words = ['under', 'current', 'sea', 'pin', 'dog', 'lay']
>>> separator = ' ⤴️ under'
>>> separator.join(under_words)
'under ⤴️ undercurrent ⤴️ undersea ⤴️ underpin ⤴️ underdog ⤴️ underlay'

# The separator can be composed different ways, as long as the result is a string.
>>> upper_words = ['upper', 'crust', 'case', 'classmen', 'most', 'cut']
>>> separator = ' 🌟 ' + upper_words[0]
>>> separator.join(upper_words)
 'upper 🌟 uppercrust 🌟 uppercase 🌟 upperclassmen 🌟 uppermost 🌟 uppercut'
```

Os pontos de código dentro de uma `str` podem ser referenciados por um número de índice `0-based index` a partir da esquerda:


```python
creative = '창의적인'

>>> creative[0]
'창'

>>> creative[2]
'적'

>>> creative[3]
'인'
```

A indexação também funciona a partir da direita, começando com um `-1-based index`:


```python
creative = '창의적인'

>>> creative[-4]
'창'

>>> creative[-2]
'적'

>>> creative[-1]
'인'

```

Não existe um tipo separado de “caractere” ou "rune" em Python, então indexar uma string produz uma nova `str` de comprimento 1:


```python

>>> website = "exercism"
>>> type(website[0])
<class 'str'>

>>> len(website[0])
1

>>> website[0] == website[0:1] == 'e'
True
```

Substrings podem ser selecionadas por meio de _notação de slice_, usando [`<str>[<start>:stop:<step>]`][common sequence operations] para produzir uma nova string.
 Os resultados excluem o índice `stop`.
 Se nenhum `start` for informado, o índice inicial será 0.
 Se nenhum `stop` for informado, o índice `stop` será o fim da string.


```python
moon_and_stars = '🌟🌟🌙🌟🌟⭐'
sun_and_moon = '🌞🌙🌞🌙🌞🌙🌞🌙🌞'

>>> moon_and_stars[1:4]
'🌟🌙🌟'

>>> moon_and_stars[:3]
'🌟🌟🌙'

>>> moon_and_stars[3:]
'🌟🌟⭐'

>>> moon_and_stars[:-1]
'🌟🌟🌙🌟🌟'

>>> moon_and_stars[:-3]
'🌟🌟🌙'

>>> sun_and_moon[::2]
'🌞🌞🌞🌞🌞'

>>> sun_and_moon[:-2:2]
'🌞🌞🌞🌞'

>>> sun_and_moon[1:-1:2]
'🌙🌙🌙🌙'
```

Strings também podem ser divididas em strings menores por meio de [`<str>.split(<separator>)`][str-split], que retornará uma `list` de substrings.
 A lista pode então ser indexada ou dividida ainda mais, se necessário.
 Usar `<str>.split()` sem nenhum argumento dividirá a string nos espaços em branco.


```python
>>> cat_ipsum = "Destroy house in 5 seconds mock the hooman."
>>> cat_ipsum.split()
...
['Destroy', 'house', 'in', '5', 'seconds', 'mock', 'the', 'hooman.']


>>> cat_ipsum.split()[-1]
'hooman.'


>>> cat_words = "feline, four-footed, ferocious, furry"
>>> cat_words.split(', ')
...
['feline', 'four-footed', 'ferocious', 'furry']
```

Os separadores de `<str>.split()` podem ter mais de um caractere.
A **string inteira** é usada na correspondência da divisão.


```python

>>> colors = """red,
orange,
green,
purple,
yellow"""

>>> colors.split(',\n')
['red', 'orange', 'green', 'purple', 'yellow']
```

Strings suportam todas as [operações comuns de sequência][common sequence operations].
 Pontos de código individuais podem ser iterados em um laço com `for item in <str>`.
 Índices _com_ itens podem ser iterados em um laço com `for index, item in enumerate(<str>)`.


```python

>>> exercise = 'လေ့ကျင့်'

# Note that there are more code points than perceived glyphs or characters
>>> for code_point in exercise:
...    print(code_point)
...
လ
ေ
့
က
ျ
င
်
့

# Using enumerate will give both the value and index position of each element.
>>> for index, code_point in enumerate(exercise):
...    print(index, ": ", code_point)
...
0 :  လ
1 :  ေ
2 :  ့
3 :  က
4 :  ျ
5 :  င
6 :  ်
7 :  ့
```


[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-split]: https://docs.python.org/3/library/stdtypes.html#str.split
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme

## Instructions

Você está ajudando sua irmã mais nova com a lição de casa de vocabulário de inglês dela, que ela está achando muito maçante. A turma dela está aprendendo a criar novas palavras adicionando _prefixos_ e _sufixos_. Dada uma lista de palavras, o objetivo é formar palavras transformadas corretamente, com a ortografia certa, adicionando o prefixo no início ou o sufixo no fim.

A tarefa tem quatro atividades, cada uma com um conjunto de textos ou palavras para trabalhar.

## 1. Adicionar um prefixo a uma palavra

Um dos prefixos mais comuns em inglês é o `un`, que significa "não". Nesta atividade, sua irmã precisa formar palavras negativas, ou palavras com sentido de "não", adicionando `un` a elas.

Implemente a função `add_prefix_un(<word>)`, que recebe `word` como parâmetro e retorna uma nova palavra com o prefixo `un`:

```python
>>> add_prefix_un("happy")
'unhappy'

>>> add_prefix_un("manageable")
'unmanageable'
```

## 2. Adicionar prefixos a grupos de palavras

Há mais quatro prefixos comuns que a turma da sua irmã está estudando: `en` (_com o sentido de 'colocar dentro' ou 'cobrir com'_), `pre` (_com o sentido de 'antes' ou 'adiante'_), `auto` (_com o sentido de 'próprio' ou 'mesmo'_) e `inter` (_com o sentido de 'entre' ou 'no meio de'_).

Neste exercício, a turma está criando grupos de palavras de vocabulário usando esses prefixos, para que possam ser estudadas em conjunto. Cada prefixo vem em uma lista com palavras comuns com as quais ele é usado. Os estudantes precisam aplicar o prefixo e produzir uma string que mostre o prefixo aplicado a todas as palavras.

Implemente a função `make_word_groups(<vocab_words>)`, que recebe `vocab_words` como parâmetro no seguinte formato: `[<prefix>, <word_1>, <word_2> .... <word_n>]`, e retorna uma string com o prefixo aplicado a cada palavra, no formato: `'<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'`.

Não é preciso criar um laço `for` ou `while` para processar a entrada aqui. Pense com cuidado sobre quais métodos de string (e delimitadores) você poderia usar em vez disso.

```python
>>> make_word_groups(['en', 'close', 'joy', 'lighten'])
'en :: enclose :: enjoy :: enlighten'

>>> make_word_groups(['pre', 'serve', 'dispose', 'position'])
'pre :: preserve :: predispose :: preposition'

>> make_word_groups(['auto', 'didactic', 'graph', 'mate'])
'auto :: autodidactic :: autograph :: automate'

>>> make_word_groups(['inter', 'twine', 'connected', 'dependent'])
'inter :: intertwine :: interconnected :: interdependent'
```

## 3. Remover um sufixo de uma palavra

`ness` é um sufixo comum que significa _'estado de ser'_. Nesta atividade, sua irmã precisa encontrar a palavra raiz original removendo o sufixo `ness`. Mas é claro que existem aquelas regras de ortografia chatas: se a palavra raiz originalmente terminava em uma consoante seguida de um 'y', então o 'y' foi trocado por 'i'. Remover o 'ness' precisa restaurar o 'y' nessas palavras raiz. Por exemplo, `happiness` --> `happi` --> `happy`.

Implemente a função `remove_suffix_ness(<word>)`, que recebe uma `word` e retorna a palavra raiz sem o sufixo `ness`.

```python
>>> remove_suffix_ness("heaviness")
'heavy'

>>> remove_suffix_ness("sadness")
'sad'
```

## 4. Extrair e transformar uma palavra

Sufixos costumam ser usados para mudar a classe gramatical à qual uma palavra pertence. Uma prática comum em inglês é o "verbing" ou "verbifying", em que um adjetivo _se torna_ um verbo ao adicionar um sufixo `en`.

Nesta tarefa, sua irmã vai praticar o "verbing" de palavras, extraindo um adjetivo de uma frase e transformando-o em um verbo. Felizmente, todas as palavras que precisam ser transformadas aqui são "regulares": elas não precisam de mudanças na ortografia para adicionar o sufixo.

Implemente a função `adjective_to_verb(<sentence>, <index>)`, que recebe dois parâmetros: uma `sentence` que usa a palavra de vocabulário e o `index` da palavra, depois que essa frase é separada. A função deve retornar o adjetivo extraído como verbo.

```python
>>> adjective_to_verb('I need to make that bright.', -1 )
'brighten'

>>> adjective_to_verb('It got dark as the sun set.', 2)
'darken'
```

## Source

### Created by

- @aldraco
- @BethanyG