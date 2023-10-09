#ДНК ATGC
class DNA(object):
    def __init__(self, string : str) -> None:
        self.dna = string
    def count_nucleotides(self) -> dict:
        A = 0
        T = 0
        C = 0
        G = 0
        for i in range(len(self.dna)):
            if self.dna[i] == 'A':
                A += 1
            if self.dna[i] == 'T':
                T += 1
            if self.dna[i] == 'C':
                C += 1
            if self.dna[i] == 'G':
                G += 1
        return {'A': A, 'T': T, 'C': C, 'G': G}
    def transcribe(self) -> str:
        trans = ''
        for i in range(len(self.dna)):
            if self.dna[i] == 'A':
                tranc += 'A' 
            if self.dna[i] == 'T':
                tranc += 'U'
            if self.dna[i] == 'C':
                tranc += 'C'
            if self.dna[i] == 'G':
                tranc += 'G'
        return trans
    def complement_dna(self) -> str:
        compl = ''
        for i in range(len(self.dna)):
            if self.dna[i] == 'A':
                compl += 'T'
            if self.dna[i] == 'T':
                compl += 'A'
            if self.dna[i] == 'C':
                compl += 'G'
            if self.dna[i] == 'G':
                compl += 'C'
        return compl
    def hamming_distance(self, string_2 : str) -> int:
        distinct = ''
        while len(self.dna) == len(string_2):
            for i in range(len(self.dna)):
                if self.dna[i] != string_2[i]:
                    distinct += self.dna[i]
            return len(distinct)
        raise TypeError

        
            


string = input()
dna = DNA(string)
dna.hamming_distance(input())
print(dna.hamming_distance(input()))
