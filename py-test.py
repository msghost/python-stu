#A和T配对，G和C配对
def dna_decode(dna):
    dna = dna.upper()
    r_dna = ''
    dnadict = {'A':'T','T':'A','G':'C','C':'G'}
    for i in dna:
        if i in dnadict:
            r_dna += dnadict[i]
        else:
            r_dna += i
    return r_dna


x = 'aaabbbcccddd'
print(dna_decode(x))
