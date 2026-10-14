def calcularDesconto(*args,desconto = 0):
        try:
            total = 0
            for num in args:
                    total += num
            total -= total * (desconto/100)
        except ValueError:
               print("digite um valor válido")
        else:
               return(total)
       
               
                   

total = calcularDesconto(10,20,10,desconto=10)
print(total)
        
        
    
    