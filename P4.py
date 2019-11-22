"""This module clusters sequences based on a distance matrix using the
WPGMA (Weighted Pair Group Method with Arithmetic Mean) method
"""

from collections import defaultdict

def Cluster(distance_matrix, labels):
    """Reads distance matrix (list of lists) and list of labels, returns
    a binary tree in string format.
    """

    if not ValidDistanceMatrix(distance_matrix, labels):
        raise Exception("malformed input")

    distance_dict = DistanceMatrixToDict(distance_matrix, labels)
    shortest_dist_pair, shortest_dist_pair_name = ShortestDistance(distance_dict)


    while len(distance_dict) > 2:

        distance_dict = DistanceDictUpdate(distance_dict, shortest_dist_pair, shortest_dist_pair_name)
        shortest_dist_pair, shortest_dist_pair_name = ShortestDistance(distance_dict)


    tree = shortest_dist_pair_name

    return tree



def ValidDistanceMatrix(distance_matrix, labels):
    """Reads distance matrix (list of lists) and list of labels
    and returns False if the structure is not valid.

    distance matrix should be of type list of lists (rectangular)

    labels is a list of strings with the same length of the matrix

    ?TODO check if matrix contains 0 on the diagonal
    """

    if type(distance_matrix) is not list:
        return False

    if len(distance_matrix) != len(distance_matrix[0]):
        return False

    for row in distance_matrix:
        if type(row) is not list:
            return False

        for value in row:
            if type(value) is not float:
                return False

    if type(labels) is not list:
        return False

    for label in labels:
        if type(label) is not str:
            return False

    if len(distance_matrix) != len(labels):
        return False

    return True



def DistanceMatrixToDict(distance_matrix, labels):
    """Reads distance matrix and its labels and returns a 2D dictionary."""

    distance_dict = defaultdict(dict)

    for row in range(0, len(distance_matrix)):
        for column in range(0, len(distance_matrix[0])-row):
            label1 = labels[row]
            label2 = labels[column+row]

            distance_dict[label1][label2] = distance_matrix[row][column+row]

    return distance_dict



def ShortestDistance(distance_dict):
    """Takes a 2D dictionary containing distance information and returns a list
    with the labels of the two closest entries and a string formatted according
    requirements for the tree.
    """

    shortest_dist = None
    shortest_dist_pair = None

    for label1 in distance_dict:
        for label2 in distance_dict[label1]:
            if label1 == label2:
                continue

            dist = distance_dict[label1][label2]
            dist_pair = [label1, label2]

            if shortest_dist is None or shortest_dist > dist:
                shortest_dist = dist
                shortest_dist_pair = dist_pair

    shortest_dist_pair_name = "(%s, %s)" % (shortest_dist_pair[0], shortest_dist_pair[1])

    return shortest_dist_pair, shortest_dist_pair_name



def DistanceDictUpdate(distance_dict, shortest_dist_pair, shortest_dist_pair_name):
    """Takes 2D dictionary containing distance information and infromation about
    shortest distance pair, reduces the dictionary and returns an updated one.
    """

    shortest1 = shortest_dist_pair[0]
    shortest2 = shortest_dist_pair[1]

    distance_dict_update = defaultdict(dict)
    distance_dict_update[shortest_dist_pair_name][shortest_dist_pair_name] = 0.0

    for label1 in distance_dict:
        if label1 not in shortest_dist_pair:
            if shortest1 in distance_dict and label1 in distance_dict[shortest1]:
                summand1 = distance_dict[shortest1][label1]
            else:
                summand1 = distance_dict[label1][shortest1]

            if shortest2 in distance_dict and label1 in distance_dict[shortest2]:
                summand2 = distance_dict[shortest2][label1]
            else:
                summand2 = distance_dict[label1][shortest2]

            distance_dict_update[shortest_dist_pair_name][label1] = (summand1+summand2)/2

            for label2 in distance_dict[label1]:
                if label2 in shortest_dist_pair:
                    continue
                distance_dict_update[label1][label2] = distance_dict[label1][label2]

    return distance_dict_update



if __name__ == '__main__':
    P3_output = [[0.0, 0.4099077797760524, 0.3831192178244929, 0.2979763481017525, 0.2979763481017525, 0.24710940084768174, 0.26627569086095443],
                 [0.4099077797760524, 0.0, 0.3162942217349584, 0.35584348469633686, 0.3749669636468151, 0.3717121538268464, 0.255694940227945],
                 [0.3831192178244929, 0.3162942217349584, 0.0, 0.34841551835862816, 0.5033762053808777, 0.2281585308022437, 0.27397429978712223],
                 [0.2979763481017525, 0.35584348469633686, 0.34841551835862816, 0.0, 0.35584348469633686, 0.255694940227945, 0.2102264738656188],
                 [0.2979763481017525, 0.3749669636468151, 0.5033762053808777, 0.35584348469633686, 0.0, 0.18848582121067953, 0.2102264738656188],
                 [0.24710940084768174, 0.3717121538268464, 0.2281585308022437, 0.255694940227945, 0.18848582121067953, 0.0, 0.13947341105434174],
                 [0.26627569086095443, 0.255694940227945, 0.27397429978712223, 0.2102264738656188, 0.2102264738656188, 0.13947341105434174, 0.0]]

    P3_output_labels = ["Mouse", "Bovine", "Gibbon", "Orangutan", "Gorilla", "Chimp", "Human"]

    print(Cluster(P3_output, P3_output_labels))
