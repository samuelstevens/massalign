from massalign.core import *

file1 = '../newsela/corpora/truecased_corpus/orioles-alvarez.en.0.txt'
file2 = '../newsela/corpora/truecased_corpus/orioles-alvarez.en.1.txt'

model = TFIDFModel('../newsela/corpora/stop_words.txt')

aligner = VicinityDrivenParagraphAligner(similarity_model=model, acceptable_similarity=0.3)

m = MASSAligner()
p1s = m.getParagraphsFromDocument(file1)
p2s = m.getParagraphsFromDocument(file2)
alignments = m.getParagraphAlignments(p1s, p2s, aligner) 

print alignments
