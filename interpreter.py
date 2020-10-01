tokenizer = { 'line':0 }

def __variableCheck__(var_chk):
    return tokenizer.get(var_chk)


def __parse__(line:str):
    line = line.replace(' ','')
    for lc in range(len(line)):
        try:
            if(line[lc] == '+'):
                a = __variableCheck__(line[:line.find('+')]) 
                b = __variableCheck__(line[line.find('+')+1:]) 
                print(a,b)
                try:
                    return int(a)+int(b)
                except:
                    return a+b     
        except:
            print('Cannot concatinate')
            return "Error"
        
        try:
            if(line[lc] == '='):
                tokenizer.update({ line[:line.find('=')]:line[line.find('=')+1:] })
                return line[lc+1:]
        except:
            print('Syntax Error in Assigning Variable')
        
        try:
            varchk = __variableCheck__(line)
            if(varchk != None):
                return varchk
        except:
            print('VariableError')



while(True):
    __input__ = input(">> ")
    print("--",__parse__(__input__))




