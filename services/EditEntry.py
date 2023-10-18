from model.Book import Book
from model.Entry import Entry
from utils.CsvHandler import writeToCsv


def editEntryByIndex(book: Book, oldEntryIndex: str, newEntry: Entry) -> Book:
    entryToEdit = book.entries[int(oldEntryIndex) - 1]
    if entryToEdit.entryType == "Income":
        book.cashIn -= entryToEdit.amount
    else:
        book.cashOut -= entryToEdit.amount

    if newEntry.entryType == "Income":
        book.cashIn += newEntry.amount
    else:
        book.cashOut += newEntry.amount

    book.netBalance = book.cashIn - book.cashOut

    entryToEdit.entryType = newEntry.entryType
    entryToEdit.date = newEntry.date
    entryToEdit.time = newEntry.time
    entryToEdit.description = newEntry.description
    entryToEdit.amount = newEntry.amount
    entryToEdit.category = newEntry.category
    entryToEdit.paymentMode = newEntry.paymentMode
    writeToCsv(book, "data/" + book.name + ".csv")
    return
