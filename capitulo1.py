# Códigos do capítulo 1
####### Usuários
users = [
    {"id":0, "name":"Hero"},
    {"id":1, "name":"Dunn"},
    {"id":2, "name":"Sue"},
    {"id":3, "name":"Chi"},
    {"id":4, "name":"Thor"},
    {"id":5, "name":"Clive"},
    {"id":6, "name":"Hicks"},
    {"id":7, "name":"Devin"},
    {"id":8, "name":"Kate"},
    {"id":9, "name":"Klein"},
]

####### Amigos
# a tupla (0,1) indica que o cientista de dados com a id 0 (Hero) e o
# cientista de dados com a id 1 (Dunn) são amigos.
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

####### Lista de amigos
# Vamos adicionar uma lista de amigos para cada usuário
# Primeiro, criamos a propriedade friends.
for user in users:
    user["friends"] = []

# Agora vamos povoar a lista com os nomes dos amigos.
# Vamos fazer isso, usando as tuplas friendships
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

###### Conexões
# Qual é o número médio de conexões?
# Primeiro, achar o total de conexões
number_of_friends = lambda user : len(user['friends'])
total_connections = sum(number_of_friends(user) for user in users)
# Então, dividimos o total de conexões pelo número de usuários, para 
# obter a média
num_users = len(users)
avg_connections = total_connections / num_users
print("\nNúmero de usuários: ", num_users)
print("Média de conexões por usuário: ", avg_connections)


###### Pessoas mais conectadas
# Pessoas mais conectadas: são as que possuem o maior número de amigos.
# Ordenar os usuários pelo número de amigos em ordem decrescente
sorted_users = sorted(users, key=number_of_friends, reverse=True)

# Imprimir a lista dos usuários mais conectados
print("\nPessoas mais conectadas:")
for user in sorted_users:
    print(f"{user['name']} tem {number_of_friends(user)} amigos.")

###### Cientista de dados que talvez você conheça
# Para cada amigo de um usuário, iterar sobre o amigo daquela pessoa e coleta
#   os resultados

def friends_of_friends_ids_bad(user):
    return [foaf['id']
            for friend in user['friends']
            for foaf in friend['friends']]

# Para users[0] (Hero), temos
print("\nCientista de dados que talvez você conheça")
print("Hero (users[0])")
print(friends_of_friends_ids_bad(users[0]))

###### Amigos em comum
print("\nAmigos em comum")
from collections import Counter

def not_the_same(user, other_user):
    """dois usuários não são os mesmos se possuem ids diferentes"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user não é um amigo se não está em user["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf['id'] 
                   for friend in user['friends']
                   for foaf in friend['friends']
                     if not_the_same(user, foaf)
                     and not_friends(user,foaf))

print("Amigos do usuário")
print(users[3]["name"])
print(friends_of_friend_ids(users[3]))