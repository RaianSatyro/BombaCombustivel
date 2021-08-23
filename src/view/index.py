import sys
sys.path.append('C:/Users/rayan/Documents/Dev/devSenai/Poo') 

from src.model.BombaDeCombustivel import BombaCombustivel


def test_abastecimento():
    bomba1 = BombaCombustivel('Gasolina', 2.39, 9700)
    print('____________________________')
    print(bomba1.abastecer_reservatorio(297))
    print(bomba1._BombaCombustivel__quantidade_combustivel)
    print('____________________________')
    