# skridt 1: importere nødvendige biblioteker

# importer bibloteket 
# FastApi er et web framework for å bygge APIer i Python.
# Det er kjent for sin hastighet og enkelhet, 
# og det gjør det enkelt å lage robuste og skalerbare APIer.

from fastapi import FastAPI

# pydentic er et bibliotek for datavalidering og 
# innstilling av data i Python.
from pydantic import BaseModel
from typing import Optional


# skridt 2: opprette en FastAPI-app instance 
app = FastAPI()

# skridt 3: lage en datamodell for bøker

# Fake Dummy Data 
# array of dictionary
books = [
    {"id": 1, "title": "Python Basics", "author": "Real P.", "pages": 635},
    {"id": 2, "title": "Breaking the Rules", "author": "Stephen G.", "pages": 99},
    {"id": 3, "title": "Breaking the Data", "author": "Stephen F.", "pages": 100},
    {"id": 4, "title": "Breaking the rule1", "author": "Stephen L.", "pages": 200},
]

# Book class is a Pydantic model that defines the structure of a book object.
class Book(BaseModel):   
    title: str
    author: str
    pages: int
    
    
# skridt 4: lage en GET-endepunkt for å hente alle bøker
# get all books
@app.get("/books")
def get_books():
    return books

# get book by id
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

# search books by title or author
@app.get("/books/search/{query}")
def search_books(query: str):
    results = []
    q = query.lower()

    for book in books:
        title = book["title"].lower()
        author = book["author"].lower()

        if q in title or q in author:
            results.append(book)

    return results

# Post book
@app.post("/books")
def create_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    }
    books.append(new_book)
    return new_book

# Put book
@app.put("/books/{id}")
def update_book(id: int, updated_book: Book):
    for book in books:
        if book["id"] == id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["pages"] = updated_book.pages
            return book
    return {"message": "Book not found"}



@app.delete("/books/{id}")
def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}


