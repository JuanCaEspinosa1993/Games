from functools import reduce
def run():
    my_list =[2,3,1,3,4]

    all_muliplied = reduce(lambda a, b: a*b, my_list)
    print(all_muliplied)



if __name__ == '__main__':
    run()