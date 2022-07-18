fuzzy-sentences-clustering
==========================

Clustering similar sentences based on their fuzzy similarity.

Purpose of the Package
----------------------

There are some popular algorithms on the market for mining topics in a
textual set, such as
`LDA <https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation>`__, but
they don’t work very well for a small set of data, let’s say a thousand
sentences for example.

This package tries to solve this for a small dataset by making the
following naive assumption:

   *If I remove all
   the *\ `stopwords <https://en.wikipedia.org/wiki/Stop_word>`__\ * between
   two sentences, extract
   the *\ `stems <https://en.wikipedia.org/wiki/Stemming>`__\ * of their
   words, sort their words and after that find similar phrases
   (intersection) between these two sentences, they are probably talking
   about the same, or similar, subject.*

The goal here is to form clusters/groups with at least two similar
sentences, isolated sentences (sentences that don’t look like any other
in the total set) will not generate a cluster just for them. For these
cases, the sentence will receive the *-1* tag.

For while it works just for **portuguese** language.

Installation
------------

You can install it using pip:

.. code:: bash

   pip3 install fuzzy-sentences-clustering

Usage
-----

.. code:: python

   >>> from fuzzy_sentences_clustering import look_for_clusters
   >>> sentences = ["morava em florianópolis", "comprar um carro", "compra de um carro", "em florianópolis eu moro", "gosto de samba", "quero comer tapioca"]
   >>> res = look_for_clusters(sentences=sentences, similarity_threshold=90)
   >>> print(res)
   output: [1, 2, 2, 1, -1, -1]

Contribution
------------

Contributions are welcome.

If you find a bug, please let me know.

Author
------

`Cloves Paiva <https://www.linkedin.com/in/cloves-paiva-02b449124/>`__.
