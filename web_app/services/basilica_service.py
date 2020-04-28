

import os
import basilica
from dotenv import load_dotenv

load_dotenv()

API_KEY =  os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(API_KEY)
print(type(connection)) # class "basilica.Connection"

breakpoint()

embedding = connection.embed_sentence("hello everyone", model="twitter")
# embedding classs list
