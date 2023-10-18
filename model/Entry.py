from datetime import date, time


class Entry:
    def __init__(self, entryType: str, date: date, time: time,
                 description: str, amount: float, category: str, paymentMode: str) -> None:
        self.entryType = entryType
        self.date = date
        self.time = time
        self.description = description
        self.amount = amount
        self.category = category
        self.paymentMode = paymentMode
