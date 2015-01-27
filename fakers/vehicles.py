# -*- coding: latin-1 -*-

from . import lorem_ipsum


WORDS = (
    '2 doors',
    '2 places',
    '4 doors',
    'aerodynamic',
    'big',
    'black',
    'blue',
    'classic',
    'convertible',
    'coupe',
    'economic',
    'expensive',
    'fast',
    'golden',
    'good',
    'gray',
    'green',
    'hp',
    'km/h',
    'light brown',
    'muscle',
    'new',
    'performance',
    'powerful',
    'red',
    'resistant',
    'rpm',
    'secure',
    'shiny',
    'silver',
    'slow',
    'small',
    'sport',
    'strong',
    'used',
    'white pearl',
    'white',
    'yellow'
)


def paragraphs(*args, **kwargs):
    return lorem_ipsum.paragraphs(*args, words=WORDS, **kwargs)


def words(*args, **kwargs):
    return lorem_ipsum.words(*args, words=WORDS, **kwargs)
