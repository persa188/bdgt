from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from uuid import uuid4

class AccountType(Enum):
    CHQ = "chequings"
    INV = "investment"
    SAV = "savings"
    RET = "retirement"
    MER = "merchant"
    PAY = "payroll"

class Account(models.Model):
    id: uuid4 = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name: str = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    type = models.CharField(
        choices=[
            (tag, tag.value) for tag in AccountType
        ]
    )
    balance = models.IntegerField(default=0)