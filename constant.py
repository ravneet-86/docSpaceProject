# Used for main heading in a frame.
HEADING_FONT = ("Verdana", 22)

# Used as second main heading in a frame.
HEADING_FONT_1 = ("Verdana", 15)

# Used for all the normal button, entry widgets.
WIDGET_FONT = ("Verdana", 12)

# Used for smaller widgets (button or labels etc) on the edges like log out.
WIDGET_FONT_1 = ("Verdana", 10)

# Used for smaller widgets (button or labels etc) on the edges like log out.
WIDGET_FONT_SMALL = ("Verdana", 8)

DOC_SPACE = "DOC Space"

LOG_OUT = "Log Out"

DOC_SPACE_HEADING_LABEL_0 = "Doctor Space"

EMAIL_LABEL = "Username/Email"

PASSWORD_LABEL = "Password"

SHOW_PASSWORD_LABEL = "Show Password"

HIDE_PASSWORD_LABEL = "Hide Password"

ENTRY_MAX_LEN_3 = 3

ENTRY_MAX_LEN_6 = 6

ENTRY_MAX_LEN_10 = 10

ENTRY_MAX_LEN_12 = 12

ENTRY_MAX_LEN_20 = 20

ENTRY_MAX_LEN_30 = 30

ENTRY_MAX_LEN_50 = 50

ERROR_BOX_TITLE = "DocSpace: Error Message"

MESSAGE_BOX_TITLE = "DocSpace: Message"

REGISTRATION_SUCCESS = "You are Registered successfully\nPlease Login."

REGISTRATION_FAILURE = "Registration failed\nPlease Contact the Developer or Try again."

MEDICAL_RECORD_SAVED_SUCCESS = "Medical Record Successfully Saved."

DB_CONNECTION_ERROR = "Error Connecting to Database\nPlease Contact the Developer or Try again."

ERROR_INVALID_EMAIL = "Email Address is Invalid\nPlease check and try again."

DOCTOR_NAME = "Doctor: "

MANDATORY_FIELDS = "* are mandatory fields"

GO_BACK = "Go Back"

PATIENT_ID = "Patient Id: "

PATIENT_NAME = "Name: "

PATIENT_GENDER = "Gender: "

PATIENT_AGE = "Age: "

PATIENT_DOB = "DOB: "

PATIENT_ADDRESS = "Address: "

PATIENT_CITY = "City: "

PATIENT_CONTACT_NO = "Mobile No: "

PATIENT_MARTIAL_S = "Martial Status: "

PATIENT_OCCUPATION = "Occupation: "

MEDICAL_RECORD_DATE = "Record Date: "

MEDICAL_RECORD_MEDICINES = "Medicines: "

MEDICAL_RECORD_SYMPTOMS = "Symptoms: "

##################################################################
#          DATABASE Constants                                    #
##################################################################
# DB information, TODO: if required move to a text file and read from there instead.
DB_HOST = "localhost"
DB_USER = "root"
# DB_USER_PASSWORD = "homeoPathicDocSpace21"
DB_USER_PASSWORD = "dehradun86"
DB_NAME = "DocSpace"
DB_BACKUP_PATH = "./"

# Error Messages
ERROR_PASSWORD_NOT_MATCHING = "Entered Password does not match\nPlease check the Password and try again."
ERROR_CHECKING_EMAIL_ADDRESS = "Error Checking Email Address in Database\nPlease Contact the Developer or Try again."
ERROR_EMAIL_USER_NOT_EXIST = "Email/User does not exist in Database\nPlease register and try again."
ERROR_DOCTOR_INFO_NOT_PRESENT = "Doctor Information not present\nPlease log out and try logging in again."
EMAIL_ADDRESS_ALREADY_EXIST = "Entered Email is already used\nPlease use different Email or"\
                              "\nTry login with this Email, Use Forgot password if required"
ERROR_CREATING_TABLE = "Unable to create Database\nPlease Contact Developer or Try again."
ERROR_INSERTING_TABLE = "Unable to register User in Database\nPlease Contact Developer or Try again."
ERROR_PATIENT_REGISTRATION_CHECK_USER_EXIST_IN_DB_FAILURE = "Unable to check and validate user in Database"
ERROR_INSERTING_PATIENT_TABLE = "Unable to register Patient in Database\nPlease Contact Developer or Try again."
ERROR_UPDATING_PATIENT_TABLE = "Unable to update Patient in Database\nPlease Contact Developer or Try again."
ERROR_GETTING_PATIENT_INFO_FROM_TABLE = "Error getting Patient info from updated Database"
ERROR_SEARCHING_DATA_BASE_ENTRY_SEARCH_RESULTS = "Unable to search user in Database\nPlease Contact Developer or Try " \
                                                 "again after restarting "
