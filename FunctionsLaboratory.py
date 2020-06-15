def give_geom_seq_element(a_1=2, factor=2, index=2):
    #  This function was created to counting geometric sequence

    counter = 1

    while index > counter:
        if counter == 1:
            print('Sequence: %d' % counter, a_1)

        geometric_sequence = a_1 * factor
        a_1 = geometric_sequence
        print('Sequence: %d' % (counter + 1), geometric_sequence)
        counter += 1

    return


give_geom_seq_element(a_1=1, index=64)
print('------------------------------------------------------------')


def give_geom_seq_element(a_1=2, factor=2, index=2):
    #  This function was created to counting geometric sequence

    counter = 1

    while index > counter:
        if counter == 1:
            print('Sequence: %d' % counter, a_1)

        geometric_sequence = a_1 * factor
        a_1 = geometric_sequence
        print('Sequence: %d' % (counter + 1), geometric_sequence)
        counter += 1

    return


give_geom_seq_element(a_1=3, index=9)
print('------------------------------------------------------------')


def give_factor_for_geom_seq(word=0):
    # This function was created to determine the value of the geometric sequence coefficient

    words = []

    for element in range(2):
        word = input("Please input %d of 2 following the value of the "
                     "geometric sequence: " % (element + 1))
        words.append(int(word))

    words.reverse()
    output = 'The factor is: %.0f' % (words[0] / words[1])

    return output


print(give_factor_for_geom_seq())
print('------------------------------------------------------------')


def give_sum_of_n_elements_geom_seq(a_1=2, factor=3, n=4):
    #  this function determines the sum of the first elements of the geometric sequence

    sum_of_geom_seq = a_1 * ((1 - pow(factor, n)) / (1 - factor))

    return sum_of_geom_seq


print(give_sum_of_n_elements_geom_seq())
print(give_sum_of_n_elements_geom_seq(4, 6, 3))
print('------------------------------------------------------------')
