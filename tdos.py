from pydantic import BaseModel

class UserTDO(BaseModel):
    id: int
    name: str
    username: str
    email: str | None = None