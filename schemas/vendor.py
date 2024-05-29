def vendorEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "contact_details": item["contact_details"],
        "address": item["address"],
        "vendor_code": item["vendor_code"],
        "on_time_delivery_rate": item["on_time_delivery_rate"],
        "quality_rating_avg": item["quality_rating_avg"],
        "fulfillment_rate": item["fulfillment_rate"],
    }

def serializelist(entity) -> list:
    item = []
    for i in entity:
        serialised_data = serializeDict(i)
        item.append(serialised_data)
    return item

def serializeDict(a) -> dict :
    # print("11111111111111111111111111111111",a, type(a)) 
    if type(a) != dict:
        return "only dictionary can be serialized"
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}

