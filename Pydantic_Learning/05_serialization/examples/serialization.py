from pydantic import BaseModel, ConfigDict # type: ignore
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders = {datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )

# Create a user instance
user = User(
    id = 11,
    name = "Sourish",
    email = "sourish@google.in",
    createdAt = datetime(2022, 4, 11, 15, 27),
    address = Address(street = "MG Road", city = "Kolkata", zip_code = "700100"),
    tags = ["Premium", "Subscriber"],
    is_active = True
)
print(user)
print(70*"#", "\n")

# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)
print(70*"#", "\n")

# Using model_dump_json() -> dict
python_json = user.model_dump_json()
print(python_json)