import numpy as np
from hmmlearn import hmm

states = []
observations = []
states_size = 0
observations_size = 0
start_probabilities = []
transition_probabilities = []
emission_probabilities = []

def readfile(filename):
    with open(filename, "r") as file:
        gene_seqeunce = file.read().replace('\n', '')
    return gene_seqeunce.upper()

def main(filename, prob_file):
    gene_seqence = readfile(filename)
    gene_seqence.strip()
    building_transition_matrix(prob_file)
    building_emmision_matrix(prob_file)

    viterbi_impl = hmm.MultinomialHMM(n_components=states_size)
    viterbi_impl.startprob_ = start_probabilities
    viterbi_impl.transmat_ = transition_probabilities
    viterbi_impl.emissionprob_ = emission_probabilities

    input_list = []
    for char in gene_seqence:
        if char == "A":
            input_list.append([0])
        elif char == "C":
            input_list.append([1])
        elif char == "G":
            input_list.append([2])
        else:
            input_list.append([3])

    in_text = np.array(input_list)

    out_text = viterbi_impl.decode(input_list, algorithm="viterbi")

    out = "%s" % " ".join([states[x][-1] for x in out_text])
    print("Output: " + out)


def building_transition_matrix(file):
    filename = file
    with open(filename, "r") as file:
        prob_file = file.read().replace('\n', '').split("#")
    Transition_matrix = []
    for i in range(0, len(prob_file)):
        if(prob_file[i].__contains__("Transition matrix")):
            temp_list = prob_file[i+1].split("break")
            for i in temp_list:
                Transition_matrix.append(i.strip().split(" "))
    global states, states_size , start_probabilities, transition_probabilities
    start_probabilities = Transition_matrix[1][1:]
    states_size = len(Transition_matrix[0])
    states = Transition_matrix[0]

    for i in range (1, len(Transition_matrix)):
        transition_probabilities.append(Transition_matrix[i][1:])


def building_emmision_matrix(file):
    filename = file
    with open(filename, "r") as file:
        prob_file = file.read().replace('\n', '').split("#")
    emission_matrix = []
    for i in range(0, len(prob_file)):
        if(prob_file[i].__contains__("Emission probabilities")):
            temp_list = prob_file[i+1].split("break")
            for i in temp_list:
                emission_matrix.append(i.strip().split(" "))
    global observations, observations_size, emission_probabilities
    observations_size = len(emission_matrix[0])
    observations = emission_matrix[0]

    for i in range (1, len(emission_matrix)):
        emission_probabilities.append(emission_matrix[i][1:])

main("inputs.txt","probabilities.txt")
