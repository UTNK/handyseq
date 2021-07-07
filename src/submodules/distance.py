import sys

def calc_distance(seq1, seq2, definition):

    if (len(seq1) != len(seq2)):

        print("Sequence length should be the same among all sequences!")
        sys.exit(1)

    if definition == "NHD":

        number_of_difference = 0
        number_of_total_positions = 0

        for i in range(len(seq1)):

            if (seq1[i] != "-" and seq2[i] != "-"):

                number_of_total_positions += 1

                if (seq1[i] != seq2[i]):

                    number_of_difference += 1
        
        return number_of_difference / number_of_total_positions