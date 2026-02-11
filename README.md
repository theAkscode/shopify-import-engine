# Matrixify-Lite

Standalone Shopify product import engine with a FastAPI backend and a Vite + React frontend.

## Assumptions
- Input file is CSV or Excel (.csv, .xlsx, .xls).
- Required columns must be present and are case-sensitive.
- Products are grouped by Handle, and variants are grouped by Variant SKU.
- If Variant SKU matches an existing variant, it is updated; otherwise it is added.
- This project uses an in-memory Shopify stub for product storage.

## Schema / Field Mapping
The parser expects these columns and maps them as follows:

- Handle -> product.handle
- Title -> product.title
- Vendor -> product.vendor
- Variant SKU -> variant.sku
- Variant Price -> variant.price
- Variant Inventory Qty -> variant.inventory
- Option1 Name -> variant.option_name
- Option1 Value -> variant.option_value

## Example Import File Template
Use this header and sample rows to match the parser:

```csv
Handle,Title,Vendor,Variant SKU,Variant Price,Variant Inventory Qty,Option1 Name,Option1 Value
shirt-basic,Basic Tee,Acme,TS-S,19.99,50,Size,S
shirt-basic,Basic Tee,Acme,TS-M,19.99,60,Size,M
```

A copy of this template is available in sample.csv.

## Setup Instructions

### Backend
```bash
cd backend
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

API endpoint:
- POST http://127.0.0.1:8000/import/products

### Frontend
```bash
cd frontend
npm install
npm run dev
```

App runs at http://localhost:5173

## Deliverables
- Backend code in backend/
- Frontend code in frontend/
- UI screen in the running app
- Tests: minimal pytest suite under backend/tests/

## Tests
```bash
cd backend
python -m pytest
```

## Repository Submission
Push the repo to GitHub after verifying both services run locally.
