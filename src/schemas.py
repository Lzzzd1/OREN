from pydantic import BaseModel
from pydantic_br import CPFDigits, CNPJDigits


class NovoCliente(BaseModel):
    id: CPFDigits | CNPJDigits
