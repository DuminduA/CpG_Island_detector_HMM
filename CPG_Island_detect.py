import numpy as np
from hmmlearn import hmm
import read_file as input_read

# All the possible states
states = ["O", "A+", "C+", "G+", "T+", "A-", "C-", "G-", "T-"]
# Number of states
states_size = len(states)

# Observations list
observations = ["a", "c", "g", "t"]
# Observations size
observations_size = len(observations)

# Start probabilities to the sequence
start_probabilities = np.array([0,0.0725193,0.1637630,0.1788242,0.0754545,0.1322050,0.1267006,0.1226380,0.1278950])

# Transition between states probabilities
transition_probabilities = np.array([
    [0, 0.0725193, 0.163763, 0.1788242, 0.0754545, 0.1322050, 0.1267006, 0.1226380, 0.1278950],
    [0.001, 0.1762237, 0.2682517, 0.4170629, 0.1174825, 0.0035964, 0.0054745, 0.0085104, 0.0023976],
    [0.001, 0.1672435, 0.3599201, 0.267984, 0.1838722, 0.0034131, 0.0073453, 0.005469, 0.0037524],
    [0.001, 0.1576223, 0.3318881, 0.3671328, 0.1223776, 0.0032167, 0.0067732, 0.0074915, 0.0024975],
    [0.001, 0.0773426, 0.3475514, 0.375944, 0.1781818, 0.0015784, 0.0070929, 0.0076723, 0.0036363],
    [0.001, 0.0002997, 0.0002047, 0.0002837, 0.0002097, 0.2994005, 0.2045904, 0.2844305, 0.2095804],
    [0.001, 0.0003216, 0.0002977, 0.0000769, 0.0003016, 0.3213566, 0.2974045, 0.0778441, 0.3013966],
    [0.001, 0.0001768, 0.000238, 0.0002917, 0.0002917, 0.1766463, 0.2385224, 0.2914165, 0.2914155],
    [0.001, 0.0002477, 0.0002457, 0.0002977, 0.0002077, 0.2475044, 0.2455084, 0.2974035, 0.2075844]
])

# Emission Probabilities
emission_probabilities = np.array([
  [0,0,0,0],
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1],
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1]
])


def main(filename):
    # Read The file for inputs
    gene_seqence = input_read.readfile(filename)

    viterbi_impl = hmm.MultinomialHMM(n_components=states_size)
    viterbi_impl.startprob_ = start_probabilities
    viterbi_impl.transmat_ = transition_probabilities
    viterbi_impl.emissionprob_ = emission_probabilities

    # Apply viterbi algorithm to the sequence
    logprob, out_text = viterbi_impl.decode(gene_seqence, algorithm="viterbi")

    # Print out the results
    out = "%s" % " ".join([states[x][-1] for x in out_text])
    print(out)


main("inputs.txt")
