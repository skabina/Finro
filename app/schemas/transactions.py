from decimal import Decimal
from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict, StringConstraints
from datetime import date, datetime

from enum import Enum




Comment = Annotated[
    str | None,
    StringConstraints(
        min_length=3,
        max_length=50,
        strip_whitespace=True,
    ),
]

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class TransactionCategory(str, Enum):
    GROCERIES = "groceries"
    TRANSPORT = "transport"
    ENTERTAINMENT = "entertainment"
    HEALTH = "health"
    EDUCATION = "education"
    OTHER = "other"

class TransactionCreate(BaseModel):
    amount: Annotated[Decimal, Field(gt=0)]
    type: TransactionType
    comment: Comment = None
    category: TransactionCategory
    date: date

class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    amount: Decimal
    type: TransactionType
    comment: Comment = None
    category: TransactionCategory
    date: date
    created_at: datetime


class TransactionUpdate(BaseModel):
    amount: Annotated[Decimal | None, Field(gt=0)] = None
    type: TransactionType | None = None
    comment: Comment = None
    category: TransactionCategory | None = None
    date: date | None = None
