import numpy as np

def readfile(filename):
    with open(filename, "r") as file:
        gene_seqeunce = file.read().replace('\n', '').upper()

    input_list = []
    for char in gene_seqeunce:
        if char == "A":
            input_list.append([0])
        elif char == "C":
            input_list.append([1])
        elif char == "G":
            input_list.append([2])
        else:
            input_list.append([3])

    in_text = np.array(input_list)
    return in_text