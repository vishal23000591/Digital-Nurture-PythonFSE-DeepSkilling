# Python Backend Frameworks – Digital Nurture 5.0

## Course Management API

A comprehensive backend development repository created as part of the **Digital Nurture 5.0 – Python Full Stack Engineer Track**.

This repository contains solutions for all **10 Hands-On Exercises** covering backend development using **Django, Flask, and FastAPI**. Each hands-on progressively enhances the Course Management API by introducing new backend concepts such as ORM, REST APIs, asynchronous programming, JWT authentication, REST best practices, and Microservices Architecture.

---

# Repository Structure

```
Python Backend Framework Solutions/
├── README.md
├── .gitignore
└── Python Backend Framework Solutions/
    └── Vishal S/
        ├── Python Backend Hands-on 01/
        ├── Python Backend Hands-on 02/
        ├── Python Backend Hands-on 03/
        ├── Python Backend Hands-on 04/
        ├── Python Backend Hands-on 05/
        ├── Python Backend Hands-on 06/
        ├── Python Backend Hands-on 07/
        ├── Python Backend Hands-on 08/
        ├── Python Backend Hands-on 09/
        └── Python Backend Hands-on 10/
```

Each hands-on contains its own implementation along with the required project files and dependencies.

---

# Technologies Used

### Programming Language

- Python 3.x

### Frameworks

- Django
- Django REST Framework
- Flask
- FastAPI

### ORM

- Django ORM
- SQLAlchemy
- Flask-SQLAlchemy

### Authentication

- JWT
- OAuth2 Concepts
- Passlib (bcrypt)
- python-jose

### Database

- SQLite

### API Testing

- Swagger UI
- Postman

### Libraries

- SQLAlchemy
- Requests
- Pydantic
- Uvicorn
- Flask Blueprint
- FastAPI Dependency Injection

---

# Common Project Scenario

The entire repository is based on a single project:

## Course Management API

The API manages

- Departments
- Courses
- Students
- Enrollments
- Authentication
- Microservices

The same project was progressively implemented using multiple Python backend frameworks to understand their architecture and development approaches.

---

# Hands-On 1

## Web Framework Foundations & Django Project Setup

### Objective

Understand web framework fundamentals and create the first Django application.

### Implemented

- Django Project Setup
- Django Application Creation
- Request–Response Cycle
- MVC vs MVT Architecture
- WSGI vs ASGI
- Middleware Concepts
- URL Routing
- Function-Based View
- Hello API Endpoint

### Learning Outcome

Developed a basic Django project and understood how HTTP requests travel through a Django application.

---

# Hands-On 2

## Django Models, ORM & Admin Interface

### Objective

Build the Course Management database using Django ORM.

### Implemented

- Department Model
- Course Model
- Student Model
- Enrollment Model
- Foreign Key Relationships
- Database Migrations
- Django ORM CRUD Operations
- Query Filtering
- Aggregation
- Django Admin Registration
- Admin Customization
- Search and Filters
- Enrollment Constraints

### Learning Outcome

Understood Django ORM, database migrations, and the Django Administration Interface.

---

# Hands-On 3

## Django REST API Development

### Objective

Create REST APIs using Django REST Framework.

### Implemented

- DRF Serializers
- APIView
- CRUD APIs
- URL Routing
- ViewSets
- Routers
- Custom Actions
- Student Enrollment Endpoint

### Learning Outcome

Built RESTful APIs using Django REST Framework and understood serializer-based API development.

---

# Hands-On 4

## Flask Application Structure

### Objective

Rebuild the Course Management API using Flask.

### Implemented

- Flask Project Structure
- Application Factory
- Configuration Class
- Blueprints
- Routing
- JSON Responses
- Request Validation
- Error Handling
- CRUD Endpoints

### Learning Outcome

Learned lightweight backend development using Flask and modular application architecture.

---

# Hands-On 5

## Flask with SQLAlchemy

### Objective

Integrate a database with the Flask application.

### Implemented

- Flask-SQLAlchemy
- Database Models
- Relationships
- ORM CRUD Operations
- Flask Migrations
- Database Queries
- Student Enrollment Queries

### Learning Outcome

Integrated SQLAlchemy ORM with Flask and connected REST APIs to a persistent database.

---

# Hands-On 6

## FastAPI Basics

### Objective

Build REST APIs using FastAPI.

### Implemented

- FastAPI Project Setup
- Pydantic Schemas
- Request Validation
- Response Models
- Path Parameters
- Query Parameters
- Swagger Documentation
- Async SQLAlchemy
- Dependency Injection
- CRUD Operations

### Learning Outcome

