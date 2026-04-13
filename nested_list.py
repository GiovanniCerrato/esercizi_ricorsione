def count_leaf_nodes(input_list):
    #terminale
    if input_list == 0:
        return 0
    #non terminale
    else:
        counter = 0
        for element in input_list:
            #check if element is a list
            if type(element) == list:
                counter += count_leaf_nodes(element)
            #else we add 1
            else:
                counter += 1
        return counter


if __name__ == '__main__':
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names)) #we expect 10