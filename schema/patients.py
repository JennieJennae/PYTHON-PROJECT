# Patient: id, name, age, sex, weight, height, phone
from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name:str
    age: int
    sex: str
    weight: int
    height: int
    phone: str
    
    
class PatientUpdate(BaseModel):
    name:str
    age: int
    sex: str
    weight: int
    height: int
    phone: str
    

patient = [
    Patient(id=0, name="Musa", age=30, sex="M", weight = 120, height=18, phone= "+2347087859615" ),
    Patient(id=1, name="Adaora", age=22, sex="F", weight = 93, height=22, phone= "+2348164896351" )
]