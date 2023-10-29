import json


with open('rna_codon_table.json') as f:
    #######################################################################
    # TODO:                                                               #
    # Use json.load function to load contents of json file to a dict      #
    #######################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    codon_table = json.load(f)
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

# Вспомогательный класс для вызова SequenceError
# raise SequenceError('Error text')
class SequenceError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
    
    def __str__(self) -> str:
        return f'{self.message}'

class Sequence(object):
    seq_type = None
    types = set(['DNA', 'RNA', 'Protein']) # all possible sequence types

    #######################################################################
    # TODO:                                                               #
    # Create sets: _prot_acids (a set of all amino acids using            #  
    # json codon_table), _dna_nucls (a set of all nucleotides in a DNA),  #
    # _rna_nucls (a set of all nucleotides in a RNA)                      #
    #######################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    _prot_acids = set(codon_table.values())
    _dna_nucls = set('A', 'T', 'G', 'C')
    _rna_nucls = set('A', 'U', 'G', 'C')
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def __init__(self, file_name: str) -> None:
        """
        Input:
        - file_name : FASTA file with sequence_name, sequence_type and 
        the sequence itself

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Using _parse and _check methods check that input sequence is        #
        # correct. Add an extra check that resulting sequence type corresponds#
        # to the given sequence_type. if everything is fine then create       #
        # sequence_attribute to store given sequence and change self.seq_type # 
        # to sequence_type, else raise Error                                  #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        # Не сделано
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        
    def _parse(self, file_name: str) -> tuple[str, str]:
        """
        Input:
        - file_name : FASTA file with sequence_name, sequence_type and 
        the sequence itself

        Output: A tuple with (sequence, sequence_type)
        """
        #######################################################################
        # TODO:                                                               #
        # Open file_name and read its contents.                               #
        # Input file format:                                                  #
        # >sequence_name sequence_type                                        #
        # sequence                                                            #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        o = open(file_name)
        contents = o.readlines()
        sequence_type = None
        for line in contents:
            if line[0] == '>':
                sequence_type = line.split()[1].split('\n')[0]
            elif sequence_type is not None:
                sequence = line
        o.close()
        return(sequence_type, sequence)

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def _check(self, string: str) -> bool:
        """
        Input:
        - string : sequence from FASTA file

        Output: A boolean value (True or False)
        """
        #######################################################################
        # TODO:                                                               #
        # Check that given type is in self.types                              #
        # Check that every element of given string is either in               #
        # self._prot_acids/self._dna_nucls/self._rna_nucls. If its true,      #
        # return True, else return False                                      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        for i in range(len(string)):
            if string[i] not in self._dna_nucls and\
            string[i] not in self._rna_nucls and string[i] not in self._prot_acids:
                return False
        # Вторая часть проверки не сделана
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def hamming_distance(self, string_2: str) -> int:
        """
        Input:
        - sequence : another sequence of nucleotides

        Output: number of different letters 
        between sequence_attribute and given string sequence
        """
        #######################################################################
        # TODO:                                                               #
        # First, check that sequence_attribute and given string have the same #
        # length, if not raise Error.                                         #
        # If the length of strings is the same, loop over one of the strings  #
        # and count different letters.                                        #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        distinct = ''
        while len(self.seq) == len(string_2):
            for i in range(len(self.seq)):
                if self.seq[i] != string_2[i]:
                    distinct += self.seq[i]
            self.h_d = len(distinct)
            return self.h_d
        raise ValueError('String lenghts are different')
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def count_nucleotides(self) -> None:
        """
        Input: None

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Raise an error, since transrcibe method can work only with elements #
        # of DNA, RNA or Protein classes                                      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        raise NameError
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> None:
        """
        Input: None

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Raise an error, since transrcibe method can work only with elements #
        # of DNA, RNA or Protein classes                                      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        raise NameError
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> None:
        """
        Input: None

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Raise an error, since transrcibe method can work only with elements #
        # of DNA or RNA classes                                               #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        raise NameError
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class DNA(Sequence):
    _type = 'DNA'
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'T', 'G', 'C' and their 
        corresponding amounts in sequence_attribute. 
        {'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        """
        #######################################################################
        # TODO:                                                               #
        # Counting 'A's, 'T's, 'G's, 'C's either by                           #
        # looping over sequence_attribute or using a standard string method.  #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
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
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def complement_dna(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'A's were changed to 'T's
        and vice versa, all 'C's changed to 'G's and vice versa
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over sequence_attribute with        #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.seq_compl_dna = ''
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                self.seq_compl_dna += 'T'
            if self.seq[i] == 'T':
                self.seq_compl_dna += 'A'
            if self.seq[i] == 'C':
                self.seq_compl_dna += 'G'
            if self.seq[i] == 'G':
                self.seq_compl_dna += 'C'
        return self.seq_compl_dna
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'T's were changed to 'U's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over sequence_attribute with        #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.seq_trans = ''
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                self.seq_trans += 'A' 
            if self.seq[i] == 'U':
                self.seq_trans += 'T'
            if self.seq[i] == 'C':
                self.seq_trans += 'C'
            if self.seq[i] == 'G':
                self.seq_trans += 'G'
        return self.seq_trans
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output: a NEW string, where all nucleotides are replaced with codons
        """
        #######################################################################
        # TODO:                                                               #
        # First transcribe DNA sequence to RNA using transcribe() method.     #
        # Second find 'AUG' - start codon. If it is found use json codon table#
        # to transcribe every 3 nucleotides of sequence_attribute to a codon, #
        # if a stop-codon is met then stop the transcription, else transcribe #
        # untill the end of the sequence.                                     #
        # If start codon was not found - raise Error                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        # Не сделано
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def restriction_slices(self) -> int:
        """
        Input: None

        Output: number of slices by EcoRI restrictase
        """
        #######################################################################
        # TODO:                                                               #
        # EcoRI restrictase slices 'GAATTC'/'CTTAAG' sequences, return        #
        # resulting number of slices                                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        rest_sl = ''
        for i in range(0, (len(self.seq - 5))):
            if self.seq[i:i+6] == 'GAATTC' or self.seq[i:i+6] == 'CTTAAG':
                rest_sl += 1
        self.r_s = len(rest_sl)
        return self.r_s
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class RNA(Sequence):
    _type = 'RNA'
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'U', 'G', 'C' and their 
        corresponding amounts in sequence_attribute. 
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C}
        """
        #######################################################################
        # TODO:                                                               #
        # Counting 'A's, 'U's, 'G's, 'C's either by                           #
        # looping over sequence_attribute or using a standard string method.  #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
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
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'U's were changed to 'T's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over sequence_attribute with        #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.seq_trans = ''
        for i in range(len(self.seq)):
            if self.seq[i] == 'A':
                self.seq_trans += 'A' 
            if self.seq[i] == 'U':
                self.seq_trans += 'T'
            if self.seq[i] == 'C':
                self.seq_trans += 'C'
            if self.seq[i] == 'G':
                self.seq_trans += 'G'
        return self.seq_trans
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output: a NEW string, where all nucleotides are replaced with codons
        """
        #######################################################################
        # TODO:                                                               #
        # First find 'AUG' - start codon. If it is found use json codon table #
        # to transcribe every 3 nucleotides of sequence_attribute to a codon, #
        # if a stop-codon is met then stop the transcription, else transcribe #
        # untill the end of the sequence.                                     #
        # If start codon was not found - raise Error                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        # Не сделано
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class Protein(Sequence):
    _type = 'Protein'
    #######################################################################
    # TODO:                                                               #
    # Create two sets of positive charge amino acids and negative charge  #
    # amino acids: _pos_acids and _neg_acids                              #
    #######################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    _pos_acids = set('K', 'R', 'H')
    _neg_acids = set('E', 'D')
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    def count_amino_acids(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with amino acids as keys and their corresponding
        amounts in sequence_attribute
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C ...}
        """
        #######################################################################
        # TODO:                                                               #
        # Using dictionary with codons as values, create a new dictionary     #
        # with amino acids and count them in sequence_attribute by            #
        # looping over sequenceattribute or using a standard string method.   #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        A = 0
        V = 0
        L = 0
        J = 0
        M = 0
        P = 0
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
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output:
        - sequence of amino acids
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C ...}
        """
        #######################################################################
        # TODO:                                                               #
        # Returning sequence_attribute is enough                              #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def charge(self) -> int:
        """
        Input: None

        Output:
        - resulting charge of sequence
        """
        #######################################################################
        # TODO:                                                               #
        # Loop over the amino acids and check if they are in _pos_acids or    #
        # _neg_acids. If in _pos_acids then charge increases by 1, if in      #
        # _neg_acids decreases by 1, else does not changes                    #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****