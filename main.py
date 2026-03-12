from fastapi import FastAPI, HTTPException

app = FastAPI()

current_expression = ""


@app.get("/")
async def root():
    return {"message": "FastAPI Calculator"}


# Сложение
@app.get("/add")
async def add(a: float, b: float):
    return {"result": a + b}


# Вычитание
@app.get("/subtract")
async def subtract(a: float, b: float):
    return {"result": a - b}


# Умножение
@app.get("/multiply")
async def multiply(a: float, b: float):
    return {"result": a * b}


# Деление
@app.get("/divide")
async def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": a / b}


# Сохранить выражение
@app.post("/expression")
async def set_expression(expr: str):
    global current_expression
    current_expression = expr
    return {"expression": current_expression}


# Посмотреть выражение
@app.get("/expression")
async def get_expression():
    return {"expression": current_expression}


# Вычислить выражение
@app.get("/calculate")
async def calculate():
    global current_expression

    if not current_expression:
        raise HTTPException(status_code=400, detail="Expression is empty")

    try:
        result = eval(current_expression)
        return {
            "expression": current_expression,
            "result": result
        }
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid expression")
