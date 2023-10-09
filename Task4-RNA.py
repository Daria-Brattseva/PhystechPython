class RNA(object):
    def __init__(self, string : str) -> None:
        self.rna = string
    def transcribe(self) -> str:
        trans = ''
        for i in range(len(self.rna)):
            if self.rna[i] == 'A':
                trans += 'A' 
            if self.rna[i] == 'U':
                trans += 'T'
            if self.rna[i] == 'C':
                trans += 'C'
            if self.rna[i] == 'G':
                trans += 'G'
        return trans


string = input()
rna = RNA(string)
print(rna.transcribe())
