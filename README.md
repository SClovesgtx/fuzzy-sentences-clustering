# phrases-fuzzy-clusters

Similar phrase clustering based on fuzzy-match.

## Purpose of the Package

Identify all groups/clursters of phrases based on their token sort ratio fuzzy similarity rate (clique [here](https://pypi.org/project/fuzzywuzzy/) to know more).

For a cluster to be formed, it needs to have at least two similar phrases, that is, if a sentence looks like at least with one other in the list, a cluster will be created for them, they will receive a positive number representing their cluster.

If the phrase does not look like any other, it will not be associated with any cluster and will receive the *-1* tag.

For while it works just for **portuguese** language.

## Installation

You can install it using pip:

```bash
pip install phrases_fuzzy_clusters
```

## Usage

```python
>>> from phrases_fuzzy_clusters import associate_cluster_per_phrase
>>> phrases = ["morava em florianópolis", "comprar um carro", "compra de um carro", "em florianópolis eu moro", "gosto de samba", "quero comer tapioca"]
>>> res = associate_cluster_per_phrase(phrases=phrases, similarity_threshold=90)
>>> print(res)
output: [('morava em florianópolis', 1), ('comprar um carro', 2), ('compra de um carro', 2), ('em florianópolis eu moro', 1), ('gosto de samba', -1), ('quero comer tapioca', -1)]
```

## Contribution

Contributions are welcome. 

If you find a bug, please let me know.

## Author

+ **Main Maintainer:** Cloves Paiva.
