def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

def serializelist(entity) -> list:
    # return [serializeDict(item) for item in entity]
    item = []
    for i in entity:
        serialised_data = serializeDict(i)
        item.append(serialised_data)
    return item

def serializeDict(a) -> dict :
    print("11111111111111111111111111111111",a, type(a)) 
    # breakpoint()
    # return a
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}

# def serializelist(entity) -> list:
#     return [serializeDict(a) for a in entity]            