ERROR_INSERTING_MEDICAL_RECORD_TABLE = "Error Inserting the Medical Record\nPlease Contact Developer or Try again."
ERROR_UPDATING_MEDICAL_RECORD_TABLE = "Error Updating the Medical Record\nPlease Contact Developer or Try again."
ERROR_GETTING_MEDICAL_RECORDS = "Error getting Medical Records for the Patient\nPlease Contact Developer or Try again."
##################################################################
# Below is how the Doctor Table looks like                       #
'''
-- Create Doctor Information table
create table doctor_info (
							name varchar(20) not null,
							email varchar(30) not null primary key,
                            password varchar(10) not null,
							contact_no varchar(12) not null,
							mobile_no varchar(10) not null,
							clinic_name varchar(20) not null,
							clinic_address varchar(50) not null
							);
'''
##################################################################
# Column indexes as defined in the Database create query
DOCTOR_INFO_NAME_INDEX = 0
DOCTOR_INFO_EMAIL_INDEX = 1
DOCTOR_INFO_PASSWORD_INDEX = 2
DOCTOR_INFO_CONTACT_NO_INDEX = 3
DOCTOR_INFO_MOBILE_NO_INDEX = 4
DOCTOR_INFO_CLINIC_NAME_INDEX = 5
DOCTOR_INFO_CLINIC_ADDRESS_INDEX = 6

# Table name and columns names as defined in the database
DOCTOR_INFO_TABLE = "doctor_info"
DOCTOR_INFO_COL = "(name, email, password, contact_no, mobile_no, clinic_name, clinic_address)"
DOCTOR_INFO_EMAIL_COL_NAME = "email"
DOCTOR_INFO_PASSWORD_COL_NAME = "password"

# Create table strings for patient info
CREATE_TABLE_PATIENT_INFO_STRING = ''' (
                            patient_id int not null primary key auto_increment,
                            name varchar(20) not null,
                            gender varchar(6) not null,
                            age int not null,
                            contact_no varchar(12) not null,
                            address varchar(50) not null,
                            city varchar(10) not null,
                            martial_status varchar(10) not null,
                            occupation varchar(20) not null,
                            dob date not null
                        );'''
PATIENT_INFO_COL = "(name, gender, age, contact_no, address, city, martial_status, occupation, dob)"

PATIENT_INFO_TABLE_ID_COL_NAME = 'patient_id'
PATIENT_INFO_TABLE_NAME_COL_NAME = 'name'
PATIENT_INFO_TABLE_GENDER_COL_NAME = 'gender'
PATIENT_INFO_TABLE_AGE_COL_NAME = 'age'
PATIENT_INFO_TABLE_CONTACT_NO_COL_NAME = 'contact_no'
PATIENT_INFO_TABLE_ADDRESS_COL_NAME = 'address'
PATIENT_INFO_TABLE_CITY_COL_NAME = 'city'
PATIENT_INFO_TABLE_MARTIAL_S_COL_NAME = 'martial_status'
PATIENT_INFO_TABLE_OCCU_COL_NAME = 'occupation'
PATIENT_INFO_TABLE_DOB_COL_NAME = 'dob'

PATIENT_INFO_TYPE_STRING = "_patient_info"

PATIENT_INFO_ID_INDEX = 0
PATIENT_INFO_NAME_INDEX = 1
PATIENT_INFO_GENDER_INDEX = 2
PATIENT_INFO_AGE_INDEX = 3
PATIENT_INFO_CONTACT_NO_INDEX = 4
PATIENT_INFO_ADDRESS_INDEX = 5
PATIENT_INFO_CITY_INDEX = 6
PATIENT_INFO_MARTIAL_STATUS_INDEX = 7
PATIENT_INFO_OCCUPATION_INDEX = 8
PATIENT_INFO_DOB_INDEX = 9
PATIENT_REGISTRATION_SUCCESS = "Patient Registered successfully."
PATIENT_INFO_UPDATED_SUCCESS = "Patient Info Updated successfully"

