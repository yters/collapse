Demonstrate model collapse with a Markov model trained on Three Little Pigs.

Example usage:
```
for i in `seq 10`; do python3 code/mm.py data/pigs.txt 5 100 5000 results/degrade.txt; done
for i in `seq 10`; do python3 code/mm.py data/pigs.txt 5 100 5000 results/filter.txt -f; done
RScript code/vocab.R
```
