from typing import List

from model.Entry import Entry


class Book:
    def __init__(self, name: str, entries: List[Entry]) -> None:
        self.name = name
        self.entries = entries
        self.cashIn = sum(
            [entry.amount for entry in entries if entry.entryType == "Income"])
        self.cashOut = sum(
            [entry.amount for entry in entries if entry.entryType == "Expense"])
        self.netBalance = self.cashIn - self.cashOut
