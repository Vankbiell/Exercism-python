# Help

## Rodando os testes

Usamos o [pytest][pytest: Getting Started Guide] como o executor de testes do nosso site.
Você vai precisar instalar o `pytest` na sua máquina de desenvolvimento se quiser rodar os testes da trilha de Python localmente.
Você também deve instalar os seguintes plugins do `pytest`:

- [pytest-cache][pytest-cache]
- [pytest-subtests][pytest-subtests]

Você encontra mais informações no nosso [guia de testes do Python][Python track tests page].


### Rodando os testes

Para rodar os testes incluídos, navegue até a pasta onde o exercício está armazenado usando `cd` no seu terminal (_substitua `<exercise-folder-location>` abaixo pelo seu caminho_).
Os arquivos de teste geralmente terminam em `_test.py` e são os mesmos testes que rodam no site quando uma solução é enviada.

Linux/MacOS
```bash
$ cd <path/to/exercise-folder-location>
```

Windows
```powershell
PS C:\Users\foobar> cd <path\to\exercise-folder-location>
```

<br>

Em seguida, rode o comando `pytest` no seu terminal, substituindo `<exercise_test.py>` pelo nome do arquivo de teste:

Linux/MacOS
```bash
$ python3 -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```

Windows
```powershell
PS C:\Users\foobar> py -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```


### Opções comuns
- `-o` : sobrescreve o `pytest.ini` padrão (_você pode usar isso para evitar avisos de marcadores_)
- `-v` : habilita a saída detalhada.
- `-x` : para de rodar os testes na primeira falha.
- `--ff` : roda as falhas do teste anterior antes dos outros casos de teste.

Para outras opções, use `python3 -m pytest -h` ou `py -m pytest -h`.


### Corrigindo avisos

Se você não usar `pytest -o markers=task` ao invocar o `pytest`, pode receber um `PytestUnknownMarkWarning` para testes que usam nossa nova sintaxe:

```bash
PytestUnknownMarkWarning: Unknown pytest.mark.task - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
```

Para evitar digitar `pytest -o markers=task` a cada teste que rodar, você pode usar um arquivo de configuração `pytest.ini`.
Criamos um que pode ser baixado do nível superior do diretório da trilha de Python: [pytest.ini][pytest.ini].

Você também pode criar seu próprio arquivo `pytest.ini` com o seguinte conteúdo:

```ini
[pytest]
markers =
    task: A concept exercise task.
```

Colocar o arquivo `pytest.ini` no diretório _raiz_ ou _de trabalho_ dos exercícios da sua trilha de Python vai registrar os marcadores e acabar com os avisos.
Você encontra mais informações sobre os marcadores do pytest na documentação do `pytest` sobre [marcar funções de teste][pytest: marking test functions with attributes] e na documentação do `pytest` sobre [trabalhar com marcadores personalizados][pytest: working with custom markers].

Você encontra informações sobre como personalizar configurações do pytest na documentação do `pytest` sobre [formatos de arquivo de configuração][pytest: configuration file formats].


### Estendendo sua IDE ou editor de código

Muitas IDEs e editores de código já têm suporte integrado para usar o `pytest` e outras ferramentas de qualidade de código.
Você encontra algumas opções feitas pela comunidade na nossa [página de ferramentas da trilha de Python][Python track tools page].

[Pytest: Getting Started Guide]: https://docs.pytest.org/en/latest/getting-started.html
[Python track tools page]: https://exercism.org/docs/tracks/python/tools
[Python track tests page]: https://exercism.org/docs/tracks/python/tests
[pytest-cache]:http://pythonhosted.org/pytest-cache/
[pytest-subtests]:https://github.com/pytest-dev/pytest-subtests
[pytest.ini]: https://github.com/exercism/python/blob/main/pytest.ini
[pytest: configuration file formats]: https://docs.pytest.org/en/6.2.x/customize.html#configuration-file-formats
[pytest: marking test functions with attributes]: https://docs.pytest.org/en/6.2.x/mark.html#raising-errors-on-unknown-marks
[pytest: working with custom markers]: https://docs.pytest.org/en/6.2.x/example/markers.html#working-with-custom-markers

## Enviando sua solução

Você pode enviar sua solução usando o comando `exercism submit conditionals.py`.
Esse comando vai enviar sua solução para o site do Exercism e imprimir a URL da página da solução.

É possível enviar uma solução incompleta, o que permite que você:

- Veja como outras pessoas resolveram o exercício
- Peça ajuda a um mentor

## Precisa de ajuda?

Se você quiser ajuda para resolver o exercício, confira as seguintes páginas:

- A [documentação da trilha Python](https://exercism.org/docs/tracks/python)
- A [categoria de programação da trilha Python no fórum](https://forum.exercism.org/c/programming/python)
- A [categoria de programação do Exercism no fórum](https://forum.exercism.org/c/programming/5)
- As [Perguntas frequentes](https://exercism.org/docs/using/faqs)

Caso esses recursos não sejam suficientes, você pode enviar sua solução (incompleta) para pedir mentoria.

Abaixo estão alguns recursos para conseguir ajuda caso você tenha problemas:

- [A PSF](https://www.python.org) hospeda os downloads do Python, a documentação e os recursos da comunidade.
- [Os fóruns da comunidade Python](https://discuss.python.org/) trazem ajuda, discussões sobre PEPs, os committers do núcleo do Python e muito mais.
- [A comunidade do Exercism no Discord](https://exercism.org/r/discord)
- [Os fóruns de discussão da comunidade do Exercism](https://forum.exercsim.org)
- [A comunidade Python no Discord](https://pythondiscord.com/) é uma comunidade muito prestativa e ativa.
- [/r/learnpython/](https://www.reddit.com/r/learnpython/) é um subreddit feito para quem está aprendendo Python.
- [#python no Libera.chat](https://www.python.org/community/irc/) é onde os desenvolvedores do núcleo da linguagem se reúnem e fazem o trabalho acontecer.
- [Os fóruns da comunidade Free Code Camp](https://forum.freecodecamp.org/)
- [Pythontutor](http://pythontutor.com/) para acompanhar pequenos trechos de código visualmente, passo a passo.

Além disso, o [StackOverflow](http://stackoverflow.com/questions/tagged/python) é um bom lugar para pesquisar seu problema ou sua dúvida e ver se já foi respondido. Se não foi, você sempre pode [perguntar](https://stackoverflow.com/help/how-to-ask) ou [responder](https://stackoverflow.com/help/how-to-answer) à pergunta de outra pessoa.