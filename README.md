# Introduction:

**MASSAlign** is a *Python 2* library for the alignment and annotation of comparable documents.
It offers **3** main functionalities:

* Paragraph-level alignment between comparable documents
* Sentence-level alignment between comparable paragraphs or documents
* Word-level annotation of modification operations between aligned sentences

**MASSAlign** uses a technique called *vicinity-driven alignment*, described here:

> Gustavo H. Paetzold and Lucia Specia. **Vicinity-Driven Paragraph and Sentence Alignment for Comparable Corpora**. arXiv preprint arXiv:1612.04113.

**MASSAlign** is excellent for extracting simplifications from complex/simple parallel documents!
These papers are evidence:

> Gustavo H. Paetzold and Lucia Specia. **Lexical Simplification with Neural Ranking**. Proceedings of the 2017 EACL.
> Fernando Alva-Manchego, Joachim Bingel, Gustavo H. Paetzold, Carolina Scarton and Lucia Specia. **Learning how to Simplify from Explicit Labeling of Complex-Simplified Text Pairs**. Proceedings of the 2017 IJCNLP.

# Installation:

To install MASSAlign, you must:

1. Download and unpack the LEXenstein's [latest release](https://github.com/ghpaetzold/LEXenstein/releases/latest).
2. Navigate to the root folder.
3. Run the following command line:

```
python setup.py install
```

# Documentation:

MASSAlign's documentation can be found [here](http://ghpaetzold.github.io/massalign_docs).

# Examples:

You can learn how to use MASSAlign [here](http://ghpaetzold.github.io/massalign_docs/examples.html).