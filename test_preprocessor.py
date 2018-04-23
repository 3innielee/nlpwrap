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
    assert(transformed=="juice46 says apple loves coconut")
