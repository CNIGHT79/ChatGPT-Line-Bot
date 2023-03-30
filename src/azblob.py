from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient
import json
token_credential = DefaultAzureCredential()

class azblob():
    def __init__(self):
        self.blob_name = "db.json"
        self.container_name = "__flask__"
        self.data_dict ={}

    def getClient(self,sas_url):
        self.blob_service_client = BlobServiceClient(account_url = sas_url, token_credential = DefaultAzureCredential())
        self.blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=self.blob_name)
        return self.blob_client

    def load_data(self,blob_client):
        self.blob_data = blob_client.download_blob().readall()
        self.data_dict = json.loads(self.blob_data)
        return self.data_dict
    
    def add_data(self, key, value):
        try:
            print(self.data_dict)
        except Exception as e:
            print(e)
        
        if key in self.data_dict:
            if isinstance(self.data_dict[key], list):
                if value not in self.data_dict[key]:
                    self.data_dict[key].append(value)
            else:
                 if value != self.data_dict[key]:
                     self.data_dict[key] = [self.data_dict[key], value]
            print("if_",key,self.data_dict[key])
        else:
            print("else_",key)
            self.data_dict[key] = value
            
    def get_data(self):
        return self.data_dict
    
    def save_data(self, blob_client, data):
        self.update_data = data
        self.client = blob_client
        print(self.update_data)
        self.updated_json_string = json.dumps(self.update_data)
        try:
            self.client.upload_blob(self.updated_json_string, overwrite=True)
        except Exception as e:
            print(e)


#Azblob = azblob()