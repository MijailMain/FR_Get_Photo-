from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient
import os
import json

# Load People list (PersonId and Names)
with open('Energetika_Customer.json', encoding="utf8") as f:
  People = json.load(f)

# Load File Names in Blob-Storage
with open('Files_Blob.json') as f:
  Name_Blob = json.load(f)

#Check for each person on the list
for person in People:
  item = 0

  print("#####################################################################################")
  print(person["PersonId"])
  print(person["PersonName"])

  # Check each file in blob storage
  for data in Name_Blob:

    #try:
      value = "value" + str(item)
      print(Name_Blob[value])
    #except:
      #print ("Error")

      # Check if the personId is linked to a file in blobstorage
      validar = Name_Blob[value].find(person["PersonId"])
      print(validar)

      
      if ( validar > -1):
        
        try:
            print("#####################################################################################")
            print("PersonId     ", person["PersonId"])
            print("fileName ", Name_Blob[value])
            # conections
            blob = BlobClient.from_connection_string(
              #  connection string (Az)
              conn_str="", 
              container_name="photos",       
              blob_name= Name_Blob[value]  # name file in blob storage
              )

            # save Image of person
            with open("Images/" + person["PersonId"] + ".jpg", "wb") as my_blob:
                blob_data = blob.download_blob()
                blob_data.readinto(my_blob)

            print("#####################################################################################")
            print("Person Found")
        except:
            print("'Error', person not found")

      #PeopleId.append(data["PersonId"])
      item +=1

print("process finished check images folder")