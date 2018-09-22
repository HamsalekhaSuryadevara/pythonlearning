print('impoerted my module')

test='Test string'

def find_index(to_search,target):
    for i,value in enumerate(to_search):
        if value==target:
            return 1
    return -1
#cou=['mat','cat','rat']
#print(find_index(cou,'rat'))
