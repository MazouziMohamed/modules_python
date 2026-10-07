from math import sqrt
def somme(note1, note2, note3, note4, note5) :
    return note1+note2+note3+note4+note5
def moyenne(note1, note2, note3, note4, note5) :
    return (note1+note2+note3+note4+note5) / 5
def variance(note1, note2, note3, note4, note5) :
    moy = moyenne(note1, note2, note3, note4, note5)
    return ((note1-moy)**2 + (note2-moy)**2 + (note3-moy)**2 + (note4-moy)**2 + (note5-moy)**2) / 5
def ecart_type(note1, note2, note3, note4, note5) :
    return sqrt(variance(note1, note2, note3, note4, note5))
def coefficient_variation(note1, note2, note3, note4, note5) :
    return (ecart_type(note1, note2, note3, note4, note5) / moyenne(note1, note2, note3, note4, note5)) * 100