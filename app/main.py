from fastapi import FastAPI
from app.routes import users, devices, accidents, notifications

app = FastAPI(title="Emergency Response System")

# Include routers
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(devices.router, prefix="/api/devices", tags=["Devices"])
app.include_router(accidents.router, prefix="/api/accidents", tags=["Accidents"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["Notifications"])

@app.post("/api/location")
def update_location(location: dict = Body(...)):
    latitude = location.get("latitude")
    longitude = location.get("longitude")
    # Process the location data (e.g., store it in the database)
    return {"message": "Location received", "latitude": latitude, "longitude": longitude}