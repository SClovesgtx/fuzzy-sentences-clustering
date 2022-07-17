from phrases_fuzzy_clusters import *


def test_associate_cluster_per_phrase():
    phrases = ["morava em florianópolis", "comprar um carro", "compra de um carro", "moro em florianópolis"]
    res = associate_cluster_per_phrase(phrases)
    assert res == [['morava em florianópolis', 1], ['comprar um carro', 2], ['compra de um carro', 2], ['moro em florianópolis', 1]]
