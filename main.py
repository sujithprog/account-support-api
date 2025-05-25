from fastapi import FastAPI
from pydantic import BaseModel
from data.accounts_db import ACCOUNTS
from data.balance_db import BALANCES
from data.usage_db import USAGES
from data.invoice_db import INVOICES

app = FastAPI()

class AccountRequest(BaseModel):
    account_number: str

@app.post("/validate/")
def validate_account(data: dict):
    account = data.get("account_number")
    zip_code = data.get("zip_code")
    
    if ACCOUNTS.get(account) == zip_code:
        return {"status": "success", "message": "Account validated."}
    return {"status": "failure", "message": "Invalid account or zip code."}

@app.post("/balance/")
def get_balance(data: AccountRequest):
    balance = BALANCES.get(data.account_number)
    if balance is not None:
        return {"status": "success", "balance": balance}
    return {"status": "failure", "message": "Balance not found."}

@app.post("/usage/")
def get_usage(data: AccountRequest):
    usage = USAGES.get(data.account_number)
    if usage:
        return {"status": "success", "usage": usage}
    return {"status": "failure", "message": "Usage details not found."}

@app.post("/invoice/")
def get_invoice(data: AccountRequest):
    invoice = INVOICES.get(data.account_number)
    if invoice:
        return {"status": "success", "invoice": invoice}
    return {"status": "failure", "message": "Invoice not found."}
