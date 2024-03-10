import sys
from collections import Counter
from math import log
from random import choices

alph = set('abcdefghijklmnopqrstuvwxyz ')
words = set(open('data/words').read().splitlines())
txt = ''.join([c for c in open(sys.argv[1]).read().lower() if c in alph])
win = int(sys.argv[2])

for iteration in range(int(sys.argv[3])):
    if '-f' in sys.argv:
        txt = ' '.join([w for w in txt.split() if w in words])
    model = {}
    kmers = {}
    for i in range(len(txt)-win-1):
        for j in range(win+1):
            prefix = txt[i:i+win-j]
            letter = txt[i+win-j]
            dist = model.get(prefix, {})
            dist[letter] = dist.get(letter, 0) + 1
            model[prefix] = dist
            kmer = prefix+letter
            kmers[kmer] = kmers.get(kmer, 0) + 1
    
    for prefix, dist in model.items():
        total = float(sum(dist.values()))
        for letter, freq in dist.items():
            dist[letter] = freq/total
        model[prefix] = dist
    
    gen_len = int(sys.argv[4])
    txt = ''
    for _ in range(gen_len):
        pred = choices(*list(zip(*list(model[''].items()))))
        for j in range(1, win):
            w = txt[-j:]
            if not w in model: continue
            pred += choices(*list(zip(*list(model[w].items()))))
        txt += pred[-1]
    
    base = len(alph)
    self_info = log(len(kmers), base)
    total = float(sum(kmers.values()))
    probs = [v/total for v in kmers.values()]
    entropy = -sum([p*log(p, base) for p in probs])
    mut_info = self_info - entropy
    word_count = len(set(txt.split()) & words)
    with open(sys.argv[5], 'a') as f:
        f.write(str(iteration)+' '+str(mut_info)+' '+str(word_count)+'\n')
    print()
    print(txt)
    print(mut_info)
    print(word_count)
