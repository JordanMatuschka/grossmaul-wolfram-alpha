# grossmaul-wolfram-alpha
Wolfram Alpha short answers plugin for the [Grossmaul IRC bot](https://github.com/JordanMatuschka/grossmaul)

## Installation:
1) git clone this project into your `grossmaul/plugins` directory (allowing it to a subdirectory)
2) edit `grossmaul/plugins/grossmaul-wolfram-alpha/grossmaul-wolfram-alpha.py` to add your Wolfram APP ID
3) restart grossmaul

## Usage:
This plugin adds a single command, `wolfram`. Anything after the command is passed to the Wolfram Short Answers API

```
!wolfram how many bones are in the human body?
[Wolfram] Adult humans typically have 206 bones

!wolfram how many inches is it from new york city to santa fe?
[Wolfram] about 112 million inches

!wolfram how can entropy be reversed
[Wolfram] THERE IS AS YET INSUFFICIENT DATA FOR A MEANINGFUL ANSWER
```
