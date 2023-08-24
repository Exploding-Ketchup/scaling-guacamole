# Scaling-guacamole
## Easily print coloured/underlined/italic/bold text; also, 'unprint' text
### How to use `fprint()`:
- Copy `fprint.py` into your project directory
- Import the functions: `from fprint import *`
- You need to provide the colors as 3 digit strings, eg '009': https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg
- `fprint()` takes the following arguments:
`color:str='255',`
` background:str='232',`
` bold:bool=False,`
` italic:bool=False,`
` underline:bool=False`
- For example:
- `fprint(
str='Lorem ipsum dolor sit amet, consecteur adipiscing elit',
color='009',
background='021',
bold=True,
italic=True,
underline=True,
)`
### How to use `unprint()`
- It takes 1 argument: the number of lines you want to unprint
## Why to use
This file allows you to print formatted text without having to use ANSI escape codes.
Other than that it's pretty useless
