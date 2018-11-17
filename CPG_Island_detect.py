
def readfile(filename):
    with open(filename, "r") as file:
        gene_seqeunce = filename.read().replace('\n', '')
    return gene_seqeunce

def main(filename):
    gene_seqence = readfile(filename)

def building_transition_matrix():
    filename = "probabilities.txt"
    with open(filename, "r") as file:
        gene_seqeunce = file.read().replace('\n', '').split("#")
    print(gene_seqeunce)
    for i in range(0, len(gene_seqeunce)):
        if(gene_seqeunce[i].__contains__("Transition matrix")):
            transition_matrix_temp = gene_seqeunce[i+1].split("break")
            print(transition_matrix_temp)


building_transition_matrix()