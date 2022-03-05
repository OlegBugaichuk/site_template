from pydantic import BaseModel


class MainPageSchema(BaseModel):
    title: str