#Using List comprenhensions create a program tah contain all  multiples of 4, 6 y 9 until 5 digits.all
import time
def multiples():
    multiples_digits = [i for i in range(4,100000,1) if (i%3  == 0 and i%4 == 0  and i%6 == 0 and i%9 == 0)  ]
    lenght_elements = len(multiples_digits)

    return print(multiples_digits), lenght_elements


if __name__ == '__main__':
    initial_time = time.time()
    print('Her start the new execution: ...')
    arr = multiples()

    print('_______________________________________________________________________________-')

    print(f'There are {arr[1]} elements in the arr')


    final_time = time.time()
    time_taken = final_time -initial_time

    print('Time taken were: ', time_taken, ' seconds')