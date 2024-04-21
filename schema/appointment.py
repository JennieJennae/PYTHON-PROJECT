from pydantic import BaseModel
from schema.patients import Patient
from schema.doctors import Doctors
from datetime import datetime

class Appointment(BaseModel):
    id: int
    patient: Patient
    doctor: Doctors
    appointment_time: datetime
    

appointment_data = [
    {
        "id": 11,
        "patient": {"id": 0, "name": "Ahmed", "age": 50, "sex": "M", "weight": 100, "height": 22, "phone": "+2348036782925"},
        "doctor": {"id": 1, "name": "Falomo", "specialization": "Anesthesiology", "phone": "+2347164859515", "is_available": True},
        "appointment_time": "2024-04-22T12:00:00"  
    },
    {
        "id": 12,
        "patient": {"id": 1, "name": "Beatrice", "age": 11, "sex": "F", "weight": 90, "height": 19, "phone": "+234330000000"},
        "doctor": {"id": 2, "name": "Aderinokun", "specialization": "Dermatology", "phone": "+2347061703817", "is_available": True},
        "appointment_time": "2024-04-20T14:00:00" 
    }
]

appointments = [Appointment(**data) for data in appointment_data]
