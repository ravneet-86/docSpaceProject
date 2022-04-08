# Class with Static data members, basically used to store global application data
# like Doctor information after user has successfully logged in.
# This class is very closely tied to the DB Controller class and has information
# of inner working of the database.

class GlobalAppData:
    # Below are class global static variables
    # This holds the doctor login info as returned from the data base.
    # it is in below format
    logged_in_doc_info = ()
    curr_selected_patient = []
    curr_medical_record = None
    gen_back_up_files_status = None
    gen_back_up_files_name = None
    gDrive_file_upload_result = None

    # Below two are not used in the App as of now.
    @staticmethod
    def set_logged_in_doc_info(doc_info):
        GlobalAppData.logged_in_doc_info = doc_info

    @staticmethod
    def get_logged_in_doc_info():
        return GlobalAppData.logged_in_doc_info

    @staticmethod
    def set_curr_selected_patient(patient_detail_list):
        GlobalAppData.curr_selected_patient = patient_detail_list

    @staticmethod
    def get_curr_selected_patient():
        return GlobalAppData.curr_selected_patient

    @staticmethod
    def set_curr_medical_record(medical_record):
        GlobalAppData.curr_medical_record = medical_record

    @staticmethod
    def get_curr_medical_record():
        return GlobalAppData.curr_medical_record

    @staticmethod
    def get_gen_back_up_files_status():
        return GlobalAppData.gen_back_up_files_status

    @staticmethod
    def set_gen_back_up_files_status(status):
        GlobalAppData.gen_back_up_files_status = status

    @staticmethod
    def get_gen_back_up_files_name():
        return GlobalAppData.gen_back_up_files_name

    @staticmethod
    def set_gen_back_up_files_name(back_up_files_name):
        GlobalAppData.gen_back_up_files_name = back_up_files_name

    @staticmethod
    def set_g_drive_file_upload_result(result):
        GlobalAppData.gDrive_file_upload_result = result

    @staticmethod
    def get_g_drive_file_upload_result():
        return GlobalAppData.gDrive_file_upload_result

