# Create a program using dictionaries. Each key is a natural number 0-100 and its value is the same number elevate 
#power 3. After that add only if the number is not multiple of 3.
# 1. JHow I resolve this problem
print('Firstmethod \n')
import time
def run():
    natural_number = {}
    for i in range(3,101):
        if i%3 != 0:
             natural_number.update({i: i**3})
    print(natural_number, '\n')

    # 2. With dict comprehensions
    print('Second method')
    my_dict =  {i : i**3 for i in range(1,101) if i%3 != 0}
    print(my_dict, '\n')

    print('third method \n')

    dic_for = {}
    for i in range(1,101):
        if i%3 != 0:
            dic_for[i] = i**3
    print(dic_for, '\n')
    return print(f"Here start the return value: \n{natural_number, my_dict,dic_for}")

if __name__ == '__main__':
        initial_time = time.time()
        run()
        final_time = time.time()
        print('\n')
        print('Time taken: ',round((final_time -initial_time),10), ' seconds')
    
