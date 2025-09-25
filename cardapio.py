class ComidaMerenda:
    def __init__(self, nome):
        # define os atributos do objeto
        self.nome = nome

    def __str__(self):
        # define como o objeto será exibido quando for impresso
        return f"{self.nome}"

class Cardapio:
    def __init__(self, data):
        # uma data e uma lista para a foods do dia
        self.data = data
        self.comida_do_dia = []
    
    def adicionar_item(self, comida):
        # Ese método adiciona um objeto da classe ItemMerenda a listaa do cardápio
        self.comida_do_dia.append(comida)
        print(f"'{comida.nome}' foi adicionado ao cardapio de {self.data}.")
        
    def remover_comida(self, nome_comida):
        # Remove um item do cardápio
        comida_removida = None
        for comida in self.comida_do_dia:
                self.comida_do_dia.remove(comida)
                comida_removida = comida
                break
        
        if comida_removida:
            print(f"'{nome_comida}' foi removido do cardápio do dia {self.data}.")
        else:
            print(f"Erro: '{nome_comida}' não encontrado no cardápio do dia {self.data}.")

    def mostrar_cardapio(self):
        # Exibe o cardápio completo
        print(f"Cardápio do dia: {self.data}")
        
        if not self.comida_do_dia:
            print("Nenhum merenda para este dia.")
        else:
            for comida in self.comida_do_dia:
                print(f"- {comida}")

# Cria objetos da classe comidaMerenda
arroz = ComidaMerenda("Arroz")
feijao = ComidaMerenda("Feijão")
carne = ComidaMerenda("Carne")
suco = ComidaMerenda("Suco")
salada = ComidaMerenda("Salada")

#  Cria um objeda classe Cardapio
cardapio_hoje = Cardapio("23/09/2025")

# Usa os metodos para construir o cardapio do di
cardapio_hoje.adicionar_comida(arroz)
cardapio_hoje.adicionar_comida(feijao)
cardapio_hoje.adicionar_comida(carne)
cardapio_hoje.adicionar_comida(suco)
cardapio_hoje.adicionar_comida(salada)

# mostra o cardápio
cardapio_hoje.mostrar_cardapio()
