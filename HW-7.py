# Exercise 1
class Protein():
    def __init__(self, identifier, sequence):
            self.identifier = identifier
            self.sequence = sequence

    def get_identifier(self):
        print(self.identifier)

    def get_sequence(self):
        print(self.sequence)

    def get_mw(self):
        my_list = []
        aminoacid_mw = {'A': 89.09, 'C': 121.16, 'E': 147.13, 'D': 133.1, 'G': 75.07, 'F': 165.19, 'I': 131.18, 'H': 155.16, 'K': 146.19, 'M': 149.21, 'L': 131.18, 'N': 132.12, 'Q': 146.15, 'P': 115.13, 'S': 105.09, 'R': 174.2, 'T': 119.12, 'W': 204.23, 'V': 117.15, 'Y': 181.19}
        for i in self.sequence:
            for x, y in aminoacid_mw.items():
                my_list.append(i.count(x)*y)
                mw = sum(my_list)
        print(mw)

    def has_subsequence(self, subsequence):
        if subsequence in self.sequence:
            print(True)
        else:
            print(False)

    def get_lenght(self):
        lenght = len(self.sequence)
        print(lenght)

# Exercise 2
def FASTA_iterator(fasta_filename):
    fd = open(fasta_filename)
    sequence = ""

    for line in fd:
        if line[0] == ">":
            if len(sequence)>0:
                yield(Protein(identifier, sequence))
            seq = ""
            identifier = line[1:].strip()
        else:
            sequence += line.strip()

    if len(sequence)>0:
        yield(Protein(identifier, sequence))

    fd.close()


for protein in FASTA_iterator("example_fasta_file.fa.txt"):
   print(protein.identifier)
