from pymongo import MongoClient

def save_data_to_database(data):
    # Connect to MongoDB
    client = MongoClient('mongodb+srv://Xerphen:nek090906@cluster0.mzyxj4u.mongodb.net/?retryWrites=true&w=majority')
    db = client['mars']
    collection = db['mars']  # Replace 'collection_name' with the actual name of your collection

    # Save data to the databasev 
    document = {'data': data}
    result = collection.insert_one(document)

    client.close()

    if result.inserted_id:
        return "Data saved successfully"
    else:
        return "Failed to save data"
