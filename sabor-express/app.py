
import os

lista_de_restaurantes = ['Pizza Rut', 'Burguer Viking', 'Mc donals', 'Subwayy',]
#funçõe precisam ser declaradas no começo do código
# function -> def
def voltar_ao_menu_principal():
      input("\nPressione qualquer tecla para retornar ao menu principal...")
      main()


def finalizar_programa():
      os.system("cls")
      print("programa finalizado com sucesso!")
       

def exbir_nome():
      #"print", tem a mesma função que sua tradução, que é de fato inprimir algo
      print ("ⓢ ⓐ ⓑ ⓞ ⓡ   ⓔ ⓧ ⓟ ⓡ ⓔ ⓢ ⓢ ☕\n")
      print ("para prosseguirmos escolha a opção que melhor te atende:\n")

def escolher_opcao():
      #"input", é utilizado para receber uma entrada do usuário

      #"int", como meu padrão de entrada é reconhecido como string, eu utilizo o 
      #"int" para converter a entrada em número inteiro
      print("""
      1. Cadastra restaurante
      2. Listar restaurantes
      3. Avaliar restaurante
      4. Sair\n
      """)

def opcao_invalida():
      print("Opção inválida, por favor escolha uma opção válida!")
      input("pressione qualquer tecla para continuar...")
      main()

#1
def cadastrar_restaurante():
      os.system("cls")
      print("Vamos começar a cadastrar um restaurante!")
      nome_do_restaurante = input("digite o nome do restaurante: \n")
      lista_de_restaurantes.append(nome_do_restaurante)
      print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
      voltar_ao_menu_principal()

#2
def listar_restaurantes():
      os.system("cls")
      print("Lista de restaurantes cadastrados:\n")
      for restaurante in lista_de_restaurantes:
            print(f"- {restaurante}")
      voltar_ao_menu_principal()



def opcao_respondida():
      try:
            opcao_escolhida = int(input("Digite o número da opção desejada: "))

            #if, elif e else, são utilizadas para criar condições no código
            #afim de satisfazer diferentes necessidades
            if opcao_escolhida == 1:
                        print("Você escolheu cadastras um restaurante!")
                        cadastrar_restaurante()
            elif opcao_escolhida == 2:
                        print("Você escolheu listar resutarantes!")
                        listar_restaurantes()
            elif opcao_escolhida == 3:
                        print("Você escolheu avaliar um restaurante!")
            elif opcao_escolhida == 4:
                  finalizar_programa()
            else:
                  opcao_invalida()
      except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            input("pressione qualquer tecla para continuar...")
            main()



def main():
      os.system("cls")
      exbir_nome()
      escolher_opcao()
      opcao_respondida()


if  __name__ == "__main__":
      main()

# O código acima se trata de uma váriavel especial.
# De uma forma breve, essa variável codiciona verifica a execução do código,
# No entanto eu não posso importar essa parte do meu cóigo para outros arquivos.







