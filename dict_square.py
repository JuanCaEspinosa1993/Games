# Crear un dictionary comprehensions cuyas llaves sean los 1000 primeros números naturales con sus raíces cuadradas como valores.
def run():
    square_root_NN = {i:i**0.5 for i in range(1,1001)}
    print(square_root_NN)

if __name__ == '__main__':
    run()