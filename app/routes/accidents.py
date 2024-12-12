from fastapi import APIRouter, Depends
from app.schemas.accident import AccidentReport
from app.services.notification_service import notify_emergency_contacts

router = APIRouter()

@router.post("/detect")
def report_accident(report: AccidentReport):
    # Business logic for accident detection
    notify_emergency_contacts(report.device_id, report.location, report.severity)
    return {"message": "Accident detected. Notifications sent."}
