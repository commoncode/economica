"""
Utility functions for generating "lorem ipsum" Latin text.
"""

from __future__ import unicode_literals

import random

COMMON_P = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

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

COMMON_WORDS = ('lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur',
        'adipisicing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt',
        'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua')


def sentence():
    """
    Returns a randomly generated sentence of lorem ipsum text.

    The first word is capitalized, and the sentence ends in either a period or
    question mark. Commas are added at random.
    """
    # Determine the number of comma-separated sections and number of words in
    # each section for this sentence.
    sections = [' '.join(random.sample(WORDS, random.randint(3, 12))) for i in range(random.randint(1, 5))]
    s = ', '.join(sections)
    # Convert to sentence case and add end punctuation.
    return '%s%s%s' % (s[0].upper(), s[1:], random.choice('?.'))


def paragraph():
    """
    Returns a randomly generated paragraph of lorem ipsum text.

    The paragraph consists of between 1 and 4 sentences, inclusive.
    """
    return ' '.join(sentence() for i in range(random.randint(1, 4)))


def paragraphs(count, common=True):
    """
    Returns a list of paragraphs as returned by paragraph().

    If `common` is True, then the first paragraph will be the standard
    'lorem ipsum' paragraph. Otherwise, the first paragraph will be random
    Latin text. Either way, subsequent paragraphs will be random Latin text.
    """
    paras = []
    for i in range(count):
        if common and i == 0:
            paras.append(COMMON_P)
        else:
            paras.append(paragraph())
    return paras


def words(count, common=True):
    """
    Returns a string of `count` lorem ipsum words separated by a single space.

    If `common` is True, then the first 19 words will be the standard
    'lorem ipsum' words. Otherwise, all words will be selected randomly.
    """
    if common:
        word_list = list(COMMON_WORDS)
    else:
        word_list = []
    c = len(word_list)
    if count > c:
        count -= c
        while count > 0:
            c = min(count, len(WORDS))
            count -= c
            word_list += random.sample(WORDS, c)
    else:
        word_list = word_list[:count]
    return ' '.join(word_list)
