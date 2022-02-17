
def calculate_aminoacid_frequencies(fasta_filename, subsequences_filename, number_of_repetitions, output_filename):
    with open(fasta_filename, "r") as inp,\
            open(subsequences_filename, "r") as subseq, \
                open(output_filename, "w") as out:
                list = []
                file = open(fasta_filename)
                fasta_list = file.readlines()
                check_protein = 0
                n_proteins = 0
                n_seq = 0
                dictionary_check_proteins = {}
                dictionary_proportion = {}
                sub_string = ""
                calc = 0

                for line1 in inp:
                    if ">" in line1:
                        n_proteins += 1

                out.write("{:s} {:18}\n".format("#Number of proteins:", n_proteins))

                for line in subseq:
                    n_seq += 1
                    sequence = line.strip()
                    dictionary_check_proteins[sequence] = 0
                    dictionary_proportion[sequence] = 0

                out.write("{:s} {:14}\n".format("#Number of subsequences:", n_seq))
                out.write(f'{"#subsequence proportions:"}\n')

                for i in dictionary_check_proteins:
                    for y in fasta_list:
                        if ">" in y:
                            calc = sub_string.count(i)
                            if calc >= number_of_repetitions:
                                dictionary_check_proteins[i] += 1
                                check_protein += 1
                                sub_string = ""
                        else:
                            y = y.strip()
                            sub_string += y

                    list.append((i, check_protein, check_protein/n_proteins))
                    check_protein = 0

                sorted_list = sorted(list, key=lambda element: element[2], reverse=True)
                for j in sorted_list:
                    out.write("{:12s} {:>6d} {:>19.4f}\n".format(j[0], j[1], j[2]))


calculate_aminoacid_frequencies("example_fasta_file.fa.txt", "sequence_fragments.txt", 4, "output.txt")
#  Gives the output file with name "output.txt"
