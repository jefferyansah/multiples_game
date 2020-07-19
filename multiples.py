#Enter a number cutoff

def calc_multiples(cut_off, multiples):
    # set a starting point
    STARTING_POINT = 0

    #generate range of numbers
    number_range = [x for x in range(STARTING_POINT, cut_off)]

    # get the multiples 
    answer = number_range[multiples::multiples]

    return print('The multiples of', str(multiples), 'between', str(STARTING_POINT ), 'and', str(cut_off),  'is', answer)

cut_off = int(input('Enter a Number greater than 0: '))
multiples = int(input('For which number do you want to find multiples of: '))
calc_multiples(cut_off, multiples)