Learned modern asynchronous API development using FastAPI.

---

# Hands-On 7

## FastAPI CRUD & Documentation

### Objective

Complete the Course Management API using FastAPI.

### Implemented

- Complete CRUD Operations
- HTTP Status Codes
- Response Models
- HTTPException Handling
- Student APIs
- Enrollment APIs
- Background Tasks
- Email Simulation
- OpenAPI Customization
- Tags
- Endpoint Summaries

### Learning Outcome

Developed production-style FastAPI applications following REST conventions.

---

# Hands-On 8

## RESTful API Design Best Practices

### Objective

Improve the API by following REST design principles.

### Implemented

### REST Improvements

- Proper Resource Naming
- HTTP Method Verification
- PATCH Endpoint
- Correct Status Codes
- Location Header

### API Improvements

- API Versioning
- Pagination
- Filtering
- Search Endpoint
- Standard Error Responses

### Learning Outcome

Applied RESTful API design principles and improved API consistency and usability.

---

# Hands-On 9

## Authentication & Security

### Objective

Secure the FastAPI application using JWT authentication.

### Implemented

### User Management

- User Model
- Password Hashing using bcrypt
- Secure Password Storage

### Authentication

- User Registration
- JWT Login
- Token Generation
- Token Validation
- Protected Routes
- OAuth2 Concepts
- Current User Dependency

### Security

- CORS Configuration
- Password Verification
- Secure Authentication Flow

### Learning Outcome

Implemented secure authentication using JWT while following backend security best practices.

---

# Hands-On 10

## Microservices Architecture

### Objective

Understand Microservices Architecture by decomposing the Course Management API into independent services.

### Implemented

### Service Decomposition

- Course Service
- Student Service
- Auth Service Design
- Notification Service Design

### Independent Services

- Separate Flask Applications
- Separate Databases
- Independent Deployment

### Inter-Service Communication

- HTTP Communication using Requests
- Enrollment Verification
- Service Availability Handling
- 503 Error Handling

### API Gateway

- Request Routing
- Service Proxy
- Gateway Testing

### Architecture Concepts

- Monolith vs Microservices
- Synchronous Communication
- Asynchronous Communication
- RabbitMQ Concepts
- Kafka Concepts

### Learning Outcome

Built independent backend services communicating through HTTP and understood the API Gateway pattern.

---

# Core API Endpoints

## Course APIs

```
GET     /api/courses/
POST    /api/courses/
GET     /api/courses/{id}
PUT     /api/courses/{id}
PATCH   /api/courses/{id}
DELETE  /api/courses/{id}
```

---

## Student APIs

```
GET     /api/students/
POST    /api/students/
```

---

## Enrollment APIs

```
POST    /api/enrollments/
```

---

## Authentication APIs

```
POST    /api/v1/auth/register/
POST    /api/v1/auth/login/
```

---

# Project Features

- Django Web Development
- Flask Development
- FastAPI Development
- ORM Integration
- CRUD Operations
- Async Programming
- RESTful API Design
- API Versioning
- Pagination
- Filtering
- Search
- JWT Authentication
- Password Hashing
- OAuth2 Concepts
- Protected Endpoints
- API Documentation
- Background Tasks
- CORS Configuration
- Microservices
- API Gateway
- Inter-Service Communication

---

# Skills Acquired

During the completion of these hands-on exercises, the following backend development concepts were learned and implemented:

- Django Project Development
- Django ORM
- Django REST Framework
- Flask Architecture
- Flask Blueprints
- SQLAlchemy ORM
- FastAPI
- Pydantic
- Dependency Injection
- Async Programming
- OpenAPI Documentation
- REST API Design
- HTTP Standards
- JWT Authentication
- Password Hashing
- OAuth2 Concepts
- API Security
- Microservices Architecture
- API Gateway
- Service Communication
- Backend Project Organization

---

# How to Run

## Django Projects

```bash
python manage.py runserver
```

---

## Flask Projects

```bash
python app.py
```

---

## FastAPI Projects

```bash
uvicorn main:app --reload
```

---

# Testing

The APIs were tested using:

- Swagger UI
- Postman
- Browser
- Thunder Client

---

# Conclusion

This repository demonstrates the complete progression of backend development using Python frameworks, starting from Django fundamentals, moving through Flask and FastAPI development, implementing RESTful API design, securing APIs with JWT authentication, and finally building a Microservices-based architecture.

The hands-on exercises collectively provide practical experience in designing, developing, securing, documenting, and deploying modern backend applications.

---

# Student Info

- **Name:** Vishal S
- **Course:** Digital Nurture 5.0 – Python Full Stack Engineer Track

