print('\n----> MULTILEVEL INHERITENCE <----')
class Hewan:
    def bersuara(self):
        print('kucing bersuara')

class Kucing(Hewan):
    def Suara(self):
        print('meong...meong...meong')
    
class AnakKucing(Kucing):
    def minum(self):
        print('Minum susu')

ak = AnakKucing()

ak.bersuara()
ak.Suara()
ak.minum()