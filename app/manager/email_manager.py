from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.constants.config import CONFIG

class EmailManager:

    def __init__(self) -> None:
        pass

    def send_email(subject, body, to_email):
        sendgrid_api_key =  CONFIG.config["EMAIL_CONFIG"]["SANDGRID_API_KEY"] 
        message = Mail(
            from_email= CONFIG.config["EMAIL_CONFIG"]["FROM_EMAIL"],
            to_emails=to_email,
            subject=subject,
            plain_text_content=body
        )
        
        try:
            sg = SendGridAPIClient(sendgrid_api_key)
            response = sg.send(message)
            print(f"Email sent successfully to {to_email}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send email. Error: {str(e)}")
    
        
