from pydantic import BaseModel

class RentRequest(BaseModel):
    unit_area: float
    total_rooms: int
    bathrooms: int