

import os
import basilica
from dotenv import load_dotenv

load_dotenv()

API_KEY =  os.getenv("BASILICA_API_KEY")

basilica_connection = basilica.Connection(API_KEY)



if __name__ == "__main__":
    
    print(f"The type of the basilica_connection is --- {type(basilica_connection)}") # class "basilica.Connection"

   

    embedding = basilica_connection.embed_sentence("hello everyone", model="twitter")
    # embedding classs list
    print(f"The size of the embedding is {len(embedding)}")
