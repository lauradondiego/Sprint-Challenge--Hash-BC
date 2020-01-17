#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(0, length):  # from start to finish
        hash_table_insert(ht, weights[i], i)  # use HTI method

    for i in range(0, length):
        difference = limit - weights[i]  # now find the difference subtract
        result_difference = hash_table_retrieve(ht, difference)
        if result_difference is not None:
            return (result_difference, i)

    # finds two items whose sum of weights equals the weight
    # limit `limit`. Your function will return an instance of
    # an `Answer` tuple that has the following form:

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
