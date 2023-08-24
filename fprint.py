def fprint(str:str,
           
            # You need to provide the colors as 3 digit strings, eg '009'
            # https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg

           color:str='255',
           background:str='232',
           bold:bool=False,
           italic:bool=False,
           underline:bool=False
           ):
    
    print(f'\x1b[0;{"4;" if underline else ""}{"3;" if italic else ""}{"1;" if bold else ""}48;5;{background};38;5;{color}m'+str)

def unprint(
        num_lines:int
        ):
    for i in range(num_lines):
        print("\033[1A","\x1b[2K", end='')