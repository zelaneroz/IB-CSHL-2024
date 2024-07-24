def translate_dna(a:str):
    dna = ['', 'A', 'C', 'G', 'T']
    i,j, output ='',0, ''
    for i in a:
        while j<5:
            if i == dna[j]:
                output+= dna[j*-1]
            j+=1
        j=0
    if output == '':
        output='not valid'
    return output

print(translate_dna('TCGA'))