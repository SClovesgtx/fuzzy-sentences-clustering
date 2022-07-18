# fuzzy-sentences-clustering

Clustering similar sentences based on their fuzzy similarity.

## Purpose of the Package

There are some popular algorithms on the market for mining topics in a textual set, such as [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation), but they don't work very well for a small set of data, let's say a thousand sentences for example.

This package tries to solve this for a small dataset by making the following naive assumption:

"If I remove all the stopwords between two sentences, extract the stems of their words and after that find similar phrases between these sentences, they are probably talking about the same subject."

The interest here is to form groups with at least two similar sentences, isolated sentences (sentences that don't look like any other in the total set) will not generate a cluster just for them. For these cases, the sentence will receive the *-1* tag.

For while it works just for **portuguese** language.

## Installation

You can install it using pip:

```bash
pip3 install phrases-fuzzy-clusters
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
