# Library Management System + Contact Book API

## Question 1: Library Database

A relational database for managing books, members, loans, and authors.

- View ERD: [Link to ERD Image]
- To run:
  ```bash
  mysql -u root -p < library.sql

Question 2: Contact Book API (FastAPI + MySQL)

A basic CRUD API to manage contacts.

Setup

pip install -r requirements.txt
uvicorn main:app --reload

Endpoints

GET /contacts

POST /contacts


Database

Run:

mysql -u root -p < contact_db.sql


