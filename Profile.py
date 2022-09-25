import math
from itertools import product,combinations
def get_residues(msa):
    residues = []
    for seq in msa:
        for res in seq:
            if res not in residues:
                residues.append(res)
    return residues

def pssm(n, msa):
    residues = get_residues(msa)
    pseudocount = 2
    msa_len = len(msa[0])
    profile = {}
    for res in residues:
        profile[res] = [0]*msa_len
    for col in range(msa_len):
        for seq in msa:
            profile[seq[col]][col] +=1
    for res in profile:
        profile[res]= [(x + pseudocount)/(n+(pseudocount*len(residues))) for x in profile[res]]
    for res in profile:
        profile[res] = [math.log2(x/(sum(profile[res])/msa_len)) for x in profile[res]]

    return profile

def generate_subs(pssm, msa_len,test_seq):
    stri = list(pssm.keys())
    if msa_len == 10:
         subs = (a+b+c+d+e+f+g+h+i+j for a,b,c,d,e,f,g,h,i,j in product(stri, repeat=msa_len) if a+b+c+d+e+f+g+h+i+j.replace("-", "") in test_seq)
    else:
        subs = map(''.join ,product(stri,repeat=msa_len) )
        subs = set(x for x in subs if x.replace("-","") in test_seq)
    return subs

def generate_binary_strings(bit_count):
    binary_strings = []
    def genbin(n, bs=''):
        if len(bs) == n:
            binary_strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')


    genbin(bit_count)
    binary_strings.remove('0'*bit_count)
    return binary_strings

def generate_subs2(pssm, msa_len, test_seq):
    windows = generate_binary_strings(msa_len)
    subs = []
    for i in range(len(test_seq) - msa_len+1):
        substr = test_seq[i:i+msa_len]
        for window in windows:
            genstring = ""
            x = 0
            for bit in window:
                if bit =='0':
                    genstring+='-'
                else:
                    genstring+=substr[x]
                    x+=1
            subs.append(genstring)
    return subs
def best_subseq(test_seq, msa, pssm):
    msa_len = len(msa[0])
    subs = generate_subs2(pssm,msa_len,test_seq)

    best_sub = ""
    best_score = 0
    for subseq in subs:
            score = 0
            for j in range(msa_len):
                score += pssm[subseq[j]][j]
            if score > best_score:
                best_score = score
                best_sub = subseq

    return best_sub


N = int(input())
msa = []
for i in range(N):
    msa.append(input())
test_seq = input()
print(best_subseq(test_seq, msa, pssm(N, msa)))

