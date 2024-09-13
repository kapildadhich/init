from app.repository.user import UserRepository
from app.utils import generate_otp
from .email_manager import EmailManager
from ..constants import Constants
from .page_manager import PageManager
from app.cache.base import RedisClient
from ..exceptions import ValidationError
from  ..repository import UserModel

class SignInManager:
    def __init__(self) -> None:
        pass
    

    @classmethod
    async def send_sign_in_otp(cls, gmail):
        otp = generate_otp()
        EmailManager.send_email(Constants.OTP_EMAIL_SUBJECT.value, Constants.OTP_EMAIL_BODY.value.format(otp), gmail) 
        await RedisClient().set(f"otp-{gmail}", str(otp), expire= 120)
        return PageManager.render_otp_page(gmail)

    @classmethod
    async def validate_otp(cls, gmail, otp):
        sent_otp= await RedisClient().get(f"otp-{gmail}")
        if not sent_otp:
            raise ValidationError("OTP expired")
        
        if int(sent_otp)!= int(otp):
            raise ValidationError("Invalid OTP")
        user = await UserRepository.get_by_gmail(gmail)
        return PageManager.render_validate_otp_page(user)
        

