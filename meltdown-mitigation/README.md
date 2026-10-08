# Mitigação do colapso

Bem-vindo ao Mitigação do colapso na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.
Se você ficar travado no exercício, confira o `HINTS.md`, mas tente resolvê-lo sem usar essas dicas primeiro :)

## Introduction

Em Python, as instruções [`if`][if statement], `elif` (_uma contração de 'else' e 'if'_) e `else` são usadas para [controlar o fluxo][control flow tools] de execução e tomar decisões em um programa.
Diferente de muitas outras linguagens de programação, o Python nas versões 3.9 e anteriores não oferece uma instrução formal de case-switch; em vez disso, usa várias instruções `elif` para cumprir um papel parecido.

O Python 3.10 introduz uma variante da instrução case-switch chamada `structural pattern matching`, que será abordada separadamente em outro conceito.

As instruções condicionais usam expressões que precisam resultar em `True` ou `False`, seja retornando um tipo `bool` diretamente, seja sendo avaliadas como ["truthy" ou "falsy"][truth value testing].

```python
x = 10
y = 5

# The comparison '>' returns the bool 'True',
# so the statement is printed.
if x > y:
    print("x is greater than y")
...
>>> x is greater than y
```

Quando combinado com um `if`, um bloco de código `else` opcional é executado quando a condição original do `if` resulta em `False`:

```python
x = 5
y = 10

# The comparison '>' here returns the bool 'False',
# so the 'else' block is executed instead of the 'if' block.
if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")
...
>>> y is greater than x
```

O `elif` permite múltiplas avaliações/blocos.

```python
x = 5
y = 10
z = 20

# The 'elif' statement allows for the checking of more conditions.
if x > y:
    print("x is greater than y and z")
elif y > z:
    print("y is greater than x and z")
else:
    print("z is greater than x and y")
...
>>> z is greater than x and y
```

[Operações Boolean][boolean operations] e [comparações][comparisons] podem ser combinadas com condicionais para testes mais complexos:

```python
>>> def classic_fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            say = 'FizzBuzz!'
        elif number % 5 == 0:
            say = 'Buzz!'
        elif number % 3 == 0:
            say = 'Fizz!'
        else:
            say = str(number)
        
        return say

>>> classic_fizzbuzz(15)
'FizzBuzz!'

>>> classic_fizzbuzz(13)
'13'
```

[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
[if statement]: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
[truth value testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

## Instructions

Neste exercício, vamos desenvolver um sistema de controle simples para um reator nuclear.

Para produzir energia, um reator precisa estar em um estado de _criticalidade_.
Se o reator estiver em um estado abaixo da criticalidade, ele pode ser danificado.
Se o estado do reator ultrapassar a criticalidade, ele pode sobrecarregar e sofrer um derretimento.
Queremos reduzir as chances de derretimento e gerenciar corretamente o estado do reator.

As três tarefas a seguir estão todas relacionadas a escrever código para manter o estado ideal do reator.

## 1. Verifique a criticalidade

A primeira coisa que um sistema de controle precisa fazer é verificar se o reator está _equilibrado em criticalidade_.
Dizemos que um reator está equilibrado em criticalidade se ele atender às seguintes condições:

- A temperatura é menor que 800 K.
- O número de nêutrons emitidos por segundo é maior que 500.
- O produto da temperatura e dos nêutrons emitidos por segundo é menor que 500000.

Implemente a função `is_criticality_balanced()` que recebe `temperature`, medida em kelvin, e `neutrons_emitted` como parâmetros, e retorna `True` se as condições de criticalidade forem atendidas, `False` se não forem.

```python
>>> is_criticality_balanced(750, 600)
True
```

## 2. Determine a faixa de potência de saída

Depois que o reator começa a produzir energia, é preciso determinar sua eficiência.
A eficiência pode ser agrupada em 4 faixas:

1. `green` -> eficiência de 80% ou mais,
2. `orange` -> eficiência menor que 80%, mas de pelo menos 60%,
3. `red` -> eficiência abaixo de 60%, mas ainda 30% ou mais,
4. `black` ->  menos de 30% de eficiência.

O valor percentual pode ser calculado como `(generated_power/theoretical_max_power)*100`, em que `generated_power` = `voltage` * `current`.
Repare que o valor percentual geralmente não é um número inteiro, então certifique-se de usar corretamente as comparações `<` e `<=`.

Implemente a função `reactor_efficiency(<voltage>, <current>, <theoretical_max_power>)`, com três parâmetros: `voltage`, `current` e `theoretical_max_power`.
Essa função deve retornar a faixa de eficiência do reator: 'green', 'orange', 'red' ou 'black'.

```python
>>> reactor_efficiency(200,50,15000)
'orange'
```

## 3. Mecanismo à prova de falhas

Sua tarefa final é criar um mecanismo à prova de falhas para evitar sobrecarga e derretimento.
Esse mecanismo vai determinar se o reator está abaixo, no nível, ou acima do limite ideal de criticalidade.
A criticalidade pode então ser aumentada, diminuída ou interrompida inserindo (ou removendo) barras de controle no reator.

Implemente a função chamada `fail_safe()`, que recebe 3 parâmetros: `temperature`, medida em kelvin, `neutrons_produced_per_second` e `threshold`, e retorna um código de status para o reator.

- Se `temperature * neutrons_produced_per_second` < 90% de `threshold`, retorne o código de status 'LOW', indicando que as barras de controle precisam ser removidas para produzir energia.

- Se o valor `temperature * neutrons_produced_per_second` estiver dentro de 10% do `threshold` (ou seja, de 0 a 10% abaixo do limite, exatamente no limite, ou de 0 a 10% acima do limite), o reator está em _criticalidade_ e o código de status 'NORMAL' deve ser retornado, indicando que o reator está em condição ideal e que as barras de controle estão em posição ideal.

- Se `temperature * neutrons_produced_per_second` não estiver nas faixas mencionadas acima, o reator vai sofrer um derretimento e o código de status 'DANGER' deve ser retornado para desligar o reator imediatamente.

```python
>>> fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
'DANGER'
```

## Source

### Created by

- @sachsom95
- @BethanyG

### Contributed to by

- @kbuc