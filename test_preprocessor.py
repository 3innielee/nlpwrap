import pytest
from preprocessor import preprocessor

def test_setup():
    assert(1 == 1)

def test_transformTextCapitalShouldBeLowercase():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("HELLO")
    assert(transformed=="hello")

def test_transformTextEmptyTextShouldBeEmpty():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("")
    assert(transformed=="")

def test_transformTextMultipleWhiteSpaceShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("  juice46     say apple love coconut ")
    assert(transformed=="juice say apple love coconut")

def test_transformTextNumbersShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("1324 969http")
    assert(transformed=="http")

def test_transformTextWordsWithAnyLengthShouldNotBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("a b c d e f g hi jkl m n", 0)
    assert(transformed=="b c e f g hi jkl n")

def test_transformTextWordsShorterThanThreeShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("ape zoo ok", 3)
    assert(transformed=="ape zoo")

def test_transformTextPunctuationShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText(".?!, text")
    assert(transformed=="text")

def test_transformTextEnglishStopwordsShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("Don't tell me")
    assert(transformed=="tell")

def test_transformTextLemmatizedLeavesShouldBeLeaf():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("leaves")
    assert(transformed=="leaf")