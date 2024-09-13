from app.constants import Constants , CtaText


class PageManager:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def init_page(cls):
        data = {
             "image":"",
             "header": Constants.WELCOME_MSG.value,
             "sub_header": Constants.GET_EMAIL.value,
             "email":{
               "input_txt": Constants.EXAMPLE_EMAIL.value
             },
             "cta":{
             "text": CtaText.INIT_CTA_TEXT.value
             }
        }
        
        return data
    
    @classmethod
    def render_otp_page(cls, gmail):
        data = {
            "header":"Verify Account",
            "sub_header": f"Enter OTP sent to {gmail}",
            "cta":{
               "text":"Resend",
               "action":"RESEND_OTP"
            }
        }
        return data

    @classmethod
    def render_validate_otp_page(cls, user):
        data = {}
        data["redirect_page"] = "Home" if user else "About you"
        return data



