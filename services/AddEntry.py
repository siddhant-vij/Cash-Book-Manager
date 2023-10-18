from model.Book import Book
from model.Entry import Entry
from utils.CsvHandler import writeToCsv


def addEntryToBook(book: Book, entry: Entry) -> None:
    book.entries.append(entry)
    if entry.entryType == "Income":
        book.cashIn += entry.amount
    else:
        book.cashOut += entry.amount
    book.netBalance = book.cashIn - book.cashOut
    writeToCsv(book, "data/" + book.name + ".csv")
