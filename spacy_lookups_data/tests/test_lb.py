# coding: utf-8
from __future__ import unicode_literals

import pytest
from spacy.lang.lb import Luxembourgish


@pytest.fixture(scope="session")
def lb_nlp():
    return Luxembourgish()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("Dëscher", "Dësch"),
        ("engagéiers", "engagéieren"),
        ("goung", "goen"),
        ("neit", "nei"),
        ("déi", "déi"),
        ("Männer", "Mann"),
        ("Mënner", "Mond"),
        ("kritt", "kréien"),
    ],
)
def test_lb_lemmatizer_lookup_assigns(lb_nlp, string, lemma):
    tokens = lb_nlp(string)
    assert tokens[0].lemma_ == lemma
