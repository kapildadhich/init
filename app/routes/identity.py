from sanic import Blueprint
from sanic.exceptions import SanicException
from sanic.request import Request
from app.manager import PageManager, SignInManager
from app.repository.user import UserRepository
from ..exceptions import ValidationError
from ..utils import send_response
from ..repository import UserModel

identity = Blueprint(name="identity", url_prefix="/sign_in", version=1)

@identity.route("/init", methods=["GET"])
async def init(request: Request):
    response = PageManager.init_page()
    return send_response(response)

@identity.route("/otp/<gmail:str>", methods=["GET"])
async def send_otp(request: Request, gmail):
    response = await SignInManager.send_sign_in_otp(gmail)
    return send_response(response)


@identity.route("/verify/otp/<gmail:str>", methods=["GET"])
async def verify_otp(request: Request, gmail):
    try:
       payload = request.args
       otp = payload.get("otp")
       if not otp:
           raise ValidationError("No OTP given")
       response = await SignInManager.validate_otp(gmail, payload)
    except Exception as e:
        raise SanicException(message=str(e), status_code=400) from e
        
    return send_response(response)

@identity.route("/create_user", methods=["POST"])
async def create_user(request: Request):
    payload = request.json
    response = await UserRepository.create(payload)
    return send_response(response)





