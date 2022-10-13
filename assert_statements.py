def divisors(num):
    assert num>0, "Ingresa un número positivo mayor a cero"    
    divisors = [x for x in range(1,num+1) if num%x == 0]
    return divisors



def run():
        num = input('ingrese un número: ')
        assert num.isnumeric(), "Debes ingresar un número"   
        print(divisors(int(num)))
        print("Terminó mi programa.....................")
if __name__ == '__main__':
    run()