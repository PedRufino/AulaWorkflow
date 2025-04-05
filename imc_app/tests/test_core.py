from core.imc import calcular, classificar

def test_calcular_imc():
    assert calcular(70, 1.75) == 22.86 # IMC esperado para peso 70kg e altura 1.75m

def test_classificar_imc():
    assert classificar(22.86) == "Peso normal"
    assert classificar(17.0) == "Abaixo do peso"
    assert classificar(26.0) == "Sobrepeso"
    assert classificar(30.0) == "Obesidade"