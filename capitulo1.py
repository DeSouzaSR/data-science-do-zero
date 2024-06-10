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
print('Chi tem dois amigos em comum com Hero(0) e um com Clive(5)')

###### Usuários com o mesmo interesse
# Dados
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Função que encontra usuários com o mesmo interesse
def data_scientists_who_like(target_interest):
    """Fornece a lista de usuários com o interesse alvo"""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

print("\nCientistas de dados que gostam de Hadoop")
print(data_scientists_who_like("Hadoop"))
print("Cientistas de dados que gostam de Python")
print(data_scientists_who_like("Python"))

# Construir um índice de interesses para usuários 
# Vamos construir um dicionário em que as chaves são interesses e os valores são
#   listas de usuários.
from collections import defaultdict
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Vamos construir um dicionário em que as chaves são os usuários e os valores são
#   os interesses

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

# Agora vamos descobrir quem possui os interesses em comum
def most_common_interests_with(user):
    return Counter(interested_user_id
        for interest in interests_by_user_id[user['id']]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user['id'])

print("Interesses em comum com Hero(0)")
print(most_common_interests_with(users[0]))
