from varasto import Varasto

def test_nega_tilavuus():
    v = Varasto(-10)
    assert v.tilavuus == 0
    assert v.saldo == -10
    assert v.paljonko_mahtuu() == 10

def test_oletussaldo():
    v = Varasto(10)
    assert v.saldo == 0
    assert v.paljonko_mahtuu() == 10

def test_alkusaldo_negatiivinen():
    v = Varasto(10, -5)
    assert v.saldo == 0
    assert v.tilavuus == 10
    assert v.paljonko_mahtuu() == 10

def test_alkusaldo_yli_tilavuuden():
    v = Varasto(10, 50)
    assert v.saldo == 10
    assert v.paljonko_mahtuu() == 0

def test_lisaa_normaalisti():
    v = Varasto(10)
    v.lisaa_varastoon(4)
    assert v.saldo == 4
    assert v.paljonko_mahtuu() == 6

def test_lisaa_liikaa():
    v = Varasto(10)
    v.lisaa_varastoon(15)
    assert v.saldo == 10
    assert v.paljonko_mahtuu() == 0

def test_lisaa_negatiivinen():
    v = Varasto(10)
    v.lisaa_varastoon(-2)
    assert v.saldo == 0
    assert v.paljonko_mahtuu() == 10

def test_ota_normaalisti():
    v = Varasto(10)
    v.lisaa_varastoon(8)
    otettu = v.ota_varastosta(3)
    assert otettu == 3
    assert v.saldo == 5
    assert v.paljonko_mahtuu() == 5

def test_ota_liikaa():
    v = Varasto(10)
    v.lisaa_varastoon(6)
    otettu = v.ota_varastosta(20)
    assert otettu == 6
    assert v.saldo == 0
    assert v.paljonko_mahtuu() == 10

def test_ota_negatiivinen():
    v = Varasto(10)
    v.lisaa_varastoon(5)
    otettu = v.ota_varastosta(-2)
    assert otettu == 0
    assert v.saldo == 5
    assert v.paljonko_mahtuu() == 5

def test_negsaldo_nollatilavuus():
    v = Varasto(0)
    v.saldo = -5
    otettu = v.ota_varastosta(2)
    assert otettu == -5
    assert v.saldo == 0
    assert v.paljonko_mahtuu() == 0

def test_str():
    v = Varasto(10)
    v.lisaa_varastoon(4)
    s = str(v)
    assert "saldo = 4" in s
    assert "vielä tilaa 6" in s
