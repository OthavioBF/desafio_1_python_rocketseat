def adicionar_contato(contatos, nome_contato, numero_contato, email_contato, favorito):
  status = True if favorito.lower() == "sim" else False
  contato = {"nome_contato": nome_contato, "contato": numero_contato, "email_contato": email_contato, "favorito": status}
  contatos.append(contato)
  print(f"Contato {nome_contato} foi adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos")
  for key, value in enumerate(contatos, start=1):
    status = "favorito" if value["favorito"] else " "
    nome_contato = value["nome_contato"]
    contato = value["contato"]
    email_contato = value["email_contato"]
    print(f"{key}. [{status}] {nome_contato} {contato} {email_contato}")
  return
    
def atualizar_contato(contatos, index, novo_nome_contato, novo_numero_contato, novo_email_contato, novo_favorito):
  if int(index) - 1 >= 0 and int(index) - 1 < len(contatos):
    if novo_nome_contato != '':
      contatos[int(index) - 1]["nome_contato"] = novo_nome_contato
    if novo_numero_contato != '':
      contatos[int(index) - 1]["contato"] = novo_numero_contato
    if novo_email_contato != '':
      contatos[int(index) - 1]["email_contato"] = novo_email_contato
    if novo_favorito != '':
      contatos[int(index) - 1]["favorito"] = novo_favorito
    print(f"Contato atualizado com sucesso")
  else:
    print("Numero do contato invalido!")
  return

def marcar_desmarcar_favorito(contatos, index):
  if int(index) - 1 >= 0 and int(index) - 1 < len(contatos):
    nome_contato = contatos[int(index) - 1]["nome_contato"]
    status = False if contatos[int(index) - 1]["favorito"] else True
    acao = 'desmarcado' if contatos[int(index) - 1]["favorito"] else 'marcado'
    contatos[int(index) - 1]["favorito"] = status
    print(f"Contato {nome_contato} {acao} como favorito!")
  else:
    print("Numero de tarefa invalido!")
  return

def ver_contatos_favoritos(contatos):
  print("\nLista de contatos")
  for key, value in enumerate(contatos, start=1):
    if value["favorito"]:
      status = "favorito" if value["favorito"] else ""
      nome_contato = value["nome_contato"]
      contato = value["contato"]
      email_contato = value["email_contato"]
      print(f"{key}. [{status}] {nome_contato} {contato} {email_contato}")
  return

def deletar_contato(contatos, index):
  contatos.pop(int(index) - 1)
  print(f"Tarefas completadas foram deletadas com sucesso!")
  return

contatos = []

while True:
  print("\nGerenciador de contatos")
  print("1. Adicionar contato")
  print("2. Vizualizar contatos")
  print("3. Editar contato")
  print("4. Marcar/Desmarcar contato como favorito")
  print("5. Vizualizar contatos favoritos")
  print("6. Deletar contato")
  print("7. Sair")
  
  escolha = input("Digite sua escolha: ")
  
  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    numero_contato = input("Digite o numero de contato que deseja adicionar: ")
    email_contato = input("Digite o email do contato que deseja adicionar: ")
    favorito = input("Deseja marcar como favorito? (sim/nao): ")
    adicionar_contato(contatos, nome_contato, numero_contato, email_contato, favorito)
  elif escolha == "2":
    ver_contatos(contatos)
  elif escolha == "3":
    ver_contatos(contatos)
    index_contato = input("Digite o numero do contato que deseja atualizar: ")
    print("Se nao quiser atualizar o campo atual aperte enter!")
    novo_nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    novo_numero_contato = input("Digite o numero de contato que deseja adicionar: ")
    novo_email_contato = input("Digite o email do contato que deseja adicionar: ")
    novo_favorito = input("Deseja marcar como favorito? (sim/nao): ")
    atualizar_contato(contatos, index_contato, novo_nome_contato, novo_numero_contato, novo_email_contato, novo_favorito)
  elif escolha == "4":
    ver_contatos(contatos)
    index_contato = input("Digite o numero do contato que deseja marcar/desmarcar como favorito: ")
    marcar_desmarcar_favorito(contatos, index_contato)
  elif escolha == "5":
    ver_contatos_favoritos(contatos)
  elif escolha == "6":
    ver_contatos(contatos)
    index_contato = input("Digite o numero do contato que deseja deletar: ")
    deletar_contato(contatos, index_contato)
    ver_contatos(contatos)
  elif escolha == "7":
    break
  
print("Programa finalizado")