CREATE_TABLE_MEDICAL_RECORD_STRING = ''' (
                            patient_id int not null,
                            record_date date not null,
                            case_type varchar(2) not null,
                            symptoms varchar(50) not null,
                            symptoms_agg_by varchar(50) not null,
                            symptoms_ameol_by varchar(50) not null,
                            symptoms_since varchar(50) not null,
                            present_complains varchar(50) not null,
                            appetite varchar(50) not null,
                            thirst varchar(50) not null,
                            urine varchar(50) not null,
                            stool varchar(50) not null,
                            sleep varchar(50) not null,
                            perspiration varchar(50) not null,
                            addiction varchar(50) not null,
                            desires varchar(50) not null,
                            aversions varchar(50) not null,
                            thermal_reaction varchar(50) not null,
                            allergy varchar(50) not null,
                            mental_symptoms varchar(50) not null,
                            back varchar(50) not null,
                            chest varchar(50) not null,
                            ear varchar(50) not null,
                            eye varchar(50) not null,
                            face varchar(50) not null,
                            head varchar(50) not null,
                            lips varchar(50) not null,
                            mouth varchar(50) not null,
                            nose varchar(50) not null,
                            teeth varchar(50) not null,
                            throat varchar(50) not null,
                            tongue varchar(50) not null,
                            past_history varchar(50) not null,
                            family_history varchar(50) not null,
                            menstrual_history varchar(50) not null,
                            Investigation varchar(50) not null,
                            medicine varchar(160) not null,
                            dose varchar(100) not null,
                            potency varchar(80) not null,
                            days varchar(80) not null,
                            next_visit_date date not null,
                            amount varchar(80) not null,
                            primary key(patient_id, record_date)
                        );'''
MEDICAL_RECORD_TYPE_STRING = "_medical_record"

MEDICAL_RECORD_TABLE_ID_COL_NAME = 'patient_id'
MEDICAL_RECORD_TABLE_RECORD_DATE_COL_NAME = 'record_date'
MEDICAL_RECORD_TABLE_CASE_TYPE_COL_NAME = 'case_type'
MEDICAL_RECORD_TABLE_SYMPTOMS_COL_NAME = 'symptoms'
MEDICAL_RECORD_TABLE_SYMPTOMS_AGG_BY_COL_NAME = 'symptoms_agg_by'
MEDICAL_RECORD_TABLE_SYMPTOMS_AMEOL_BY_COL_NAME = 'symptoms_ameol_by'
MEDICAL_RECORD_TABLE_SYMPTOMS_SINCE_COL_NAME = 'symptoms_since'
MEDICAL_RECORD_TABLE_PRESENT_COMPLAINS_COL_NAME = 'present_complains'
MEDICAL_RECORD_TABLE_APPETITE_COL_NAME = 'appetite'
MEDICAL_RECORD_TABLE_THIRST_COL_NAME = 'thirst'
MEDICAL_RECORD_TABLE_URINE_COL_NAME = 'urine'
MEDICAL_RECORD_TABLE_STOOL_COL_NAME = 'stool'
MEDICAL_RECORD_TABLE_SLEEP_COL_NAME = 'sleep'
MEDICAL_RECORD_TABLE_PERSPIRATION_COL_NAME = 'perspiration'
MEDICAL_RECORD_TABLE_ADDICTIONS_COL_NAME = 'addiction'
MEDICAL_RECORD_TABLE_DESIRES_COL_NAME = 'desires'
MEDICAL_RECORD_TABLE_AVERSIONS_COL_NAME = 'aversions'
MEDICAL_RECORD_TABLE_THERMAL_REACTION_COL_NAME = 'thermal_reaction'
MEDICAL_RECORD_TABLE_ALLERGY_COL_NAME = 'allergy'
MEDICAL_RECORD_TABLE_MENTAL_SYMPTOMS_COL_NAME = 'mental_symptoms'
MEDICAL_RECORD_TABLE_BACK_COL_NAME = 'back'
MEDICAL_RECORD_TABLE_CHEST_COL_NAME = 'chest'
MEDICAL_RECORD_TABLE_EAR_COL_NAME = 'ear'
MEDICAL_RECORD_TABLE_EYE_COL_NAME = 'eye'
MEDICAL_RECORD_TABLE_FACE_COL_NAME = 'face'
MEDICAL_RECORD_TABLE_HEAD_COL_NAME = 'head'
MEDICAL_RECORD_TABLE_LIPS_COL_NAME = 'lips'
MEDICAL_RECORD_TABLE_MOUTH_COL_NAME = 'mouth'
MEDICAL_RECORD_TABLE_NOSE_COL_NAME = 'nose'
MEDICAL_RECORD_TABLE_TEETH_COL_NAME = 'teeth'
MEDICAL_RECORD_TABLE_THROAT_COL_NAME = 'throat'
MEDICAL_RECORD_TABLE_TONGUE_COL_NAME = 'tongue'
MEDICAL_RECORD_TABLE_PAST_HISTORY_COL_NAME = 'past_history'
MEDICAL_RECORD_TABLE_FAMILY_HISTORY_COL_NAME = 'family_history'
MEDICAL_RECORD_TABLE_MENSTRUAL_HISTORY_COL_NAME = 'menstrual_history'
MEDICAL_RECORD_TABLE_INVESTIGATION_COL_NAME = 'Investigation'
MEDICAL_RECORD_TABLE_MEDICINE_COL_NAME = 'medicine'
MEDICAL_RECORD_TABLE_DOSE_COL_NAME = 'dose'
MEDICAL_RECORD_TABLE_POTENCY_COL_NAME = 'potency'
MEDICAL_RECORD_TABLE_DAYS_COL_NAME = 'days'
MEDICAL_RECORD_TABLE_NEXT_VISIT_DATE_COL_NAME = 'next_visit_date'
MEDICAL_RECORD_TABLE_AMOUNT_COL_NAME = 'amount'

