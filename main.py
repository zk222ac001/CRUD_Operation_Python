# skridt no 1 : importere FastAPI klassen fra fastapi biblioteket

from fastapi import FastAPI
from pydantic import BaseModel

# skridt no 2 : oprette en instans af FastAPI klassen
app = FastAPI()

# Fake Dummy Data 

books = [
    {"id": 1, "title": "Python Basics", "author": "Real P.", "pages": 635},
    {"id": 2, "title": "Breaking the Rules", "author": "Stephen G.", "pages": 99},
    {"id": 3, "title": "Breaking the Data", "author": "Stephen F.", "pages": 100},
    {"id": 4, "title": "Breaking the rule1", "author": "Stephen L.", "pages": 200},
]

# class based approach
class Book(BaseModel):
    title: str
    author : str
    pages : int

# skridt no 3 : definere en rute ved hjælp af app.get() dekoratoren
@app.get("/books")
def get_books():
    return books    

@app.get("/books/{id}") 
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    return {"message": "Book not found"}

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

@app.get("/books/search")
def search_books(query: str):
    results = []
    for book in books:
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            results.append(book)
    return results

@app.get("/books/sort")
def sort_books(by: str):
    if by == "title":
        sorted_books = sorted(books, key=lambda x: x["title"])
    elif by == "author":
        sorted_books = sorted(books, key=lambda x: x["author"])
    elif by == "pages":
        sorted_books = sorted(books, key=lambda x: x["pages"])
    else:
        return {"message": "Invalid sort parameter"}
    return sorted_books
