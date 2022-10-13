import time
def run():
   
    natural_numbers = [x**2 for x in range(1,101,1) if x**2%3 != 0]

    return print(natural_numbers)



if __name__ == '__main__':
        initial_time = time.time()
        run()
        final_time = time.time()
        print('\n')
        print('Time taken: ',round((final_time -initial_time),10), ' seconds')