MEDICAL_COL_NAME_LIST = [MEDICAL_RECORD_TABLE_ID_COL_NAME,
MEDICAL_RECORD_TABLE_RECORD_DATE_COL_NAME,
MEDICAL_RECORD_TABLE_CASE_TYPE_COL_NAME,
MEDICAL_RECORD_TABLE_SYMPTOMS_COL_NAME,
MEDICAL_RECORD_TABLE_SYMPTOMS_AGG_BY_COL_NAME,
MEDICAL_RECORD_TABLE_SYMPTOMS_AMEOL_BY_COL_NAME,
MEDICAL_RECORD_TABLE_SYMPTOMS_SINCE_COL_NAME,
MEDICAL_RECORD_TABLE_PRESENT_COMPLAINS_COL_NAME,
MEDICAL_RECORD_TABLE_APPETITE_COL_NAME,
MEDICAL_RECORD_TABLE_THIRST_COL_NAME,
MEDICAL_RECORD_TABLE_URINE_COL_NAME,
MEDICAL_RECORD_TABLE_STOOL_COL_NAME,
MEDICAL_RECORD_TABLE_SLEEP_COL_NAME,
MEDICAL_RECORD_TABLE_PERSPIRATION_COL_NAME,
MEDICAL_RECORD_TABLE_ADDICTIONS_COL_NAME,
MEDICAL_RECORD_TABLE_DESIRES_COL_NAME,
MEDICAL_RECORD_TABLE_AVERSIONS_COL_NAME,
MEDICAL_RECORD_TABLE_THERMAL_REACTION_COL_NAME,
MEDICAL_RECORD_TABLE_ALLERGY_COL_NAME,
MEDICAL_RECORD_TABLE_MENTAL_SYMPTOMS_COL_NAME,
MEDICAL_RECORD_TABLE_BACK_COL_NAME,
MEDICAL_RECORD_TABLE_CHEST_COL_NAME,
MEDICAL_RECORD_TABLE_EAR_COL_NAME,
MEDICAL_RECORD_TABLE_EYE_COL_NAME,
MEDICAL_RECORD_TABLE_FACE_COL_NAME,
MEDICAL_RECORD_TABLE_HEAD_COL_NAME,
MEDICAL_RECORD_TABLE_LIPS_COL_NAME,
MEDICAL_RECORD_TABLE_MOUTH_COL_NAME,
MEDICAL_RECORD_TABLE_NOSE_COL_NAME,
MEDICAL_RECORD_TABLE_TEETH_COL_NAME,
MEDICAL_RECORD_TABLE_THROAT_COL_NAME,
MEDICAL_RECORD_TABLE_TONGUE_COL_NAME,
MEDICAL_RECORD_TABLE_PAST_HISTORY_COL_NAME,
MEDICAL_RECORD_TABLE_FAMILY_HISTORY_COL_NAME,
MEDICAL_RECORD_TABLE_MENSTRUAL_HISTORY_COL_NAME,
MEDICAL_RECORD_TABLE_INVESTIGATION_COL_NAME,
MEDICAL_RECORD_TABLE_MEDICINE_COL_NAME,
MEDICAL_RECORD_TABLE_DOSE_COL_NAME,
MEDICAL_RECORD_TABLE_POTENCY_COL_NAME,
MEDICAL_RECORD_TABLE_DAYS_COL_NAME,
MEDICAL_RECORD_TABLE_NEXT_VISIT_DATE_COL_NAME,
MEDICAL_RECORD_TABLE_AMOUNT_COL_NAME
]
MEDICAL_RECORD_TABLE_ID_INDEX = 0
MEDICAL_RECORD_TABLE_RECORD_DATE_INDEX = 1
MEDICAL_RECORD_TABLE_CASE_TYPE_INDEX = 2
MEDICAL_RECORD_TABLE_SYMPTOMS_INDEX = 3
MEDICAL_RECORD_TABLE_SYMPTOMS_AGG_BY_INDEX = 4
MEDICAL_RECORD_TABLE_SYMPTOMS_AMEOL_BY_INDEX = 5
MEDICAL_RECORD_TABLE_SYMPTOMS_SINCE_INDEX = 6
MEDICAL_RECORD_TABLE_PRESENT_COMPLAINS_INDEX = 7
MEDICAL_RECORD_TABLE_APPETITE_INDEX = 8
MEDICAL_RECORD_TABLE_THIRST_INDEX = 9
MEDICAL_RECORD_TABLE_URINE_INDEX = 10
MEDICAL_RECORD_TABLE_STOOL_INDEX = 11
MEDICAL_RECORD_TABLE_SLEEP_INDEX = 12
MEDICAL_RECORD_TABLE_PERSPIRATION_INDEX = 13
MEDICAL_RECORD_TABLE_ADDICTIONS_INDEX = 14
MEDICAL_RECORD_TABLE_DESIRES_INDEX = 15
MEDICAL_RECORD_TABLE_AVERSIONS_INDEX = 16
MEDICAL_RECORD_TABLE_THERMAL_REACTION_INDEX = 17
MEDICAL_RECORD_TABLE_ALLERGY_INDEX = 18
MEDICAL_RECORD_TABLE_MENTAL_SYMPTOMS_INDEX = 19
MEDICAL_RECORD_TABLE_BACK_INDEX = 20
MEDICAL_RECORD_TABLE_CHEST_INDEX = 21
MEDICAL_RECORD_TABLE_EAR_INDEX = 22
MEDICAL_RECORD_TABLE_EYE_INDEX = 23
MEDICAL_RECORD_TABLE_FACE_INDEX = 24
MEDICAL_RECORD_TABLE_HEAD_INDEX = 25
MEDICAL_RECORD_TABLE_LIPS_INDEX = 26
MEDICAL_RECORD_TABLE_MOUTH_INDEX = 27
MEDICAL_RECORD_TABLE_NOSE_INDEX = 28
MEDICAL_RECORD_TABLE_TEETH_INDEX = 29
MEDICAL_RECORD_TABLE_THROAT_INDEX = 30
MEDICAL_RECORD_TABLE_TONGUE_INDEX = 31
MEDICAL_RECORD_TABLE_PAST_HISTORY_INDEX = 32
MEDICAL_RECORD_TABLE_FAMILY_HISTORY_INDEX = 33
MEDICAL_RECORD_TABLE_MENSTRUAL_HISTORY_INDEX = 34
MEDICAL_RECORD_TABLE_INVESTIGATION_INDEX = 35
MEDICAL_RECORD_TABLE_MEDICINE_INDEX = 36
MEDICAL_RECORD_TABLE_DOSE_INDEX = 37
MEDICAL_RECORD_TABLE_POTENCY_INDEX = 38
MEDICAL_RECORD_TABLE_DAYS_INDEX = 39
MEDICAL_RECORD_TABLE_NEXT_VISIT_INDEX = 40
MEDICAL_RECORD_TABLE_AMOUNT_INDEX = 41

MEDICAL_RECORD_INFO_COL = '''(patient_id,
                            record_date,
                            case_type,
                            symptoms,
                            symptoms_agg_by,
                            symptoms_ameol_by,
                            symptoms_since,
                            present_complains,
                            appetite,
                            thirst,
                            urine,
                            stool,
                            sleep,
                            perspiration,
                            addiction,
                            desires,
                            aversions,
                            thermal_reaction,
                            allergy,
                            mental_symptoms,
                            back,
                            chest,
                            ear,
                            eye,
                            face,
                            head,
                            lips,
                            mouth,
                            nose,
                            teeth,
                            throat,
                            tongue,
                            past_history,
                            family_history,
                            menstrual_history,
                            Investigation,
                            medicine,
                            dose,
                            potency,
                            days,
                            next_visit_date,
                            amount)'''
