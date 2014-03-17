"""
Utility functions for generating "lorem ipsum" Latin text.
"""

from __future__ import unicode_literals

import random

COMMON_P = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

WORDS = (
    'advanced',
    'ageless',
    'air-soft',
    'air-whipped',
    'all-day',
    'all-in-one',
    'all-natural',
    'anti-aging',
    'anti-inflammatory',
    'antimicrobial',
    'antioxidant-rich',
    'antiseptic',
    'aromatic',
    'beautiful',
    'beneficial',
    'best',
    'blendable',
    'botanical',
    'brilliant',
    'clarifying',
    'classic',
    'clean',
    'cleansing',
    'clump-free',
    'color-rich',
    'color-true',
    'concentrated',
    'conditioning',
    'continuous',
    'convenient',
    'cooling',
    'creamy',
    'crease-resistant',
    'daily',
    'deep',
    'deep-cleansing',
    'defining',
    'delicate',
    'dermatologist-recommended',
    'dermatologist-tested',
    'dramatic',
    'easily-applied',
    'easy',
    'easy-to-apply',
    'easy-to-use',
    'effective',
    'emollient',
    'enhancing',
    'enriched',
    'enriching',
    'environmentally friendly',
    'essential',
    'even-toned',
    'exceptional',
    'exclusive',
    'exfoliating',
    'extra',
    'facial',
    'fade-proof',
    'firm',
    'firmer',
    'firming',
    'flawless',
    'formulated',
    'fragrance-free',
    'fragrant',
    'fresh',
    'fresh-faced',
    'fuller',
    'fuss-free',
    'gentle',
    'gently',
    'glow-boosting',
    'gorgeous',
    'hand-milled',
    'healthy',
    'healthy-looking',
    'heavenly',
    'herbal',
    'high definition',
    'hydrating',
    'ideal',
    'illuminating',
    'immediate',
    'innovative',
    'instantly',
    'intense',
    'intensified',
    'intensive',
    'invigorating',
    'kissable',
    'lasting',
    'lengthening',
    'light',
    'lightweight',
    'line-diminishing',
    'long-lasting',
    'long-wearing',
    'lovely',
    'luminous',
    'luscious',
    'lush',
    'luxurious',
    'magical',
    'matte',
    'medicated',
    'medicinal',
    'microfine',
    'mineral-rich',
    'miraculous',
    'more even',
    'must-have',
    'natural',
    'natural-looking',
    'naturally',
    'nature',
    'no-shine',
    'non-greasy',
    'nourishing',
    'nutritive',
    'oil-free',
    'on-the-go',
    'ophthalmologist-tested',
    'organic',
    'outdoor',
    'overnight',
    'oxidant-rich',
    'perfecting',
    'personal',
    'plant-based',
    'plant-powered',
    'plumping',
    'powerful',
    'prescription-strength',
    'professional',
    'proven',
    'pure',
    'quick',
    'quick-absorbing',
    'quick-drying',
    'radiance-enhancing',
    'radiant',
    'recommended',
    'refreshed',
    'refreshing',
    'regenerating',
    'rehydrating',
    'remarkable',
    'renewed',
    'replenishing',
    'resilient',
    'restorative',
    'restructuring',
    'revitalizing',
    'revived',
    'rich',
    'satin-soft',
    'scientifically advanced',
    'sexy',
    'sheer',
    'shimmering',
    'signature',
    'silky',
    'simple',
    'skin cream',
    'sleek',
    'smear-proof',
    'smooth',
    'smoothing',
    'smudge-free',
    'smudge-resistant',
    'soft',
    'soothing',
    'sophisticated',
    'spa-inspired',
    'SPF',
    'stay-in-place',
    'strengthening',
    'striking',
    'styling',
    'suitable',
    'sun-kissed',
    'super-enriched',
    'supple',
    'tear-free',
    'therapeutic',
    'thicker',
    'toned',
    'ultra-conditioning',
    'ultra-emollient',
    'ultra-fine',
    'ultra-light',
    'unique',
    'velvety',
    'versatile',
    'vibrant',
    'visibly',
    'volumizing',
    'warming',
    'waterproof',
    'weightless',
    'worry-free',
    'younger-looking',
    'youth-enhancing',
    'youthful'
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
