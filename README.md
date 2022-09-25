# PSSM-Generator
This project first builds a profile for the given multiple sequence alignment and then using that profile, determines the most similar subsequence of a long given protein sequence to that MSA.
<br>
The profile is made just like the way PSSM is created, with the difference that the gaps are also considered. Pseudocount is equal to 2 in this implementation in order to avoid log(0). After the creation of the profile, the code looks for subsequence of the given long protein sequence that has the highest score according to the profile.
<br>
## Input
The inputs to this code are 1) an integer n, which is the number of sequences that are in the MSA 2) the actual protein sequences in the MSA (which are given in the next n lines) and 3) the long sequence which the most similar subsequence is going to be extracted from it.
<br>
Example:
```
4
HVLIP
H-MIP
HVL-P
LVLIP
LIVPHHVPIPVLVIHPVLPPHIVLHHIHVHIHLPVLHIVHHLVIHLHPIVL
```
## Output
The outputs to this code is the most similar subsequence of the long sequence to the MSA.
<br>
Example:
```
H-L-P
```
