# -*- coding: latin-1 -*-

from . import lorem_ipsum


WORDS = (
    'Access',
    'Acrobat Distiller',
    'Acrobat Pro',
    'Adobe',
    'AIR',
    'ArcGIS',
    'Bridge',
    'Citrix Virtual Desktop',
    'DPGraph',
    'Dreamweaver',
    'Excel',
    'ExtendScript Toolkit',
    'FineReader',
    'Fireworks',
    'Flash Builder',
    'Flash Player',
    'Google Chrome',
    'Google SketchUp',
    'Histology',
    'Illustrator',
    'InDesign',
    'InfoPath',
    'iTunes',
    'Java',
    'JAWS',
    'JCreator LE',
    'Maple',
    'Matlab',
    'Microsoft'
    'Minitab',
    'Mozilla Firefox',
    'NetBeans IDE',
    'OneNote',
    'OpenBUGS',
    'Outlook',
    'Photoshop',
    'PowerPoint',
    'Premiere Pro',
    'Publisher',
    'Pymol',
    'QuickTime Player',
    'R for Windows',
    'Reader',
    'Respondus LockDown Browser',
    'SAS',
    'Shockwave Player',
    'SPSS',
    'Stata',
    'TeXnicCenter',
    'TurningPoint',
    'UMedic',
    'VLC Video Player',
    'Wolfram Mathematica',
    'Word',
    'Write-N-Cite Word plug-in',
    'WS_FTP Professional',
    'ZoomText'
)


def paragraphs(*args, **kwargs):
    return lorem_ipsum.paragraphs(*args, words=WORDS, **kwargs)


def words(*args, **kwargs):
    return lorem_ipsum.words(*args, words=WORDS, **kwargs)
