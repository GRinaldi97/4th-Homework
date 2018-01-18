# 4th-Homework
Done by Giuseppe Rinaldi, Elisa Piperni and Isabella Grassuci



#3rd Problem

Two players play the following game with a nucleotide sequence of
length n = nA + nT + nC + nG , where nA, nT , nC , and nG are the
number of A,T,C, and G in the sequence. At every turn a player
may delete either one or two nucleotides from the sequence. The
player who is left with a uni-nucleotide sequence of an arbitrary
length (i.e., the sequence containing only one of 4 possible
nucleotides) loses. Who will win? Describe the winning strategy
for each nA, nT , nC , and nG .


Our reasoning:
Count the amount of each nucleotide (na, nc, ng, nt). Divide each count by three and take the remainder. Then sum the remainders.
The sum can vary from 0 to 8 (because the maximum remainder of each kind of nucleotide is 2). 
If the sum of the remainders is equal to zero or a multiple of three(0, 3 or 6), the first player cannot win, provided that the other player "plays at his best".
If the sum is not a multiple of three (1, 2, 4, 5, 7, 8) the first player, in order to win, have to bring back the sum of the residues to 0, to 3 or to 6, deleting either one or two elements depending on the initial situation (one if it's 1, 4 or 7, two if it's 2, 5 or 8) after that he has to "play at his best".
To "play at your best" means to always do the opposite move of the other player (if the other delete one, you delete two; if the other delete two, you delete one), to always mantain a remainder of 0, 3 or 6.
