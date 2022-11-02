import unittest

from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # Tästä eteenpäin uusia testejä

    def test_luotavan_varaston_tilavuus_ei_voi_olla_negatiivinen(self):
        huonovarasto = Varasto(-1)

        self.assertAlmostEqual(huonovarasto.tilavuus, 0.0)

    def test_luotavan_varaston_saldo_ei_voi_olla_negatiivinen(self):
        huonovarasto = Varasto(1, -1)

        self.assertAlmostEqual(huonovarasto.saldo , 0.0)

    def test_alkusaldo_ei_voi_olla_suurempi_kuin_tilavuus(self):
        huonovarasto = Varasto(1, 2)

        self.assertAlmostEqual(huonovarasto.saldo , 1)

    def test_varastoon_ei_voi_lisätä_negatiivista_maaraa(self):
        saldo_alussa = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(saldo_alussa, self.varasto.saldo)

    def test_varastoon_ei_voi_lisata_enempaa_kuin_sinne_mahtuu(self):

        self.varasto.lisaa_varastoon(125342653456)
        self.assertAlmostEqual(self.varasto.tilavuus ,self.varasto.saldo)
    
    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        saldo_alussa = self.varasto.saldo
        negatiivinen = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(negatiivinen, 0)
        self.assertAlmostEqual(saldo_alussa, self.varasto.saldo)

    def test_varastosta_ei_voi_ottaa_enempaa_kuin_siella_on(self):
        saldo_alussa = self.varasto.saldo
        liikaa = self.varasto.ota_varastosta(saldo_alussa +9001)
        self.assertAlmostEqual(liikaa, saldo_alussa)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_varasto_tulostuu_oikein(self):
        oletustuloste= f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        mita_tulostuu = self.varasto.__str__()

        self.assertEqual(oletustuloste, mita_tulostuu)