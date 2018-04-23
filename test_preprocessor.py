import pytest
from preprocessor import preprocessor

def test_setup():
    assert(1 == 1)

def test_getTransformedStringCapitalShouldBeLowercase():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("HELLO")
    assert(transformed=="hello")

def test_getTransformedStringEmptyTextShouldBeEmpty():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("")
    assert(transformed=="")

def test_getTransformedStringMultipleWhiteSpaceShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("  juice46     say apple love coconut ")
    assert(transformed=="juice say apple love coconut")

def test_getTransformedStringNumbersShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("1324 969http")
    assert(transformed=="http")

def test_getTransformedStringWordsWithAnyLengthShouldNotBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("a b c d e f g hi jkl m n", 0)
    assert(transformed=="b c e f g hi jkl n")

def test_getTransformedStringWordsShorterThanThreeShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("ape zoo ok", 3)
    assert(transformed=="ape zoo")

def test_getTransformedStringPunctuationShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString(".?!, text")
    assert(transformed=="text")

def test_getTransformedStringEnglishStopwordsShouldBeRemoved():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("Don't tell me")
    assert(transformed=="tell")

def test_getTransformedStringLemmatizedLeavesShouldBeLeaf():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedString("leaves")
    assert(transformed=="leaf")

def test_getTransformedListLemmatizedLeavesShouldBeLeaf():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedList("leaves")
    assert(transformed==["leaf"])

def test_getTransformedListThreeWordsShouldAListOfThreeElements():
    preprocessorObj=preprocessor()
    transformed=preprocessorObj.getTransformedList("three sausage dogs")
    assert(transformed==["three", "sausage", "dog"])

