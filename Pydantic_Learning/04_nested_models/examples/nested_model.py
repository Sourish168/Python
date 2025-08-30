from typing import List, Optional
from pydantic import BaseModel # type: ignore

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address # Other Replication/Reference from Address Class

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None # Self Replication/Reference from Comment Class

Comment.model_rebuild() # Rebuilding Forward Referencing for Pydantic 

address = Address(
    street = "MG Road",
    city = "Kolkata",
    postal_code = "700012"
)

user = User(
    id = 15,
    name = "Sourish",
    address = address
)

comment = Comment(
    id = 11,
    content = "First Comment",
    replies = [Comment(id=1, content="Reply 1"),
               Comment(id=4, content="Reply 2", replies=[Comment(id=6, content="Reply 1 of Reply 2"), Comment(id=7, content="Reply 2 of Reply 2")])]
)

print(address)
print(user)
print(70*"#")
print(comment)