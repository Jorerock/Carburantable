import json

with open(".\\prix-carburants-fichier-instantane-test-ods-copie.json", "r") as read_file:
    data = json.load(read_file)


moins_chere = float(0 if data[1]["prix_valeur"] is None else data[1]["prix_valeur"])
Id_moins_chere = 1

for i in range (len(data)) :
    i_Prix = float(99999 if data[i]["prix_valeur"] is None else data[i]["prix_valeur"])
    # print(data[i]["ville"], i_Prix, moins_chere)
    if(i_Prix <= moins_chere) :
        moins_chere = i_Prix
        Id_moins_chere = i


print("ville: ",data[Id_moins_chere]["ville"])
print("daresse: ",data[Id_moins_chere]["adresse"])
print("Prix: ",data[Id_moins_chere]["prix_valeur"])


# print(data[1])
print("end")
