from src.model.BombaDeCombustivel import BombaCombustivel


def test_abastecimento():
    bomba1 = BombaCombustivel('Gasolina', 2.39, 140)

 
    print(f'''
    ________________________________________________________

    {bomba1.abastecer_por_litro(100)}
    Estoque restante: {bomba1.quantidade_combustivel} litros 
    ________________________________________________________
    
    {bomba1.abastecer_reservatorio(480)}  
    ________________________________________________________    
    
    {bomba1.abastecer_por_valor(20)}
    Estoque restante: {bomba1.quantidade_combustivel} litros 

    ''')

    