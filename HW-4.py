# Exercise 1
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

for i in FASTA_interator("example_fasta_file.fa.txt"):
    print(i)
    #print(type(i))


# Exercise 2
def compare_fasta_file_identifiers(fasta_filenames_list1, fasta_filenames_list2, fasta_filenames_list3):
    set_1 = set()
    set_2 = set()
    set_3 = set()
    set_4 = set()
    x = set()
    count = 0
    dictionary_1 = {}
    dictionary_2 = {}
    dictionary_3 = {}
    with open(fasta_filenames_list1 , "r") as inp1, open(fasta_filenames_list2, "r") as inp2, open(fasta_filenames_list3, "r") as inp3:
        inpts = [inp1, inp2, inp3]
        for i in inpts:
            if count == 0:
                for line in i:
                    if ">" in line:
                        line1 = line.strip()
                        line1.upper
                        set_1.add(line1)
                        dictionary_1[line1] = 1
                        set_3.add(line1)
                        set_4.add(line1)
                count = 1
            else:
                for line in i:
                    if ">" in line:
                        line1 = line.strip()
                        line1.upper
                        set_1.add(line1)
                        dictionary_1[line1] = dictionary_1.get(line1, 0) + 1
                        set_2.add(line1)
                        set_4.add(line1)
                set_3.intersection_update(set_2)
                set_2.clear
            dictionary_2[i.name] = set(set_4)
            my_set4 = set()

        for key,value in dictionary_2.items():
            x = set(value)
            for t,p in dictionary_2.items():
                y = set(p)
                if key != t:
                    x.difference_update(y)
            dictionary_3[key] = x

        dictionary_4 = {"intersection": set_3, "union": set_1, "frequency": dictionary_1, "specific":dictionary_3}
        return(dictionary_4)
print(compare_fasta_file_identifiers("example_fasta_file1.fa","example_fasta_file2.fa","example_fasta_file3.fa"))

