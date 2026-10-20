# Project 31 — Hotel Guest Information Assistant

A small Flask classroom project with a late-checkout charge calculator and a policy-question demo.

## Requirements
- Python 3.10+
- Flask

## Run in VS Code
1. Extract `project31_hotel_assistant.zip`.
2. Open the extracted `project31_hotel_assistant` folder in VS Code.
3. Open Terminal → New Terminal.
4. (Optional) Create a virtual environment:
   - Windows: `py -m venv .venv`
   - PowerShell: `.venv\\Scripts\\Activate.ps1`
5. Install dependencies: `python -m pip install -r requirements.txt`
6. Start the app: `python app.py`
7. Open the local address printed in the terminal (usually `http://127.0.0.1:5000`).

## Example calculations
- Rate 4000, time 11:00 → 0%, INR 0.00
- Rate 4000, time 14:00 → 25%, INR 1000.00
- Rate 4000, time 14:01 → 50%, INR 2000.00
- Rate 4000, time 18:01 → 100%, INR 4000.00

## Scope boundaries
- The tool estimates the additional charge only.
- Checkout after 11 AM requires reception approval.
- It does not access reservations, assign rooms, check live service availability, or approve extensions.
- The policy documents in `data/` are fictional classroom data.
