
# Class with Static data members, basically used to store global application data
# like Doctor information after user has succesfully logged in.
class GlobalAppData:

    logged_in_doc_info = ()

    @staticmethod
    def set_logged_in_doc_info(doc_info):
        GlobalAppData.logged_in_doc_info = doc_info

    @staticmethod
    def get_logged_in_doc_info():
        return GlobalAppData.logged_in_doc_info
