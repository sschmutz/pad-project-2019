"""This module clusters sequences based on a distance matrix using the
WPGMA (Weighted Pair Group Method with Arithmetic Mean) method.
"""

from collections import defaultdict

def Cluster(distance_matrix, labels):
    """Reads distance matrix (list of lists) and a list of labels, returns
    a binary tree in string format.
    """

    if not ValidDistanceMatrix(distance_matrix, labels):
        raise Exception("malformed input")

    distance_dict = DistanceMatrixToDict(distance_matrix, labels)

    while len(distance_dict) > 1:
        closest_pair = ShortestDistance(distance_dict)
        distance_dict = DistanceDictUpdate(distance_dict, closest_pair)

    # to end up with a properly formatted tree,
    # the list of the closest pair needs to be reformatted
    tree = "(%s, %s)" % (closest_pair[0], closest_pair[1])

    return tree



def ValidDistanceMatrix(distance_matrix, labels):
    """Reads distance matrix (list of lists) and list of labels,
    returns True if the structure is valid and False otherwise.

    Distance matrix should be of type list of lists, containing floats >= 0. and
    the same number of rows and columns.

    The diagonal of the distance matrix has to be 0.

    Labels is a list of strings with the same length of the matrix.
    """

    if type(distance_matrix) is not list:
        return False

    for row in distance_matrix:
        if type(row) is not list:
            return False

        for value in row:
            if type(value) is not float or value < 0.:
                return False

    rows = len(distance_matrix)
    columns = len(distance_matrix[0])

    if rows != columns:
        return False

    for row, column in zip(range(rows), range(columns)):
        if distance_matrix[row][column] != 0.:
            return False

    if type(labels) is not list:
        return False

    for label in labels:
        if type(label) is not str:
            return False

    if rows != len(labels):
        return False

    return True



def DistanceMatrixToDict(distance_matrix, labels):
    """Reads distance matrix and its labels and returns a 2D dictionary with
    labels as keys and distance as values.
    """

    distance_dict = defaultdict(dict)

    for row in range(0, len(distance_matrix)):
        for column in range(0, len(distance_matrix[0])-row):
            label1 = labels[row]
            label2 = labels[column+row]

            distance_dict[label1][label2] = distance_matrix[row][column+row]

    return distance_dict



def ShortestDistance(distance_dict):
    """Takes a 2D dictionary containing distance information and returns a list
    with the labels of the two closest elements.
    """

    closest_dist = None
    closest_pair = None

    for label1 in distance_dict:
        for label2 in distance_dict[label1]:
            if label1 == label2:
                continue

            dist = distance_dict[label1][label2]

            if closest_dist is None or closest_dist > dist:
                closest_dist = dist
                closest_pair = [label1, label2]

    return closest_pair



def DistanceDictUpdate(distance_dict, closest_pair):
    """Takes a 2D dictionary containing distance information and
    the closest pair, reduces it and returns an updated dictionary.

    The new distances are calculated by averaging distances between each element
    and the closest pair.
    """

    closest1 = closest_pair[0]
    closest2 = closest_pair[1]

    closest_pair_label = "(%s, %s)" % (closest_pair[0], closest_pair[1])

    distance_dict_update = defaultdict(dict)
    distance_dict_update[closest_pair_label][closest_pair_label] = 0.

    for label1 in distance_dict:
        if label1 not in closest_pair:
            if closest1 in distance_dict and label1 in distance_dict[closest1]:
                summand1 = distance_dict[closest1][label1]
            else:
                summand1 = distance_dict[label1][closest1]

            if closest2 in distance_dict and label1 in distance_dict[closest2]:
                summand2 = distance_dict[closest2][label1]
            else:
                summand2 = distance_dict[label1][closest2]

            distance_dict_update[closest_pair_label][label1] = (summand1+summand2)/2

            for label2 in distance_dict[label1]:
                if label2 not in closest_pair:
                    distance_dict_update[label1][label2] = distance_dict[label1][label2]


    return distance_dict_update



if __name__ == "__main__":
    P3_output = [[0.0, 0.4099077797760524, 0.3831192178244929, 0.2979763481017525, 0.2979763481017525, 0.24710940084768174, 0.26627569086095443],
                 [0.4099077797760524, 0.0, 0.3162942217349584, 0.35584348469633686, 0.3749669636468151, 0.3717121538268464, 0.255694940227945],
                 [0.3831192178244929, 0.3162942217349584, 0.0, 0.34841551835862816, 0.5033762053808777, 0.2281585308022437, 0.27397429978712223],
                 [0.2979763481017525, 0.35584348469633686, 0.34841551835862816, 0.0, 0.35584348469633686, 0.255694940227945, 0.2102264738656188],
                 [0.2979763481017525, 0.3749669636468151, 0.5033762053808777, 0.35584348469633686, 0.0, 0.18848582121067953, 0.2102264738656188],
                 [0.24710940084768174, 0.3717121538268464, 0.2281585308022437, 0.255694940227945, 0.18848582121067953, 0.0, 0.13947341105434174],
                 [0.26627569086095443, 0.255694940227945, 0.27397429978712223, 0.2102264738656188, 0.2102264738656188, 0.13947341105434174, 0.0]]

    P3_output_labels = ["Mouse", "Bovine", "Gibbon", "Orangutan", "Gorilla", "Chimp", "Human"]

    wikipedia_example = [[0.0, 17.0, 21.0, 31.0, 23.0],
                         [17.0, 0.0, 30.0, 34.0, 21.0],
                         [21.0, 30.0, 0.0, 28.0, 39.0],
                         [31.0, 34.0, 28.0, 0.0, 43.0],
                         [23.0, 21.0, 39.0, 43.0, 0.0]]

    wikipedia_example_labels = ["a", "b", "c", "d", "e"]

    print(Cluster(P3_output, P3_output_labels))
