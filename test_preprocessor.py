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
    transformed=preprocessorObj.transformText("  juice46     says apple loves coconut ")
    assert(transformed=="juice says apple loves coconut")

def test_transformTextNumbersShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("1324 969https")
    assert(transformed=="https")

def test_transformTextWordsWithAnyLengthShouldNotBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("a b c d e f g hi jkl m n", 0)
    assert(transformed=="b c e f g hi jkl n")

def test_transformTextWordsShorterThanThreeShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.transformText("apes zoo ok", 3)
    assert(transformed=="apes zoo")

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