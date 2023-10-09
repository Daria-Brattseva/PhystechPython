class Sequence(object):
    def __init__(self, string: str) -> None:
        self.seq = string
    def transcribe(self) -> None:
        raise TypeError
    def hamming_distance(self, string_2 : str) -> int:
        distinct = ''
        while len(self.seq) == len(string_2):
            for i in range(len(self.seq)):
                if self.seq[i] != string_2[i]:
                    distinct += self.seq[i]
            return len(distinct)
        raise TypeError

class DNA(Sequence):
    def count_nucleotides(self) -> dict:
        A = 0
        T = 0
        C = 0
        G = 0
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                A += 1
            if self.seq[i] == 'T':
                T += 1
            if self.seq[i] == 'C':
                C += 1
            if self.seq[i] == 'G':
                G += 1
        return {'A': A, 'T': T, 'C': C, 'G': G}
    def transcribe(self) -> str:
        trans = ''
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                trans += 'A' 
            if self.seq[i] == 'T':
                trans += 'U'
            if self.seq[i] == 'C':
                trans += 'C'
            if self.seq[i] == 'G':
                trans += 'G'
        return trans
    def complement_dna(self) -> str:
        compl = ''
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                compl += 'T'
            if self.seq[i] == 'T':
                compl += 'A'
            if self.seq[i] == 'C':
                compl += 'G'
            if self.seq[i] == 'G':
                compl += 'C'
        return compl

class RNA(Sequence):
    def transcribe(self) -> str:
        trans = ''
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                trans += 'A' 
            if self.seq[i] == 'U':
                trans += 'T'
            if self.seq[i] == 'C':
                trans += 'C'
            if self.seq[i] == 'G':
                trans += 'G'
        return trans
    def count_nucleotides(self) -> dict:
        A = 0
        U = 0
        C = 0
        G = 0
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                A += 1
            if self.seq[i] == 'U':
                U += 1
            if self.seq[i] == 'C':
                C += 1
            if self.seq[i] == 'G':
                G += 1
        return {'A': A, 'U': U, 'C': C, 'G': G}


string1 = 'GAGAGTCGCG'
string2 = 'GAUUCUAGCU'
string3 = 'GATCGCTAGC'
seq = Sequence(string1)
rna = RNA(string2)
dna = DNA(string3)
print(dna.transcribe())
print(rna.transcribe())
print(dna.hamming_distance('GAGCTAGGAG'))
print(rna.hamming_distance('AAGCGUAUAU'))
print(dna.count_nucleotides())
print(rna.count_nucleotides())
print(dna.complement_dna())
print(seq.transcribe())

