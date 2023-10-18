from datetime import date, time
import os
from model.Book import Book
from model.Entry import Entry


def writeToCsv(book: Book, fileName: str) -> None:
    with open(fileName, "w") as f:
        counter = 0
        for entry in book.entries:
            counter += 1
            f.write(f"{str(counter)},{str(entry.entryType)},{str(entry.date)},{str(entry.time)},{str(entry.description)},{float(entry.amount)},{str(entry.category)},{str(entry.paymentMode)}" + "\n")


def readFromCsv(fileName: str) -> Book:
    if not os.path.exists(fileName):
        return Book(fileName.split(".")[0].split("/")[1], [])
    with open(fileName, "r") as f:
        entries = []
        for line in f:
            fields = line.strip().split(",")
            entry = Entry(
                entryType=fields[1],
                date=date((int)(fields[2].split(
                    "-")[0]), (int)(fields[2].split("-")[1]), (int)(fields[2].split("-")[2])),
                time=time((int)(fields[3].split(":")[0]), (int)(
                    fields[3].split(":")[1]), (int)(fields[3].split(":")[2])),
                description=fields[4],
                amount=float(fields[5]),
                category=fields[6],
                paymentMode=fields[7]
            )
            entries.append(entry)
    return Book(fileName.split(".")[0].split("/")[1], entries)
