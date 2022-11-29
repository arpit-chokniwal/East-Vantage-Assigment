from fastapi import APIRouter
from config.db_config import My_Collection
from schema.address_schema import serializeDict, serializeList
from bson import ObjectId
from controller.address_ctrl import findByDistance


address = APIRouter()



# Post Request
@address.post('/v1/api/addressBook/')
async def Add_Address(location_name: str, longitude: float, latitude: float):

    inserted_data = My_Collection.insert_one({"name": location_name, "address": {
                             "coordinates": [longitude, latitude], "type": "Point"}})

    return serializeList(My_Collection.find({'_id':inserted_data.inserted_id}))

# Get Request
@address.get('/v1/api/addressBook/')
async def Get_All_Addresses():

    return serializeList(My_Collection.find())



# Patch Request
@address.patch('/v1/api/addressBook/{id}')
async def Update_Data(id, location_name: str , longitude: float , latitude: float ):

    My_Collection.find_one_and_update(
            {'_id': ObjectId(id)}, {"$set": {"name": location_name, "address": {"coordinates": [longitude, latitude], "type": "Point"}}})
    return serializeDict(My_Collection.find_one({'_id': ObjectId(id)}))


# Delete Request
@address.delete('/v1/api/addressBook/{id}')
async def Delete_Data(id):

    return My_Collection.find_one_and_delete({'_id': ObjectId(id)}, {'_id': 0})


# Get Request (By Distance in meter)
@address.get('/v1/api/addressBook/distance')
async def Get_All_Addresses_By_Distance(longitude: float = -73.98241999999999, latitude: float = 40.579505, distance_in_km: int = 5):

    return serializeList(findByDistance(longitude, latitude, distance_in_km))


# Get Request (By Min and Max length )
@address.get('/v1/api/addressBook/advance_distance')
async def Get_All_Addresses_By_Min_Distance_Max_Distance(longitude: float = -73.98241999999999, latitude: float = 40.579505, max_distance: int=10, min_distance: int =2):
    return serializeList(findByDistance(longitude, latitude, max_distance, min_distance))


# Home Get Request
@address.get('/')
async def Get_All_Addresses():

    return "welcome to easyventage tast please hit http://127.0.0.1:8000/docs"