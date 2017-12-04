
from datetime import datetime

class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.time_admitted = datetime.now()
        self.bed_num = None
        self.id = Patient.PATIENT_COUNT
        
        Patient.PATIENT_COUNT += 1

class Hospital(object):
    def __init__(self, hosp_name, capacity):
        self.patients = []
        self.hosp_name = hosp_name
        self.capacity = capacity
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    Patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"
    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"


Todd = Patient("Todd Coles", "None")
Nick = Patient("Nicolas Coles", "None")
ccd = Hospital("Test hosp", 10).admit(Todd)
ccp = Hospital("Test hosp", 10).admit(Nick)




