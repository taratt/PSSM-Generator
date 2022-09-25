# PSSM-Generator
This project first builds a profile for the given multiple sequence alignment and then using that profile, determines the most similar subsequence of a long given protein sequence to that MSA.
<br>
The profile is made just like the way PSSM is created, with the difference that the gaps are also considered. Pseudocount is equal to 2 in this implementation in order to avoid log(0). After the creation of the profile, the code looks for subsequence of the given long protein sequence that has the highest score according to the profile.
<br>
