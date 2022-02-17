class Sequence(object):
    def __init__(self, identifier, sequence):
        self.identifier = identifier
        self.sequence = sequence
        self.alphabet = ['T', 'A', 'C', 'G', 'E', 'D', 'F', 'I', 'H', 'K', 'M', 'L', 'N', 'Q', 'P', 'S', 'R', 'W', 'V', 'Y', 'U']
        self.dictionary = {'A': 89.09, 'C': 121.16, 'E': 147.13, 'D': 133.1, 'G': 75.07, 'F': 165.19, 'I': 131.18, 'H': 155.16, 'K': 146.19, 'M': 149.21, 'L': 131.18, 'N': 132.12, 'Q': 146.15, 'P': 115.13, 'S': 105.09, 'R': 174.2, 'T': 119.12, 'W': 204.23, 'V': 117.15, 'Y': 181.19}


    def get_identifier(self):
        print(self.identifier)

    def get_sequence(self):
        print(self.sequence)

    def get_mw(self):
        rna_weights = {'A': 363.0, 'C': 339.0, 'U': 340.0, 'G': 379.0}
        dna_weights = {'A': 347.0, 'C': 323.0, 'T': 322.0, 'G': 363.0}
        my_list = []
        if "L" or "M" in self.sequence:
            for i in self.sequence:
                for x, y in self.dictionary.items():
                    my_list.append((str(i).count(x))*y)
                    mw = sum(my_list)
            print(mw)
        elif "U" in self.sequence:
            for i in self.sequence:
                for x, y in rna_weights():
                    my_list.append((str(i).count(x))*y)
                    mw = sum(my_list)
            print(mw)
        else:
            for i in self.sequence:
                for x, y in dna_weights:
                    my_list.append((str(i).count(x))*y)
                    mw = sum(my_list)
            print(mw)

    def has_subsequence(self, subsequence):
        if subsequence in self.sequence:
            print(True)
        else:
            print(False)


class ProteinSequence(Sequence):
    pass


class NucleotideSequence(Sequence):

    def translate(self):
        my_prot = []
        prot_list = []
        triplet = ""
        rna_table = {'GUC': 'V', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GUU': 'V', 'AAC': 'N', 'AGG': 'R', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'AGA': 'R', 'AAU': 'N', 'ACU': 'T', 'CAC': 'H', 'GUG': 'V', 'CCG': 'P', 'CCA': 'P', 'AGU': 'S', 'CCC': 'P', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'CGA': 'R', 'CAG': 'Q', 'CGC': 'R', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'GAG': 'E', 'UCC': 'S', 'UAC': 'Y', 'CGU': 'R', 'GAA': 'E', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'UCA': 'S', 'AUG': 'M', 'CUG': 'L', 'AUU': 'I', 'CAU': 'H', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V', 'UGC': 'C', 'GCU': 'A', 'UGU': 'C', 'CUC': 'L', 'UUG': 'L', 'UUA': 'L', 'GAU': 'D', 'UUC': 'F'}
        dna_table = {'CTT': 'L', 'ATG': 'M', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'AGC': 'S', 'AGA': 'R', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'ACT': 'T', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'TAC': 'Y', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GAC': 'D', 'GAA': 'E', 'AAG': 'K', 'AAA': 'K', 'AAC': 'N', 'CTC': 'L', 'CAT': 'H', 'AAT': 'N', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'TGT': 'C', 'TCT': 'S', 'GAT': 'D', 'TTT': 'F', 'TGC': 'C', 'TGG': 'W', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TCA': 'S', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A'}
        if "U" not in self.sequence:
            if (self.sequence.startswith("TTG") or self.sequence.startswith("CTG") or self.sequence.startswith("ATG")) and (self.sequence.endswith("TAA") or self.sequence.endswith("TAG") or self.sequence.endswith("TGA")):
                for i in self.sequence:
                    if i not in self.alphabet[:-1]:
                        raise ValueError("Impossible to create instance: " + str(i) + " not possible")

                    elif len(triplet) < 3:
                        triplet += i
                        if i == self.sequence[-1]:
                            prot_list.append(triplet)
                    elif len(triplet) == 3:
                        prot_list.append(triplet)
                        triplet = i

                for i in prot_list:
                    for x, y in dna_table.items():
                        if i == x:
                            my_prot.append(y)
                print("".join(my_prot))
            else:
                print("no start, or stop codons")

        else:
            if (self.sequence.startswith("UUG") or self.sequence.startswith("CUG") or self.sequence.startswith("AUG")) and (self.sequence.endswith("UAA") or self.sequence.endswith("UAG") or self.sequence.endswith("UGA")):
                for i in self.sequence:
                    if i not in self.alphabet[1:4] and i != "U":
                        raise ValueError("Impossible to create instance: " + str(i) + " not possible")

                    elif len(triplet) < 3:
                        triplet += i
                        if i == self.sequence[-1]:
                            prot_list.append(triplet)
                    elif len(triplet) == 3:
                        prot_list.append(triplet)
                        triplet = i

                for i in prot_list:
                    for x, y in rna_table.items():
                        if i == x:
                            my_prot.append(y)
                print("".join(my_prot))
            else:
                print("no start, or stop codons")


class DNASequence(NucleotideSequence):

    def transcribe(self):
        rna = []
        dna_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for i in self.sequence:
            if i not in self.alphabet[:4]:
                raise ValueError("Impossible to create instance: " + str(i) + " not possible")
            else:
                for x, y in dna_complement.items():
                    if i == x:
                        rna.append(y)
        print("".join(rna))


class RNASequence(NucleotideSequence):

    def reverse_transcribe(self):
        dna = []
        rna_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        for i in self.sequence:
            if i not in self.alphabet[1:4] and i != "U":
                    raise ValueError("Impossible to create instance: " + str(i) + " not possible")
            else:
                for x, y in rna_complement.items():
                    if i == x:
                        dna.append(y)
        print("".join(dna))

seq1 = Sequence("5gHJ", "TAACTTAT")
prot1 = ProteinSequence("Hgfh1", "AAAGQAA")
nucseq = NucleotideSequence("H1234","TAACTTCTTTTG")
DNAseq = DNASequence("H6745","TTGATTTAA")
RNAseq = RNASequence("P34E5","UUGCUCUAA")

#print(DNAseq.transcribe())
#print(RNAseq.translate())

