from fastapi import FastAPI, UploadFile, File
from parser import parse_file
from merge import merge_product, merge_variant
from shopify import get_product, create_product, update_product, get_all_products
from supabase_service import log_import
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/import/products")
def import_products(file: UploadFile = File(...)):
    """
    Accept CSV or Excel file,
    parse into structured product data,
    apply merge logic,
    and store via Shopify layer (stub).
    """

    # ✅ Basic file validation
    if not file.filename.endswith((".csv", ".xlsx", ".xls")):
        return {
            "error": "Unsupported file format. Please upload CSV or Excel."
        }

    try:
        # Step 1: Parse file
        parsed_products = parse_file(file)

    except ValueError as e:
        # Column validation or parsing errors
        return {"error": str(e)}

    except Exception:
        # Catch unexpected errors
        return {"error": "Failed to process file."}

    results = {
        "created": 0,
        "updated": 0
    }

    # Step 2: Process each product
    for handle, incoming_product in parsed_products.items():

        existing_product = get_product(handle)

        if existing_product:

            # Merge product-level fields
            merge_product(existing_product, incoming_product)

            # Merge variants
            for variant in incoming_product["variants"]:
                merge_variant(existing_product["variants"], variant)

            update_product(existing_product)

            results["updated"] += 1

        else:
            create_product(incoming_product)
            results["created"] += 1
    log_import(
    file.filename,
    results["created"],
    results["updated"],
    "success"
)

    return {
        "summary": results,
        "data": get_all_products()
    }
