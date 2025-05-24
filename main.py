from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class DivisionInputs(BaseModel):
    numerator: float
    denominator: float


@app.post("/divide")
async def divide_numbers(inputs: DivisionInputs):
    if inputs.denominator == 0:
        raise HTTPException(
            status_code=400, detail="Division by zero is not permitted."
        )

    result = round(inputs.numerator / inputs.denominator, 2)
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
