# Faça um programa que leia uma sequência de nomes de alunos de uma turma, terminada por "FIM", além de suas duas notas (entre 0 e 10).
# Para cada aluno, o programa deve informar:
# Média do aluno
# Se o aluno está aprovado ou em prova final (Média ≥ 6 = Aprovado).
# Ao final, o programa deve mostrar a média geral da turma.
# Utilize a função de arredondamento para exibir as médias.
# Implemente as funções:
# Entrada do nome e das notas.
# Cálculo da média do aluno.
# Cálculo da média da turma.

from math import ceil

lista_de_alunos = []

class Alunos:
    """
        Classe para representar um aluno.

        Atributos:
        _id (int): Identificador único do aluno.
        nome (str): Nome completo do aluno.
        nota1 (float): Primeira nota do aluno.
        nota2 (float): Segunda nota do aluno.
        media (float): Média das notas do aluno.
        status (str): Status do aluno (Aprovado ou Prova final).
    """
    _id = 1
    def __init__(self, nome, nota1, nota2):
        """
            Construtor da classe Alunos.

            Args:
                nome (str): Nome do aluno.
                nota1 (float): Primeira nota.
                nota2 (float): Segunda nota.
        """
        self.id=Alunos._id
        Alunos._id +=1
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0
        self.status = ""

    def salvar_aluno(self):
        """Adiciona o aluno à lista global de alunos."""
        lista_de_alunos.append(self)

    def salvar_media(self,media):
        """ Define a média do aluno.

            Args:
                media (float): A média calculada.
        """
        self.media = media
    
    def avaliar_status(self):
        """Avalia o status do aluno com base na média."""
        if(self.media>=6):
            self.status = "Aprovado"
        else:
            self.status = "Prova final"

def entrada_nome_e_notas():
    """
        Solicita o nome e as duas notas de um aluno, validando os dados.

        Retorna:
            dict: Um dicionário contendo o nome, a primeira nota e a segunda nota do aluno.
    """
    while True:
        nome = input("Digite o nome do aluno: ")
        if nome.strip() == "":
            print("O nome não pode ser vazio.")
        elif not nome.isalpha():
            print("O nome deve conter apenas letras.")
        else:
            break

    while True:
        try:
            nota1 = float(input("Digite a primeira nota do aluno (0 a 10): "))
            if 0 <= nota1 <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um valor numérico válido.")

    while True:
        try:
            nota2 = float(input("Digite a segunda nota do aluno (0 a 10): "))
            if 0 <= nota2 <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um valor numérico válido.")

    return{
        "nome":nome,
        "nota1":nota1,
        "nota2":nota2
    }

def criar_aluno():
  """
    Cria novos alunos e os adiciona à lista de alunos global.

    Permite ao usuário inserir os dados de um ou mais alunos. A entrada é encerrada quando
    o usuário digita "FIM".
  """
  msg_inicial = input("Deseja adicionar um aluno (digite FIM para encerrar)? ")
  if(msg_inicial.upper()=="FIM"):
    aluno = Alunos(msg_inicial, 0, 0)
    aluno.salvar_aluno()
  while(msg_inicial.upper()!="FIM"):
    dados_aluno =  entrada_nome_e_notas()
    aluno = Alunos(dados_aluno["nome"], dados_aluno["nota1"], dados_aluno["nota2"])
    aluno.salvar_aluno()
    msg_inicial = input("Deseja adicionar mais um aluno (digite FIM para encerrar)? ")
  aluno = Alunos(msg_inicial.upper(), 0, 0)
  aluno.salvar_aluno()

def listar_alunos(lista_de_alunos):
    """
        Imprime na tela as informações de todos os alunos da lista, incluindo nome,
        notas e status.

        Args:
            lista_de_alunos (list): Uma lista de objetos da classe Alunos.
    """
    for aluno in lista_de_alunos:
        print(f"Nome: {aluno.nome}")
        print(f"Nota 1: {aluno.nota1}")
        print(f"Nota 2: {aluno.nota2}")
        print(f"Média: {ceil(aluno.media)}")
        print(f"Status: {aluno.status}")

def procurar_aluno(id_aluno):
    """
        Procura um aluno na lista de alunos pelo seu ID.

        Args:
            id_aluno (int): O identificador do aluno a ser procurado.

        Returns:
            dict: Um dicionário contendo o objeto do aluno e seu índice na lista, caso seja encontrado.
            False: Se o aluno não for encontrado.
    """
    for aluno in lista_de_alunos:
        if aluno.id == id_aluno:
            indice = lista_de_alunos.index(aluno)
            return {
              "aluno":  aluno,
              "indice aluno" :indice
            }
        else:
            print(f"Não existe nenhum aluno com o ID {id_aluno}")
            return False

def calcular_media(id_aluno):
    """ Calcula a média das notas de um aluno específico e atualiza seu status.

        Busca o aluno na lista global de alunos pelo seu ID, calcula a média das suas notas
        e atualiza os atributos `media` e `status` do objeto do aluno.

        Args:
            id_aluno (int): Identificador único do aluno na lista.

        Raises:
            ValueError: Se o aluno não for encontrado.
    """
    aluno = procurar_aluno(id_aluno)
    if(aluno):
        aluno_atributos = aluno["aluno"]
        media = (aluno_atributos.nota1 + aluno_atributos.nota2) / 2
        aluno_atributos.salvar_media(media)
        aluno_atributos.avaliar_status()
    else:
        raise ValueError("Aluno não encontrado!")

def calcular_media_turma():
    """
        Calcula a média geral da turma, chamando a função calcular_media para cada aluno
        e somando as médias individuais.

        Imprime a média geral da turma na tela.
    """
    total_media = 0
    for aluno in lista_de_alunos:
        if(aluno.nome =="FIM"):
            continue
        calcular_media(aluno.id)
        total_media+=aluno.media
    print(f"A média geral da turma é {total_media/(len(lista_de_alunos)-1)}")

def main():
    """
        Função principal do programa.

        Executa as seguintes tarefas:
        1. Cria alunos e adiciona-os à lista.
        2. Calcula a média de cada aluno e atualiza seu status.
        3. Calcula a média geral da turma.
        4. Imprime os dados de todos os alunos.
    """
    criar_aluno()
    calcular_media_turma()
    listar_alunos(lista_de_alunos)

main()