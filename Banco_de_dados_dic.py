import pickle as pck

BD={"Nome":{0:"Eduardo Oliveira",
            1:"Amaral Silva",
            2:"Bianca Gama"},
    "CPF":{0:78945612332,
           1:12345678912,
           2:12378945612},
    "Endereço":{0:"Rua Da Batata",
                1:"Rua Da Cenoura",
                2:"Rua Do Chuchu"}}

def listar_funcoes():
    print("Funções disponíveis")
    print("incluir() - Para incluir um novo cadastro")
    print("excluir_por_nome() - Para excluir um cadastro")
    print("alterar_dados() - Para alterar uma indormação")
    print("listarBD() - Retorna todos os nomes e CPFs cadastrados por ordem alfabética")
    print("consulta_completa_nome() - Retorna todas as informações de um cadastro pesquisando pelo nome")
    print("consulta_completa_cpf() - Retorna todas as informações de um cadastro pesquisando pelo CPF")

    
def incluir():
    id=len(BD["Nome"])
    nome=input("Digite o nome")
    nome = nome.title()
    cpf=eval(input("Digite o CPF. Somente os números"))
    end=input("Digite o endereço")
    end=end.title()
    BD["Nome"][id] = nome
    BD["CPF"][id] = cpf
    BD["Endereço"][id] = end 
    with open("MeuBancoDeDados.pkl","wb") as file:
        pck.dump(BD,file)
    return print("inclusão confirmada")
    
def excluir_por_nome():
    def excluir(i):
        del BD["Nome"][i]
        del BD["CPF"][i]
        del BD["Endereço"][i]
        with open("MeuBancoDeDados.pkl","wb") as file:
            pck.dump(BD,file)
        return print("Exclusão confirmada")
    
    nome = input("Digite o nome do registro que será excluido")
    nome = nome.title()
    for i in range(len(BD["Nome"])):
        if BD["Nome"][i] == nome:
            return excluir(i)
    
    return (print("Nome incorreto ou inexistente. Tente novamente"),excluir_por_nome())
    
    
def alterar_dados():
    def alteração(id,dado):
        if dado == "Nome":
            novo_nome = input("Digite o novo nome")
            novo_nome = novo_nome.title()
            BD["Nome"][id] = novo_nome
            with open("MeuBancoDeDados.pkl","wb") as file:
                pck.dump(BD,file)
            return print("Alteração confirmada")
        if dado == "CPF":
            novo_cpf = eval(input("Digite o novo CPF. Somente os números"))
            BD["CPF"][id] = novo_cpf
            with open("MeuBancoDeDados.pkl","wb") as file:
                pck.dump(BD,file)
            return print("Alteração confirmada")
        if dado == "Endereço":
            novo_end = input("Digite o nome endereço")
            novo_end = novo_end.title()
            BD["Endereço"][id] = novo_end
            with open("MeuBancoDeDados.pkl","wb") as file:
                pck.dump(BD,file)
            return print("Alteração confirmada")
    
    nome=input("Digite o nome que deseja alterar uma informação")
    nome=nome.title()
    dado=input("Digite qual dado deseja alterar")
    for i in range(len(BD["Nome"])):
        if BD["Nome"][i] == nome:
            return alteração(i,dado)
    return (print("Nome incorreto ou inexistente. Tente novamente"),alterar_dados())    


def listarBD():
    lista=[]
    for i in range(len(BD["Nome"])):
        lista.append([BD["Nome"][i],BD["CPF"][i]])
    lista = sorted(lista)
    for i in range(len(lista)):
        print("Nome:",lista[i][0],"-","CPF:",lista[i][1])
    
    
def consulta_completa_nome():
    def impressao(i,existe):
        if existe == "Sim":
            print("Nome:",BD["Nome"][i],"\n" "CPF:",BD["CPF"][i],"\n" "Endereço:",BD["Endereço"][i])
        else:
            print("Nome incorreto ou inexistente. Tente novamente")
            consulta_completa_nome()
    
    nome=input("Digite o nome completo")
    nome=nome.title()
    for i in range(len(BD["Nome"])):
        if BD["Nome"][i] == nome:
            return impressao(i,"Sim")
    return impressao(i,"Não")


def consulta_completa_cpf():
    def impressao(i,existe):
        if existe == "Sim":
            print("CPF:",BD["CPF"][i],"\n" "Nome:",BD["Nome"][i],"\n" "Endereço:",BD["Endereço"][i])
        else:
            print("CPF incorreto ou inexistente. Tente novamente")
            consulta_completa_cpf()
    
    numero=eval(input("Digite o CPF.Somente os números"))
    for i in range(len(BD["CPF"])):
        if BD["CPF"][i] == numero:
            return impressao(i,"Sim")
    return impressao(i,"Não")