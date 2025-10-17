from fastapi import FastAPI, Query, status, Request
from pydantic import BaseModel, Field
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

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


class Item(BaseModel):
    """
    Pydantic model defining the structure and validation rules
    for a book item in the API request body.
    """
    name: str
    author: str = Field(max_length=500, min_length=5)
    price: int
    number: int | None = Field(default=1, ge=1)


@app.post("/create/book/")
def create_book(item: Item, creator: str = Query(default="staff")):
    """
    Example endpoint demonstrating:
    - Request body validation using a Pydantic model (`Item`)
    - Query parameter with a default value (`creator`)
    - Use of `model_dump()` to serialize model data into a dictionary
    """
    return {"creator": creator, **item.model_dump()}


class UserInput(BaseModel):
    username: str = Field(min_length=3, max_length=50, description="User's display name")
    phone_number: str = Field(
        pattern=r"^09\d{9}$",
        description="Iranian mobile number (must start with 09 and be 11 digits)",
    )
    password: str = Field(min_length=8)


class UserOutPut(BaseModel):
    username: str
    phone_number: str


@app.post("/create/user/", response_model=UserOutPut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserInput):
    """
    Endpoint to create a new user.

    - **Request Body: Uses `UserInput` for input validation.
    - **Response Model: Returns `UserOutPut`, which hides sensitive data like passwords.

    This demonstrates how to separate input and output models for cleaner and safer API design.
    """
    return user


template = Jinja2Templates(directory="templates")


@app.get("/welcome/template/{name}", response_class=HTMLResponse)
def welcome(request: Request, name: str):
    """
    Endpoint to render a welcome page using a Jinja2 template.

    Path Parameter:
    - name: The name of the user to greet, passed in the URL path.

    Context:
    - The `context` dictionary is used to pass data into the template.
    - The `request` object is required by Jinja2Templates for template rendering.

    Returns:
    - HTML response rendered from 'welcome.html' with the user's name.

    Example:
    GET /welcome/template/Fereshteh
    """

    return template.TemplateResponse(
        request=request,
        name="welcome.html",
        context={"name": name}
    )
