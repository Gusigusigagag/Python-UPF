# Reading FASTA file
def FASTA_interator(fasta_filename):
    name = ""
    seq = ""
    with open(fasta_filename, "r") as inp:
        for line in inp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, "".join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, "".join(seq))


# Exercise 1 Part 1
def get_proteins_ratio_by_residue_threshold(fasta_filename, residue, relative_threshold=0.03, absolute_threshold=10):
    proteins = 0
    check_proteins = 0
    protein_len = 0
    aminoacids = 0
    for i in FASTA_interator(fasta_filename):
        proteins += 1
        if protein_len > 0:
            if aminoacids/protein_len >= relative_threshold and aminoacids >= absolute_threshold:
                check_proteins += 1
            protein_len = 0
            aminoacids = 0
        protein_len = protein_len + len(i[1])
        aminoacids = aminoacids + i[1].count(residue)
    if aminoacids/protein_len >= relative_threshold and aminoacids >= absolute_threshold:
        check_proteins += 1
    return check_proteins/proteins
print(get_proteins_ratio_by_residue_threshold('example_fasta_file.fa.txt', "A", relative_threshold=0.03, absolute_threshold=10))


# Exercise 1 Part 2
def sequence_summary(fasta_filename, output_filename, first_n=10, last_m=10):
    with open(output_filename, 'w') as out:
        protein = """"""
        aminoacids =""""""
        count_ac_list = []
        count_ac = 0
        new_line = ""
        for i in FASTA_interator(fasta_filename):
            protein = i[0].replace('>', '')
            protein = protein.strip()
            aminoacids = i[1].strip()
            if aminoacids != "":
                out.write(f'{aminoacids[0:first_n]}\t {aminoacids[-last_m:]}\t')
                for x in aminoacids:
                    if x not in count_ac_list:
                        count_ac_list.append(x)
                        count_ac_list.append(':')
                        count_ac_list.append(aminoacids.count(x))
                        count_ac_list.append(',')
                        new_line = "".join(str(a) for a in count_ac_list)
                aminoacids = """"""
                count_ac_list = []
                out.write(f'{new_line}\n')
            out.write(f'{protein}\t')
        out.write(f'{aminoacids[0:first_n]}\t {aminoacids[-last_m:]}\t')
    print("output file with name OUT_5.txt was created")
sequence_summary('example_fasta_file.fa.txt', 'out_5.txt', first_n=10, last_m=10)

# Exercise 2
def get_max_sequence_length_from_FASTA_file(fasta_filename):
    with open(fasta_filename, "r") as inp:
        string = ""
        length_list = []
        lenght_line = 0
        for line in inp:
            if not line.startswith(">"):
                string = line.strip()
                lenght_line += len(string)
            else:
                length_list.append(lenght_line)
                lenght_line = 0
        print(max(length_list))
get_max_sequence_length_from_FASTA_file("example_fasta_file.fa.txt")


# Exercise 3
def get_min_sequence_length_from_FASTA_file(fasta_filename):
    with open(fasta_filename, "r") as inp:
        string = ""
        length_list = []
        lenght_line = 0
        for line in inp:
            if not line.startswith(">"):
                string = line.strip()
                lenght_line += len(string)
            else:
                length_list.append(lenght_line)
                lenght_line = 0
        length_list.pop(0)
        print(min(length_list))
get_min_sequence_length_from_FASTA_file("example_fasta_file.fa.txt")


# Exercise 4
def get_longest_sequences_from_FASTA_file(fasta_filename):
    my_list = []
    dictionary_name_len = {}
    dictionary_name_seq = {}
    for i in FASTA_interator(fasta_filename):
        dictionary_name_seq[i[0]] = i[1]
        dictionary_name_len[i[0]] = len(i[1])
    max_len = max(dictionary_name_len.values())
    max_val = [x for x, r in dictionary_name_len.items() if r == max_len]
    for e in max_val:
        for y, h in dictionary_name_seq.items():
            if e == y:
                my_list += [(e, h)]
    my_list.sort()
    return my_list
print(get_longest_sequences_from_FASTA_file("example_fasta_file.fa.txt"))


