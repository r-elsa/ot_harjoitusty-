import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
       
    def test_luodun_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyjen_maukkaiden_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_myytyjen_edullisten_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_edullisten_lounaiden_osalta(self):
        kateismaksu = 1000
        res = self.kassapaate.syo_edullisesti_kateisella(kateismaksu)
        self.assertEqual(res, kateismaksu - 240 )

    def test_kateisosto_toimii_maukkaiden_lounaiden_osalta(self):
        katesismaksu = 10000
        res = self.kassapaate.syo_maukkaasti_kateisella(katesismaksu)
        self.assertEqual(res, katesismaksu - 400)

    def test_jos_kateismaksu_riittava_kassassa_rahamaara_kasvaa_edullisen_lounaan_hinnalla(self):
        katesimaksu = 250
        self.kassapaate.syo_edullisesti_kateisella(katesimaksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
    
    def test_jos_kateismaksu_riittava_kassassa_rahamaara_kasvaa_maukkaan_lounaan_hinnalla(self):
        kateismaksu = 500
        self.kassapaate.syo_maukkaasti_kateisella(kateismaksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)

    def test_jos_kateismaksu_riittava_edullisen_vaihtorahan_suuruus_oikea(self):
        kateismaksu = 1000
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(kateismaksu)
        self.assertEqual(vaihtoraha, kateismaksu - 240)

    def test_jos_kateismaksu_riittava_maukkaan_vaihtorahan_suuruus_oikea(self):
        kateismaksu = 1000
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(kateismaksu)
        self.assertEqual(vaihtoraha, kateismaksu - 400)
    
    def test_jos_kateismaksu_riittava_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        kateismaksu = 1000
        self.kassapaate.syo_edullisesti_kateisella(kateismaksu)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kateismaksu_riittava_myytyjen_maukkaiden_lounaiden_maara_kasvaa(self):
        kateismaksu = 1000
        self.kassapaate.syo_maukkaasti_kateisella(kateismaksu)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_kateismaksu__ei_ole_riittava_edullinen_lounas_kassassa_oleva_rahamaara_ei_muutu(self):
        kateismaksu = 230
        self.kassapaate.syo_edullisesti_kateisella(kateismaksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kateismaksu__ei_ole_riittava_maukas_lounas_kassassa_oleva_rahamaara_ei_muutu(self):
        kateismaksu = 390
        self.kassapaate.syo_maukkaasti_kateisella(kateismaksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_jos_kateismaksu_ei_ole_riittava_edullinen_lounas_kaikki_rahat_palautetaan_vaihtorahana(self):
        kateismaksu = 230
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(kateismaksu)
        self.assertEqual(vaihtoraha, kateismaksu)

    def test_jos_kateismaksu_ei_ole_riittava_maukas_lounas_kaikki_rahat_palautetaan_vaihtorahana(self):
        kateismaksu = 390
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(kateismaksu)
        self.assertEqual(vaihtoraha, kateismaksu)

    def test_jos_kateismaksu_ei_ole_riittava_myytyjen_edullisten_lounaiden_maarassa_ei_muutosta(self):
        kateismaksu = 230
        self.kassapaate.syo_edullisesti_kateisella(kateismaksu)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_kateismaksu_ei_ole_riittava_myytyjen_maukkaiden_lounaiden_maarassa_ei_muutosta(self):
        kateismaksu = 390
        self.kassapaate.syo_maukkaasti_kateisella(kateismaksu)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_jos_kortilla_on_tarpeeksi_rahaa_edullinen_veloitetaan_summa_kortilta(self):
        rahaa = 250
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, rahaa - 240)
        

    def test_jos_kortilla_on_tarpeeksi_rahaa_maukas_veloitetaan_summa_kortilta(self):
        rahaa = 500
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, rahaa - 400)

    def test_jos_kortilla_on_tarpeeksi_rahaa_edullinen_palautetaan_true(self):
        rahaa = 250
        maksukortti = Maksukortti(rahaa)
        palautus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(palautus, True)

    def test_jos_kortilla_on_tarpeeksi_rahaa_maukas_palautetaan_true(self):
        rahaa = 500
        maksukortti = Maksukortti(rahaa)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(palautus, True)


    def test_jos_kortilla_on_tarpeeksi_rahaa_edullinen_myytyjen_lounaiden_maara_kasvaa(self):
        rahaa = 250
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kortilla_on_tarpeeksi_rahaa_maukas_myytyjen_lounaiden_maara_kasvaa(self):
        rahaa = 500
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_edullinen_lounas_kortin_rahamaara_ei_muutu(self):
        rahaa = 230
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, rahaa)

    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maukas_lounas_kortin_rahamaara_ei_muutu(self):
        rahaa = 390
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, rahaa)

    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_edullinen_lounas_myytyjen_lounaiden_maara_muuttumaton(self):
        rahaa = 230
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maukas_lounas_myytyjen_lounaiden_maara_muuttumaton(self):
        rahaa = 390
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_edullinen_lounas_palautetaan_false(self):
        rahaa = 230
        maksukortti = Maksukortti(rahaa)
        palautus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(palautus, False)

    def test_jos_kortilla_ei_ole_tarpeeksi_rahaa_maukas_lounas_palautetaan_false(self):
        rahaa = 390
        maksukortti = Maksukortti(rahaa)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(palautus, False)


    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_ostettaessa_edullinen_lounas(self):
        rahaa = 250
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 )
    
    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_ostettaessa_maukas_lounas(self):
        rahaa = 500
        maksukortti = Maksukortti(rahaa)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 )

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        rahaa = 500
        maksukortti = Maksukortti(rahaa)
        summa = 100
        self.kassapaate.lataa_rahaa_kortille(maksukortti, summa)
        self.assertEqual(maksukortti.saldo, rahaa+summa )

    def test_kortille_rahaa_ladattaessa_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        rahaa = 500
        maksukortti = Maksukortti(rahaa)
        summa = 100
        self.kassapaate.lataa_rahaa_kortille(maksukortti, summa)
        self.assertEqual(self.kassapaate.kassassa_rahaa,  100000 + summa )
        


