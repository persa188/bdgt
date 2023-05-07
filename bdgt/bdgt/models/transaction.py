from django.db import models
from django.contrib.auth.models import User
from .account import Account
from uuid import uuid4
from enum import Enum

class TransactionType(Enum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateField()
    source = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    dest = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    amount = models.FloatField(null=False)
    currency = models.CharField(default="CAD")
    type = models.CharField(
        choices=[
            (tag, tag.value) for tag in TransactionType
        ]
    )
    category = models.CharField()
    metadata = models.JSONField()

