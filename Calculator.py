class Maths:
    for i in range(1, 10):
        def addition(x, y):
            return (x + y)
        def subtraction(x, y):
            return (x - y)
        def multiplication(x, y):
            return (x * y)
        def division(x, y):
            return (x / y)
        def power(x, y):
            return (x ** y)
            
        z = str(input("Math Equation: "))

        math_operations = []    
        
        all_results = []
        
        zs = z.split()
        
        for word in zs:
            if word in ['+', '-', '*', '/', '^']:
                math_operations.append(word)
                
        if '+' in math_operations:
            print(math_operations)
            
            x = zs[0]
            x = float(x)
            print(x)
            
            y = zs[2]
            y = float(y)
            print(y)

            result = [addition(x,y)]
            
            all_results.append(result)
            
            print(addition(x, y))
            
        elif '-' in math_operations:
            print(math_operations)
            
            x = zs[0]
            x = float(x)
            print(x)
            
            y = zs[2]
            y = float(y)
            print(y)
            
            result = [subtraction(x,y)]
            
            all_results.append(result)
            
            print(subtraction(x, y))
            
        elif '*' in math_operations:
            print(math_operations)
            
            x = zs[0]
            x = float(x)
            print(x)
            
            y = zs[2]
            y = float(y)
            print(y)
            
            result = [multiplication(x,y)]
            
            all_results.append(result)
            
            print(multiplication(x, y))
            
        elif '/' in math_operations:
            print(math_operations)
            
            x = zs[0]
            x = float(x)
            print(x)
            
            y = zs[2]
            y = float(y)
            print(y)
            
            result = [division(x,y)]
            
            all_results.append(result)
            
            print(division(x, y))
            
        elif '^' in math_operations:
            print(math_operations)
            
            x = zs[0]
            x = float(x)
            print(x)
            
            y = zs[2]
            y = float(y)
            print(y)
            
            result = [power(x,y)]
            
            all_results.append(result)
            
            print(power(x, y))
            
        print(all_results)
