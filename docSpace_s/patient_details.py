# Just defines the interface which holds the patient detail information
class PatientDetails:

    def __init__(self, name, gender, age, dob, occupation, martial_status,
                 mobile_no, address, city):
        self.name = name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.occupation = occupation
        self.martial_status = martial_status
        self.mobile_no = mobile_no
        self.address = address
        self.city = city
