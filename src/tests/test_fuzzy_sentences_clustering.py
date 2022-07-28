from fuzzy_sentences_clustering import *
from fuzzy_sentences_clustering import __version__


def test_check_version():
    assert __version__ == "1.1.2"


def test_look_for_clusters_en():
    sentences = [
        "I live in New York",
        "I want to buy a car",
        "a car I would like to buy",
        "Ohh New York, I lived there in 2005",
        "I have a dog",
    ]
    res = look_for_clusters(sentences, similarity_threshold=60)
    assert res == [1, 2, 2, 1, -1]


def test_look_for_clusters_ger():
    sentences = [
        "ich lebe in New York",
        "Ich möchte ein Auto kaufen",
        "ein Auto, das ich kaufen möchte",
        "Oh New York, Ich habe dort 2005 gelebt",
        "Ich habe einen Hund",
    ]
    res = look_for_clusters(
        sentences, language="german", method="token_set_ratio", similarity_threshold=80
    )
    assert res == [1, 2, 2, 1, -1]
