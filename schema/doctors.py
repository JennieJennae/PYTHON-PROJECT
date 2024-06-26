# Doctors: id, name, specialization, phone, is_available (defaults to True)

from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    is_available = "True"
    not_available = "False"

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: Status = Status.is_available
    
    def set_availability(self, availability: Status):
        self.is_available = availability


    
class DoctorsUpdate(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorStatus(BaseModel):
    is_available: Status
    
    

doctors: list[Doctors] = [
    Doctors(id=1, name="Ufondu", specialization= "Padieatrics", phone= "+2348034354587", is_available= Status.is_available),
    Doctors(id=2, name="Okurinola", specialization= "Oncology", phone= "+2347061859819", is_available= Status.not_available)
]
