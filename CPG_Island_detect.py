
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
    Transition_matrix = []
    for i in range(0, len(gene_seqeunce)):
        if(gene_seqeunce[i].__contains__("Transition matrix")):
            temp_list = gene_seqeunce[i+1].split("break")
            for i in temp_list:
                Transition_matrix.append(i.strip().split(" "))
    return(Transition_matrix)

def building_emmision_matrix():
    filename = "probabilities.txt"
    with open(filename, "r") as file:
        gene_seqeunce = file.read().replace('\n', '').split("#")
    Transition_matrix = []
    for i in range(0, len(gene_seqeunce)):
        if(gene_seqeunce[i].__contains__("Emission probabilities")):
            temp_list = gene_seqeunce[i+1].split("break")
            for i in temp_list:
                Transition_matrix.append(i.strip().split(" "))
    return(Transition_matrix)

def viterbi(sequence, transition_matrix, emission_matrix):

    # print(transition_matrix)
    # print(emission_matrix)

    plus_prob_each_step = []
    minus_prob_each_step = []

    for symbol in range(0, len(sequence)):

        symbol_plus = sequence[symbol] + "+"
        symbol_minus = sequence[symbol] + "-"


        if symbol == 0:
            previous_symbol = "0"
        else:
            previous_symbol = sequence[symbol - 1]

        if(previous_symbol == "0"):

            probability_plus = float(transition_matrix[1][transition_matrix[0].index(symbol_plus) + 1])
            probability_minus = float(transition_matrix[1][transition_matrix[0].index(symbol_minus) + 1])

            plus_prob_each_step.append(probability_plus)
            minus_prob_each_step.append(probability_minus)

        else:
            previous_plus_prob = plus_prob_each_step[len(plus_prob_each_step) - 1]
            previous_minus_prob = minus_prob_each_step[len(minus_prob_each_step) - 1]

            previous_symbol_plus = previous_symbol + "+"
            previous_symbol_minus = previous_symbol + "-"

            transition_prob_plus = []
            transition_prob_minus = []
            transition_prob_plus.append(transition_matrix[transition_matrix[0].index(previous_symbol_plus) + 1][transition_matrix[0].index(symbol_plus) + 1])
            transition_prob_plus.append(transition_matrix[transition_matrix[0].index(previous_symbol_minus) + 1][transition_matrix[0].index(symbol_plus) + 1])
            transition_prob_minus.append(transition_matrix[transition_matrix[0].index(previous_symbol_plus) + 1][transition_matrix[0].index(symbol_minus) + 1])
            transition_prob_minus.append(transition_matrix[transition_matrix[0].index(previous_symbol_minus) + 1][transition_matrix[0].index(symbol_minus) + 1])


            new_prob_1 = previous_plus_prob * float(transition_prob_plus[0]) * 1
            new_prob_2 = previous_plus_prob * float(transition_prob_plus[1]) * 1
            new_prob_3 = previous_minus_prob * float(transition_prob_minus[0]) * 1
            new_prob_4 = previous_minus_prob * float(transition_prob_minus[1]) * 1

            plus_prob_each_step.append(max(new_prob_1, new_prob_2))
            minus_prob_each_step.append(max(new_prob_3, new_prob_4))

    output = ""
    for i in range(0, len(sequence)):

        if plus_prob_each_step[i] > minus_prob_each_step[i]:
            output = output + "+"
        else:
            output = output + "-"

    print(output)



# building_transition_matrix()
# building_emmision_matrix()

viterbi("ACGT", building_transition_matrix(), building_emmision_matrix())