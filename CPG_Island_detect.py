
def readfile(filename):
    with open(filename, "r") as file:
        gene_seqeunce = filename.read().replace('\n', '')
    return gene_seqeunce

