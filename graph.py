from pathlib import Path
from tools import calculate_late_checkout_fee

DATA_DIR = Path(__file__).parent / "data"

def retrieve_policy_answer(question: str) -> str:
    """Small classroom retrieval demo over the supplied knowledge documents."""
    q = (question or "").lower().strip()
    if not q:
        return "Please enter a question about hotel information."
    if any(term in q for term in ("which room", "room assigned", "my reservation", "reservation")):
        return ("That is outside this assistant's scope. Please contact reception; "
                "this assistant cannot access reservations or room assignments.")
    if "breakfast" in q:
        return "Breakfast is served from 7 AM to 10 AM."
    if "early check-in" in q or "early check in" in q:
        return "Early check-in depends on room availability; it is not guaranteed."
    if "check-in" in q or "check in" in q:
        return "Standard check-in begins at 2 PM. Guests must provide the identification requested by reception."
    if "checkout" in q or "check-out" in q or "check out" in q:
        return ("Standard checkout is at 11 AM. An estimate does not extend a reservation, "
                "and reception must approve any extension.")
    if "fitness" in q or "gym" in q:
        return "The fitness room is open from 6 AM to 9 PM."
    if "wi-fi" in q or "wifi" in q:
        return "Wi-Fi access instructions are available at reception."
    if "supplies" in q or "missing room" in q:
        return "Please contact reception for missing room supplies."
    if "availability" in q or "available" in q:
        return "This assistant cannot check the current availability of hotel services. Please contact reception."
    return ("I couldn't find that information in the hotel knowledge documents. "
            "Please contact reception for assistance.")

def hotel_assistant(state: dict) -> dict:
    """Simple graph-node dispatcher for the project."""
    action = state.get("action")
    if action == "calculate_late_checkout":
        return calculate_late_checkout_fee(
            state.get("nightly_rate"),
            state.get("checkout_time", "")
        )
    if action == "ask_question":
        return {"answer": retrieve_policy_answer(state.get("question", ""))}
    return {"error": "Unsupported action."}
