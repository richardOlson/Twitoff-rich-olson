

import os
import basilica
from dotenv import load_dotenv

load_dotenv()

API_KEY =  os.getenv("BASILICA_API_KEY")

basilica_connection = basilica.Connection(API_KEY)



if __name__ == "__main__":
    
    print(type(basilica_connection)) # class "basilica.Connection"

    breakpoint()

    embedding = basilica_connection.embed_sentence("hello everyone", model="twitter")
    # embedding classs list
