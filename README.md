# fuzzy-sentences-clustering

Clustering similar sentences based on their fuzzy similarity.

For the word stem extractor I am using [Snowball stemmers](https://www.nltk.org/api/nltk.stem.snowball.html#:~:text=The%20following%20languages%20are%20supported,%2C%20Russian%2C%20Spanish%20and%20Swedish.) from NLTK library. So the following languages are supported: 

* Arabic 
* Danish 
* Dutch 
* English
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish 
* Swedish

## Purpose of the Package

There are some popular algorithms on the market for mining topics in a textual set, such as [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation), but they don't work very well for a small set of data, let's say a thousand sentences for example.

This package tries to solve this for a small dataset by making the following naive assumption:

> *If I remove all the stopwords, get the stems from words and after that these sentences become similar, they are probably talking about the same, or similar, subject.*

The goal here is to form clusters/groups with at least two similar sentences, isolated sentences (sentences that don't look like any other in the total set) will not generate a cluster just for them. For these cases, the sentence will receive the *-1* tag.

## Usage

You can choose more than one method to compare the similarity between sentences:

* ratio
* partial_ratio
* token_sort_ratio (the default one)
* token_set_ratio

To know more about these methods click [here](https://pypi.org/project/fuzzywuzzy/).

```python
>>> from fuzzy_sentences_clustering import look_for_clusters
>>> eng_sentences = [
        "I live in New York",
        "I want to buy a car",
        "a car I would like to buy",
        "Ohh New York, I lived there in 2005",
        "I have a dog",
    ]
>>> ger_sentences = [
        "ich lebe in New York",
        "Ich möchte ein Auto kaufen",
        "ein Auto, das ich kaufen möchte",
        "Oh New York, Ich habe dort 2005 gelebt",
        "Ich habe einen Hund",
    ]
>>> look_for_clusters(eng_sentences, similarity_threshold=60)
output: [1, 2, 2, 1, -1]
>>> look_for_clusters(ger_sentences, language="german", method="token_set_ratio", similarity_threshold=80)
output: [1, 2, 2, 1, -1]
```

## Contribution

Contributions are welcome. 

If you find a bug, please let me know.

## Author

[Cloves Paiva](https://www.linkedin.com/in/cloves-paiva-02b449124/).
