from config.db_config import My_Collection

def findByDistance(longitude, latitude, max_distance, min_distance=0):
    data = list(My_Collection.find({
        "address": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [longitude, latitude]
                },
                "$maxDistance": max_distance,
                "$minDistance": min_distance
            }
        }
    }))
    return data