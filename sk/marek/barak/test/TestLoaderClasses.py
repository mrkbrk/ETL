'''
Created on Dec 14, 2012

@author: marek
INTEGRACNE TESTY
'''

import unittest
from sk.marek.barak.app.DatabaseLoader import *


class TestZamestnanecLoader(unittest.TestCase):
    #@unittest.skip("Skip zam test")
    def testZamLoad(self):
        print "Zam loader test"
        dbLoader = Dim_ZamestanecLoader()
        l = list()
        l.append("Marek")
        l.append("Barak")
        l.append("Programator")
        l.append(1)
        l.append("mrk.barak@gmail.com")
        rows = list()
        s=list()
        s.append("Jaroslav")
        s.append("Hoblak")
        s.append("Ozran")
        s.append(1)
        s.append("jaroslav.hoblak@gmail.com")
        rows.append(l)
        rows.append(s)
        #dbLoader.load(rows)
        print dbLoader.getKey()
        
    @unittest.skip("Skip Dod test")
    def testDodLoader(self):
        print "Dod loader test"
        dbLoader = Dim_DodavatelLoader()
        l = list()
        l.append("Prvy")
        l.append("Prve miesto")
        l.append("123456789/4587")
        l.append("12345678")
        s = list()
        s.append("Second")
        s.append("Druhe miesto")
        s.append("987654321/3216")
        s.append("98765432")
        row = list()
        row.append(l)
        row.append(s)
        dbLoader.load(row)
        
    @unittest.skip("Already tested")
    def testCasLoad(self):
        print "CAS load Test"
        dbLoad = Dim_CasLoader()
        l = list()
        s = list()
        l.append("2012")
        l.append("5")
        l.append("4")
        s.append("2011")
        s.append("12")
        s.append("13")
        row = list()
        row.append(s)
        row.append(l)
        dbLoad.load(row)
        
    @unittest.skip("Already tested")
    def testTovarLoader(self):
        dbLoader = DimTovarLoader()
        l = list()
        l.append("Kategoria Horor")
        l.append("Nazov T Kniha")
        l.append("Platforma 1")
        l.append("Mutacia CZE")
        l.append(600)
        l.append("1.12.2012")
        l.append("Marek Barak")
        l.append("Slov art")
        l.append("Volaco hlupeho")
        l.append("Prve ISBN")
        l.append(1525.5)
        l.append(18)
        row = list();
        row.append(l)
        s= list(l)
        row.append(s)
        dbLoader.load(row)
        
    @unittest.skip("Already tested")
    def testZakaznikLoader(self):
        l = list()
        l.append("Pravnicka osoba")
        l.append("SRO")
        l.append("Vydaj sro")
        l.append("Kovacova 21")
        l.append("Namestovo")
        l.append("0915126544")
        l.append("vydaj@zmrd.sk")
        l.append("123554478/8547")
        l.append("12345678")
        l.append("DCSD")
        s = list(l)
        row = list()
        row.append(l)
        row.append(s)
        dbLoader = DimZakaznikLoader()
        dbLoader.load(row)
        
    @unittest.skip("Already tested")
    def testPobockaLoader(self):
        l = list()
        l.append(1)
        l.append("Nove Zamky")
        l.append("Nitriansky")
        l.append("Nitriansky")
        l.append("Komarnanska 29")
        l.append("0915126544")
        l.append(1)
        l.append("mrk.barak@gmail.com")
        s = list(l)
        row = list()
        row.append(l)
        row.append(s)
        dbLoader = DimPobockaLoader()
        dbLoader.load(row)
        
    @unittest.skip("Already tested")
    def testFakturaLoader(self):
        l = list()
        l.append("ano")
        l.append("nie")
        l.append("ano")
        s = list(l)
        row = list()
        row.append(l)
        row.append(s)
        dbLoader= DimFakturaLoader()
        dbLoader.load(row)
        
    #@unittest.skip("Already tested")
    def testSluzbyZakaznikomLoader(self):
        l = list()
        l.append(2)
        l.append(1)
        l.append(1)
        l.append(1)
        l.append(1)
        l.append("Blby popis")
        l.append("Text_dotazu")
        l.append("Text_odpovede")
        l.append("ano")
        row = list()
        row.append(l)
        dbLoader = FaktSluzbyZakaznikomLoader()
        print "KEYS "
        print dbLoader.getKey()
        #dbLoader.load(row)
        
    @unittest.skip("Already tested")
    def testFaktSkladLoader(self):
        d=list()
        d.append(2)
        d.append(1)
        d.append(1)
        d.append(1)
        d.append(30)
        d.append("dostupne")
        l=list()
        l.append(1)
        l.append(1)
        l.append(1)
        l.append(1)
        l.append(30)
        l.append("dostupne")
        row =list()
        row.append(l)
        row.append(d)
        dbLoader = FaktSkladLoader()
        dbLoader.load(row)
    @unittest.skip("Already tested")
    def testFaktObjednavkaLoader(self):
        d = list()
        d.append(1)
        d.append(1)
        d.append(1)
        d.append(1)
        d.append(1)
        d.append(200)
        d.append("ano")
        d.append("Blbost")
        d.append("kurier")
        d.append("online")
        d.append("prijata")
        l = list()
        l.append(2)
        l.append(1)
        l.append(1)
        l.append(1)
        l.append(1)
        l.append(200)
        l.append("ano")
        l.append("Blbost")
        l.append("posta")
        l.append("online")
        l.append("pripravena na expediciu")
        row = list()
        row.append(l)
        row.append(d)
        dbloader = FaktObjednavkaLoader()
        dbloader.load(row)
    @unittest.skip("Already tested")
    def testDodavkaLoader(self):
        d= list()
        d.append(1)
        d.append(1)
        d.append(1)
        d.append(1)
        d.append("Poznamka 1")
        d.append(25)
        l= list()
        l.append(2)
        l.append(1)
        l.append(1)
        l.append(1)
        l.append("Poznamka 2")
        l.append(30)
        row = list()
        row.append(l)
        row.append(d)
        dbLoader = FaktDodavkaLoader()
        dbLoader.load(row)
    @unittest.skip("Already tested")
    def testReklamaciaLoader(self):
        d = list()
        d.append(1)
        d.append(1)
        d.append(1)
        d.append("Popis chyby 1")
        d.append("ano")
        d.append("ano")
        d.append("Zdovodnenie 1")
        d.append(5)
        l = list()
        l.append(2)
        l.append(1)
        l.append(1)
        l.append("Popis chyby 2")
        l.append("nie")
        l.append("ano")
        l.append("Zdovodnenie 2")
        l.append(2)
        row = list()
        row.append(d)
        row.append(l)
        dbLoader= FaktReklamaciaLoader()
        dbLoader.load(row)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()