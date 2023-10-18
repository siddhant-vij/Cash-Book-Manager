import os
from prettytable import PrettyTable

from model.Book import Book
from model.Entry import Entry


def getBookNames():
    files = os.listdir("data")
    files = [x[:-4] for x in files]
    return files


def printBooksToConsole() -> None:
    books = getBookNames()
    table = PrettyTable()
    table.field_names = ["S.No.", "Cashbook"]
    for index, book in enumerate(books):
        table.add_row([index+1, book])
    print(table)


def printBookEntriesToConsole(book: Book) -> None:
    entries = PrettyTable()
    entries.field_names = ["S.No.", "Entry Type", "Date", "Time",
                           "Description", "Amount", "Category", "Payment Mode"]
    for index, entry in enumerate(book.entries):
        entries.add_row([index+1, entry.entryType, entry.date, entry.time,
                         entry.description, entry.amount, entry.category, entry.paymentMode])
    print(entries)


def printEntryDetailsToConsole(entry: Entry) -> None:
    entryTable = PrettyTable()
    entryTable.field_names = ["S.No.", "Entry Key", "Entry Value"]
    for index, detail in enumerate(entry.__dict__.items()):
        if detail[0] != "id":
            entryTable.add_row([index, detail[0], detail[1]])
    print(entryTable)


def printBookSummaryViewToConsole(book: Book) -> None:
    summaryTable = PrettyTable()
    summaryTable.field_names = ["Book Name",
                                "Cash In", "Cash Out", "Net Balance"]
    summaryTable.add_row(
        [book.name, book.cashIn, book.cashOut, book.netBalance])
    print(summaryTable)
