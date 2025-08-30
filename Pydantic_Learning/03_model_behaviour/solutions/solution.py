from pydantic import BaseModel, Field, computed_field # type: ignore

# TODO: Create Booking model 
# Fields:
# - uder_id: int
# - room_id: int
# - nights: int (must be >= 1)
# - rate_per_night: float
# Also, add computrd field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(...,
                        ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night

input_data = {"user_id": 712136,
              "room_id": 501,
              "nights": "13",
              "rate_per_night": "350"}
booking = Booking(**input_data)   
print(booking)
print(booking.total_amount)