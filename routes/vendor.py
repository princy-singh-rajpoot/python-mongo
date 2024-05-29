from fastapi import APIRouter
from models.vendor import Vendor 
from config.db import conn
from schemas.vendor import serializeDict,serializelist
from bson import ObjectId

vendor = APIRouter()

@vendor.get('/')
async def find_all_vendors():
    return serializelist(conn.local.vendor.find())

@vendor.get('/{id}')
async def find_one_vendor(id):
   return serializeDict(conn.local.vendor.find_one({"_id":ObjectId(id)}))

@vendor.post('/')
async def create_vendor(vendor: Vendor):
    conn.local.vendor.insert_one(dict(vendor))
    return serializelist(conn.local.vendor.find())

@vendor.put('/{id}')
async def update_vendors(id,vendor:Vendor):
    conn.local.vendor.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(vendor)})
    return serializeDict(conn.local.vendor.find_one({"_id":ObjectId(id)}))

@vendor.delete('/{id}')
async def delete_vendor(id):
    if conn.local.vendor.find_one({"_id":ObjectId(id)}) == None:
        return "Data does not exist"
    conn.local.vendor.delete_one({"_id":ObjectId(id)})
    return "vendor data deleted successfully"
    