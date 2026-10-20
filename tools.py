from datetime import datetime

def calculate_late_checkout_fee(nightly_rate: float, checkout_time: str) -> dict:
    """Estimate the additional late-checkout charge using the classroom policy."""
    try:
        rate = float(nightly_rate)
    except (TypeError, ValueError):
        return {"error": "Nightly rate must be a valid number."}
    if rate <= 0:
        return {"error": "Nightly rate must be positive."}

    if not isinstance(checkout_time, str):
        return {"error": "Checkout time must be a valid HH:MM time (24-hour clock)."}

    try:
        parsed = datetime.strptime(checkout_time, "%H:%M")
        # strptime can accept non-zero-padded values on some platforms; enforce HH:MM.
        if parsed.strftime("%H:%M") != checkout_time:
            raise ValueError
    except ValueError:
        return {"error": "Enter a valid HH:MM time using the 24-hour clock, for example 14:30."}

    minutes = parsed.hour * 60 + parsed.minute
    if minutes <= 11 * 60:
        percentage = 0
    elif minutes <= 14 * 60:
        percentage = 25
    elif minutes <= 18 * 60:
        percentage = 50
    else:
        percentage = 100

    charge = round(rate * percentage / 100, 2)
    return {
        "checkout_time": checkout_time,
        "charge_percentage": percentage,
        "additional_charge": charge,
        "approval_required": minutes > 11 * 60,
        "message": (
            "Reception approval is required for checkout after 11 AM."
            if minutes > 11 * 60
            else "No late-checkout extension approval is needed under this estimate."
        )
    }
