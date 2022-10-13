def divisors(num):
    try:
         if num <=0:
            raise ValueError("Ingresa un número positivo mayor a cero")    
         divisors = [x for x in range(1,num+1) if num%x == 0]
         return divisors
    except ValueError as ve:
        print(ve)


def run():
    try:
        num = int (input('ingrese un número: '))        
        print(divisors(num))
        print("Terminó mi programa.....................")
    except ValueError:
        print("Ingresa un número")
if __name__ == '__main__':
    run()