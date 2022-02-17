# Exercise 1
def get_proteins_ratio_by_residue_threshold(filename, residue, relative_threshold=0.03, absolute_threshold=10):
    proteins = 0
    check_proteins = 0
    protein_len = 0
    aminoacids = 0

    with open(filename, "r") as f:

        for line in f:
            if line.startswith(">"):
                proteins += 1
                if protein_len > 0:
                    if aminoacids/protein_len >= relative_threshold and aminoacids >= absolute_threshold:
                        check_proteins += 1
                protein_len = 0  # Come back to 0 to calculate next protein
                aminoacids = 0

            else:
                line_new = line.strip()
                protein_len += len(line_new)
                aminoacids += line.count(residue)
        if aminoacids/protein_len >= relative_threshold and aminoacids >= absolute_threshold:
            check_proteins += 1
    return check_proteins/proteins
print(get_proteins_ratio_by_residue_threshold('example_fasta_file.fa.txt', "A", relative_threshold=0.03, absolute_threshold=10))


# Exercise 2
def sequence_summary(filename, output_filename, first_n=10, last_m=10):
    with open(filename, "r") as inp, open(output_filename, "w") as out:
        protein = """"""
        count_ac_list = []
        aminoacids = """"""
        count_ac = 0
        new_line = ""

        for line in inp:
            if line == line[-1]:
                line = line + ">"

            if ">" in line:
                protein = line.replace(">","")
                protein = protein.strip()

                if aminoacids != "":
                    out.write(f'{aminoacids[0:first_n]}\t {aminoacids[-last_m:]}\t')

                    for x in aminoacids:
                        if x not in count_ac_list:
                            count_ac_list.append(x)
                            count_ac_list.append(":")
                            count_ac_list.append(aminoacids.count(x))
                            count_ac_list.append(",")
                            new_line = "".join(str(i) for i in count_ac_list)
                    new_line = new_line[:-1]
                    aminoacids = """"""
                    count_ac_list = []
                    out.write(f'{new_line}\n')
                out.write(f'{protein}\t')

            else:
                line = line.strip()
                aminoacids += line

        out.write(f'{aminoacids[0:first_n]}\t {aminoacids[-last_m:]}\t')

sequence_summary('example_fasta_file.fa.txt', 'finish.txt', first_n=10, last_m=10)
# will create an output file with the name "finish.txt
