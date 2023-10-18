from datetime import date
from model.Book import Book
from model.Entry import Entry


def viewEntryByIndex(book: Book, entryIndex: str) -> Entry:
    return book.entries[int(entryIndex) - 1]


def filterBookEntriesByCategoryType(book: Book, category: str) -> Book:
    filteredBook = Book(book.name + "-filtered-by-category", [])
    for entry in book.entries:
        if entry.category == category:
            filteredBook.entries.append(entry)
    return filteredBook


def filterBookEntriesByDateRange(book: Book, startDate: date, endDate: date) -> Book:
    filteredBook = Book(book.name + "-filtered-by-date", [])
    for entry in book.entries:
        if entry.date >= startDate and entry.date <= endDate:
            filteredBook.entries.append(entry)
    return filteredBook


def filterBookEntriesByPaymentModeType(book: Book, paymentMode: str) -> Book:
    filteredBook = Book(book.name + "-filtered-by-paymentMode", [])
    for entry in book.entries:
        if entry.paymentMode == paymentMode:
            filteredBook.entries.append(entry)
    return filteredBook


def filterBookEntriesByEntryType(book: Book, entryType: str) -> Book:
    filteredBook = Book(book.name + "-filtered-by-entryType", [])
    for entry in book.entries:
        if entry.entryType == entryType:
            filteredBook.entries.append(entry)
    return filteredBook
