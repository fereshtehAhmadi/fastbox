from fastapi import FastAPI

app = FastAPI(title="FastBox Demo API", version="1.0.0")


@app.get("/greet/")
def greet_user():
    """
    Example endpoint for a simple GET request.
    """
    return {"message": "Welcome to FastBox!"}


@app.get("/book/{title}")
def get_book_info(title: str):
    """
    Example showing a path parameter.
    Returns a short description for a given book title.
    """
    return {"book_title": title, "description": f"{title} is an amazing read!"}


@app.get("/product/{product_name}")
def get_product_details(product_name: str, price: float = 99.9):
    """
    Example combining path and query parameters.

    Path parameter:
      - product_name: specifies the product

    Query parameter:
      - price (optional, with default value)

    Demonstrates how query params can have default values.
    """
    return {
        "product": product_name,
        "price": price,
        "message": f"The product '{product_name}' costs ${price}.",
    }
