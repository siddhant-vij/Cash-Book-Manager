from model.Book import Book
from model.Entry import Entry
from utils.CsvHandler import writeToCsv


def deleteAllEntries(book: Book) -> None:
    book.entries = []
    book.cashIn = 0
    book.cashOut = 0
    book.netBalance = 0
    writeToCsv(book, "data/" + book.name + ".csv")


def deleteEntryByIndex(book: Book, entryId: str) -> None:
    entryToDelete: Entry = book.entries[int(entryId) - 1]
    book.entries.remove(entryToDelete)
    if entryToDelete.entryType == "Income":
        book.cashIn -= entryToDelete.amount
    else:
        book.cashOut -= entryToDelete.amount
    book.netBalance = book.cashIn - book.cashOut
    writeToCsv(book, "data/" + book.name + ".csv")
