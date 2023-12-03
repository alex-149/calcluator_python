while True:
    def Calcluate(x, y):
        if '+' in math_operations:
            return x + y
        
        if '-' in math_operations:
            return x - y
        
        if '*' in math_operations:
            return x * y
        
        if '/' in math_operations:
            return x / y
        if '^' in math_operations:
            return x ** y
    
    z = str(input("Math Equation: "))
    
    math_operations = []    
            
    zs = z.split()
    
    for word in zs:
        if word in ['+', '-', '*', '/', '^']:
            math_operations.append(word)
                    
            if '+' in math_operations:
                
                x = zs[0]
                x = float(x)
                
                y = zs[2]
                y = float(y)
                
                print(Calcluate(x, y))
                
            elif '-' in math_operations:
                
                x = zs[0]
                x = float(x)
    
                y = zs[2]
                y = float(y)
                
                result = [Calcluate(x,y)]
                
                print(Calcluate(x, y))
                
            elif '*' in math_operations:
                
                x = zs[0]
                x = float(x)
                
                y = zs[2]
                y = float(y)
                
                result = [Calcluate(x,y)]
                
                print(Calcluate(x, y))
                
            elif '/' in math_operations:
                
                x = zs[0]
                x = float(x)
                
                y = zs[2]
                y = float(y)
                
                if x or y == 0:
                    print("Error Cannot Divide by Zero")
                    break
                
                result = [Calcluate(x,y)]
                
                print(Calcluate(x, y))
                
            elif '^' in math_operations:
                
                x = zs[0]
                x = float(x)
                
                y = zs[2]
                y = float(y)
                
                result = [Calcluate(x,y)]
                
                print(Calcluate(x, y))
