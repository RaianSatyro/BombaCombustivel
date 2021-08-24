import sys
sys.path.insert(1, 'C:/Users/Rio/Documents/code/BombaCombustivel') 

from src.model.BombaDeCombustivel import BombaCombustivel


def test_abastecimento():
    bomba1 = BombaCombustivel('Gasolina', 2.39, 140)
    print('____________________________')
    print(bomba1.abastecer_por_litro(20))

    print('____________________________')
    print(bomba1.abastecer_por_litro(50))
 
    print('____________________________')
    print(bomba1.abastecer_por_litro(15))

    print('____________________________')
    print(bomba1.abastecer_por_litro(30))

    print('____________________________')