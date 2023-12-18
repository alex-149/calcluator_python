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
                        
        if '+' in math_operations or '-' in math_operations or '*' in math_operations or '/' in math_operations or '^' in math_operations:
                    
            x = zs[0]
            x = float(x)
                
            y = zs[2]
            y = float(y)
                
            print(Calcluate(x, y))
        else: 
            print("Must be a valid math equation.")
