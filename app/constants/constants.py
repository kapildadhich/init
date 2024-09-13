from enum import Enum


class Constants(Enum):
    WELCOME_MSG = "Glad to see you:)"
    GET_EMAIL = "What's your email address?"
    EXAMPLE_EMAIL = "name@example.com"
    OTP_EMAIL_BODY = "You otp to sign in NotesAPP is {}"
    OTP_EMAIL_SUBJECT = "NotesAPP OTP"

class CtaText(Enum):
    INIT_CTA_TEXT = "Next"

class HTTPStatusCodes(Enum):
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    FORBIDDEN = 403
    UNAUTHORIZED = 401
    MOVED_TEMPORARILY = 302
    INTERNAL_SERVER_ERROR = 500
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 503

