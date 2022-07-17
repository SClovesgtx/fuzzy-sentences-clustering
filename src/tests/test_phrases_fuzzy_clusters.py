from phrases_fuzzy_clusters import *


def test_associate_cluster_per_phrase():
    phrases = [
        "morava em florianópolis",
        "comprar um carro",
        "compra de um carro",
        "em florianópolis eu moro",
        "gosto de samba",
        "quero comer tapioca",
    ]
    res = associate_cluster_per_phrase(phrases)
    assert res == [
        ("morava em florianópolis", 1),
        ("comprar um carro", 2),
        ("compra de um carro", 2),
        ("em florianópolis eu moro", 1),
        ("gosto de samba", -1),
        ("quero comer tapioca", -1),
    ]
