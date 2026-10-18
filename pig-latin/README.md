# Pig Latin

Bem-vindo ao Pig Latin na trilha Python do Exercism.
Se você precisar de ajuda para rodar os testes ou enviar seu código, confira o `HELP.md`.

## Introduction

Seus pais desafiaram você e seus irmãos para uma partida de basquete dois contra dois.
Confiante de que vão ganhar, eles deixam você marcar os primeiros pontos, mas depois começam a dominar o jogo.
Precisando de um empurrãozinho, você começa a falar em [Pig Latin][pig-latin], uma língua infantil inventada que é difícil para quem não é criança entender.
Isso vai te dar a vantagem para vencer seus pais!

[pig-latin]: https://en.wikipedia.org/wiki/Pig_latin

## Instructions

Sua tarefa é traduzir texto do inglês para o Pig Latin.
A tradução é definida por quatro regras, que observam o padrão de vogais e consoantes no início de uma palavra.
Essas regras observam como cada palavra usa vogais e consoantes:

- vogais: as letras `a`, `e`, `i`, `o` e `u`
- consoantes: as outras 21 letras do alfabeto inglês

## Regra 1

Se uma palavra começa com uma vogal, ou começa com `"xr"` ou `"yt"`, adicione um som `"ay"` ao final da palavra.

Por exemplo:

- `"apple"` -> `"appleay"` (começa com vogal)
- `"xray"` -> `"xrayay"` (começa com `"xr"`)
- `"yttria"` -> `"yttriaay"` (começa com `"yt"`)

## Regra 2

Se uma palavra começa com uma ou mais consoantes, primeiro mova essas consoantes para o final da palavra e depois adicione um som `"ay"` ao final da palavra.

Por exemplo:

- `"pig"` -> `"igp"` -> `"igpay"` (começa com uma única consoante)
- `"chair"` -> `"airch"` -> `"airchay"` (começa com várias consoantes)
- `"thrush"` -> `"ushthr"` -> `"ushthray"` (começa com várias consoantes)

## Regra 3

Se uma palavra começa com zero ou mais consoantes seguidas de `"qu"`, primeiro mova essas consoantes (se houver) e a parte `"qu"` para o final da palavra, e depois adicione um som `"ay"` ao final da palavra.

Por exemplo:

- `"quick"` -> `"ickqu"` -> `"ickquay"` (começa com `"qu"`, sem consoantes antes)
- `"square"` -> `"aresqu"` -> `"aresquay"` (começa com uma consoante seguida de `"qu`")

## Regra 4

Se uma palavra começa com uma ou mais consoantes seguidas de `"y"`, primeiro mova as consoantes que vêm antes do `"y"` para o final da palavra, e depois adicione um som `"ay"` ao final da palavra.

Alguns exemplos:

- `"my"` -> `"ym"` -> `"ymay"` (começa com uma única consoante seguida de `"y"`)
- `"rhythm"` -> `"ythmrh"` -> `"ythmrhay"` (começa com várias consoantes seguidas de `"y"`)

## Source

### Created by

- @behrtam

### Contributed to by

- @akashsara
- @cmccandless
- @Dog
- @ikhadykin
- @N-Parsons
- @pheanex
- @Sukhj1nder
- @tqa236
- @yawpitch

### Based on

The Pig Latin exercise at Test First Teaching by Ultrasaurus - https://github.com/ultrasaurus/test-first-teaching/tree/master/learn_ruby/pig_latin