# Exercise 5
def get_shortest_sequences_from_FASTA_file(fasta_filename):
    my_list = []
    dictionary_name_len = {}
    dictionary_name_seq = {}
    for i in FASTA_interator(fasta_filename):
        dictionary_name_seq[i[0]] = i[1]
        dictionary_name_len[i[0]] = len(i[1])
    min_len = min(dictionary_name_len.values())
    min_val = [x for x, r in dictionary_name_len.items() if r == min_len]
    for e in min_val:
        for y, h in dictionary_name_seq.items():
            if e == y:
                my_list += [(e, h)]
    my_list.sort()
    return my_list
print(get_shortest_sequences_from_FASTA_file("example_fasta_file.fa.txt"))


# Exercise 6
def get_molecular_weights(fasta_filename):
    aminoacid_mw = {'A': 89.09, 'C': 121.16, 'E': 147.13, 'D': 133.1, 'G': 75.07, 'F': 165.19, 'I': 131.18, 'H': 155.16, 'K': 146.19, 'M': 149.21, 'L': 131.18, 'N': 132.12, 'Q': 146.15, 'P': 115.13, 'S': 105.09, 'R': 174.2, 'T': 119.12, 'W': 204.23, 'V': 117.15, 'Y': 181.19}
    dictionari_protein_mw = {}
    new_list = []
    sum_list = []
    for i in FASTA_interator(fasta_filename):
        for e, h in aminoacid_mw.items():
            new_list.append(i[1].count(e)*h)
            dictionari_protein_mw[i[0]] = sum(new_list)
        new_list = []
    return dictionari_protein_mw
print(get_molecular_weights("example_fasta_file.fa.txt"))


# Exercise 7
def get_sequence_with_min_molecular_weights(fasta_filename):
    aminoacid_mw = {'A': 89.09, 'C': 121.16, 'E': 147.13, 'D': 133.1, 'G': 75.07, 'F': 165.19, 'I': 131.18, 'H': 155.16, 'K': 146.19, 'M': 149.21, 'L': 131.18, 'N': 132.12, 'Q': 146.15, 'P': 115.13, 'S': 105.09, 'R': 174.2, 'T': 119.12, 'W': 204.23, 'V': 117.15, 'Y': 181.19}
    dictionari_protein_mw = {}
    new_list = []
    tuple_prot_min = ()
    for i in FASTA_interator(fasta_filename):
        for e, h in aminoacid_mw.items():
            new_list.append(i[1].count(e)*h)
            dictionari_protein_mw[i[0]] = sum(new_list)
        new_list = []
    min_prot = min(dictionari_protein_mw.values())
    newer_list = [x for x, r in dictionari_protein_mw.items() if r == min_prot]
    for y in newer_list:
        for t, u in dictionari_protein_mw.items():
            if t == y:
                tuple_prot_min = (t, u)
    return tuple_prot_min [0:2]
print(get_sequence_with_min_molecular_weights("example_fasta_file.fa.txt"))

# Exercise 8
def get_mean_molecular_weights(fasta_filename):
    aminoacid_mw = {'A': 89.09, 'C': 121.16, 'E': 147.13, 'D': 133.1, 'G': 75.07, 'F': 165.19, 'I': 131.18, 'H': 155.16, 'K': 146.19, 'M': 149.21, 'L': 131.18, 'N': 132.12, 'Q': 146.15, 'P': 115.13, 'S': 105.09, 'R': 174.2, 'T': 119.12, 'W': 204.23, 'V': 117.15, 'Y': 181.19}
    dictionari_protein_mw = {}
    new_list = []
    for i in FASTA_interator(fasta_filename):
        for e, h in aminoacid_mw.items():
            new_list.append(i[1].count(e)*h)
            dictionari_protein_mw[i[0]] = sum(new_list)
        new_list = []
    sum_prot = sum(dictionari_protein_mw.values())
    mean_prot = sum_prot / len(dictionari_protein_mw.keys())
    return mean_prot
print(get_mean_molecular_weights("example_fasta_file.fa.txt"))
