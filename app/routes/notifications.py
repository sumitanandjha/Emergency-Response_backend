from app.utils.notification_utils import send_sms, send_email

def notify_emergency_contacts(device_id: str, location: dict, severity: str):
    contacts = [
        {"name": "Jane Doe", "phone": "+1234567890"}  # Fetch contacts from the database
    ]
    for contact in contacts:
        send_sms(contact["phone"], f"Accident detected at {location}. Severity: {severity}")
        send_email(contact["email"], "Emergency Alert", f"Accident detected at {location}.")
