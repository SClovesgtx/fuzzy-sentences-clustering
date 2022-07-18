from fuzzy_sentences_clustering import *


def test_look_for_clusters():
    sentences = [
        "morava em florianópolis",
        "comprar um carro",
        "compra de um carro",
        "em florianópolis eu moro",
        "gosto de samba",
        "quero comer tapioca",
    ]
    res = look_for_clusters(sentences)
    assert res == [1, 2, 2, 1, -1, -1]
