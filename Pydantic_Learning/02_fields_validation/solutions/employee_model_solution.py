from pydantic import BaseModel, Field # type: ignore
from typing import Optional

# TODO: Create Employee model 
# - id: int
# - name: str
# - department: optional str (default "General")
# - salary: float (must be >= 10000)

class Employee(BaseModel):
    id: int
    name: str = Field(..., 
                      min_length=3,
                      max_length=50,
                      description="Employee Name",
                      examples="Sourish Ghosh")
    department: Optional[str]="General"
    salary: float = Field(...,
                          ge=10000)
    

input_data = {"id": 110,
              "name": "Tiger Shroff",
              "salary": "40000",
            #   "department": "Data Science"
              }
employee=Employee(**input_data)
print(employee)