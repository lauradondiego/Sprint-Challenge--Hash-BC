#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
        # dont forget hashtable
        hash_table_insert(hashtable, i.source, i.destination)

    current_ticket = hash_table_retrieve(hashtable, "NONE")
    # ^ get the first one
    while current_ticket is not "NONE":
        for i in range(len(route)):
            route[i] = current_ticket  # i think route is like storage here

            current_ticket = hash_table_retrieve(hashtable, current_ticket)
            # ^ new current ticket
            if current_ticket is "NONE":
                route[i+1] = current_ticket  # if its last, go next insert
                break

# Your function should output an array of strings with
# the entire route of your trip.
# start airport NONE, end airport NONE
    return route
