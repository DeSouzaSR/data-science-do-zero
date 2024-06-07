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
print("Número de usuários: ", num_users)
print("Média de conexões por usuário: ", avg_connections)


###### Pessoas mais conectadas
# Pessoas mais conectadas: são as que possuem o maior número de amigos.