### (X) Verificar se tem combustivel no estoque
### (X) Abastecimento do estoque da bomba. 
### ( ) Colocar um dicinario com tipo de combustivel, preço e quat de estoque.
### ( ) Relatorio de estoque e vendas do dia.
### ( ) Mensagem de estoque minimo de combustivel (acabou o estoque).
### ( ) Controle e menutenção da bomba.


class BombaCombustivel():
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel, capacidade_estoque = 10000):
        self.tipo_combustivel = tipo_combustivel
        self.__valor_litro = float(valor_litro)
        self.__quantidade_combustivel = float(quantidade_combustivel)
        self.__capacidade_estoque = capacidade_estoque


    # método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    def abastecer_por_valor(self, valor):
        qnt_litro_abastecido = valor / self.__valor_litro

        if self.__verifica_reservatorio(qnt_litro_abastecido):
            self.__alterar_quantidade_combustivel(qnt_litro_abastecido)
            return f'{qnt_litro_abastecido:.2f} litros'
        else:
            print('Combústivel insuficiente')
    
    #método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    def abastecer_por_litro(self, qnt_litro):
        if self.__verifica_reservatorio(qnt_litro):
            total = self.__valor_litro * qnt_litro
            self.__alterar_quantidade_combustivel(qnt_litro)
            return f'R${total:.2f}'
    

    #altera o valor do litro do combustível.
    def alterar_valor(self, novo_valor):
        self.valor_litro = float(novo_valor)


    #altera o tipo do combustível.
    def alterar_combustivel(self, tp_combustivel):
        self.tipo_combustivel = str(tp_combustivel)
    

    #altera a quantidade de combustível restante na bomba.
    def __alterar_quantidade_combustivel(self, saida_combustivel):
        self.__quantidade_combustivel -= saida_combustivel

    
    def __verifica_reservatorio(self, litros):
        return litros <= self.__quantidade_combustivel


    def abastecer_reservatorio(self, qnt_entrada):
        limite = self.__capacidade_estoque - self.__quantidade_combustivel
        
        if qnt_entrada <= limite:
            self.__quantidade_combustivel += qnt_entrada
            print('Abastecendo')
            
        else:
            print(f'Não é possivél abastecer, a capacidade maxima atual é de {limite}')

        
