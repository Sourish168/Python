from pydantic import BaseModel # type: ignore

# TODO: Create Booking model 
# Fields:
# - uder_id: int
# - room_id: int
# - nights: int (must be >= 1)
# - rate_per_night: float
# Also, add computrd field: total_amount = nights * rate_per_night