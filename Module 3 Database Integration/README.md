# Module 3: Database Integration – Digital Nurture 5.0

This directory contains implementation files, scripts, and SQL schemas for **Module 3: Database Integration**, part of the **Digital Nurture 5.0 – Python Full Stack Engineer Track**.

It covers relational database design, query optimization, advanced SQL, NoSQL document modeling, Python ORM integration (SQLAlchemy), and database schema migrations (Alembic).

---

# Repository Structure

```
Module 3 Database Integration/
└── Vishal S/
    ├── README.md              # Dedicated Database Integration README
    ├── hands_on_1/
    │   └── hands_on_1.sql     # Relational Schema Design & DDL
    ├── hands_on_2/
    │   └── hands_on_2.sql     # CRUD (DML) & Basic SQL Queries
    ├── hands_on_3/
    │   └── hands_on_3.sql     # Advanced SQL (Subqueries, Views, Triggers, CTEs)
    ├── hands_on_4/
    │   └── hands_on_4.sql     # Query Performance & Indexing Optimization
    ├── hands_on_5/            # MongoDB NoSQL
    │   └── mongodb_queries.js # Document Modeling, CRUD & Aggregations
    ├── hands_on_6/            # Python ORM (SQLAlchemy)
    │   ├── models.py          # SQLAlchemy Models & Table Creation
    │   ├── crud.py            # CRUD Operations & N+1 Problem Demo
    │   └── requirements.txt   # Dependencies
    ├── hands_on_7/            # Schema Migrations (Alembic)
    │   ├── alembic.ini        # Migration Configurations
    │   ├── models.py          # Updated models with Alembic track
    │   ├── crud.py            # Database verification scripts
    │   ├── migrations/        # Generated Migration Revisions
    │   └── requirements.txt   # Dependencies
    └── python/                # Standalone Python Verification Scripts
        ├── n_plus_one_demo.py # Raw MySQL N+1 demonstration
        └── optimized_join.py  # Raw MySQL JOIN performance optimization
```

---

# Technologies & Tools Used

### Relational Database
- **MySQL 8.x**: For relational schema design, querying, indexing, and transactional operations.

### NoSQL Database
- **MongoDB**: For document-based data modeling, nested array/object queries, and aggregation pipelines.

### Python Libraries & Frameworks
- **SQLAlchemy (Core & ORM)**: Object-Relational Mapper for Python.
- **Alembic**: Database migrations tool for SQLAlchemy.
- **PyMySQL**: Python MySQL driver.
- **mysql-connector-python**: Official driver for raw MySQL interactions.

---

# Detailed Hands-On Breakdown

## Hands-On 1: Database Design & DDL Setup
- **Objective**: Design a normalized relational schema for a college management database.
- **Key Implementations**:
  - Structured tables: `departments`, `students`, `courses`, `enrollments`, and `professors`.
  - Defined constraints: `PRIMARY KEY`, `FOREIGN KEY` references, `UNIQUE`, `NOT NULL`, and `DEFAULT` options.
  - Set up auto-increment identifiers to manage relational records.

## Hands-On 2: DML & SQL Querying
- **Objective**: Manipulate database records and query relational data.
- **Key Implementations**:
  - Inserted rich mock datasets across all entities.
  - Executed updates and conditional deletes to maintain database integrity.
  - Written queries utilizing `WHERE` filters, `ORDER BY` sorting, `INNER JOIN`, and `LEFT JOIN`.
  - Implemented aggregations using `COUNT`, `SUM`, `AVG`, `GROUP BY`, and `HAVING` filters.

## Hands-On 3: Advanced SQL (Subqueries, Views, Triggers, CTEs)
- **Objective**: Solve complex querying scenarios and define automatic execution rules.
- **Key Implementations**:
  - **Subqueries & CTEs**: Designed nested queries to isolate students with above-average enrollment workloads and courses with universal criteria.
  - **Database Views**: Built reusable view schemas mapping student details to enrollment profiles.
  - **Triggers**: Configured database-level validation to track seat limits and audit course records on update.

## Hands-On 4: Database Optimization & Indexing
- **Objective**: Identify query performance bottlenecks and implement optimization strategies.
- **Key Implementations**:
  - Used `EXPLAIN FORMAT=JSON` to analyze execution plans and cost parameters.
  - Tracked Full Table Scan operations on non-indexed query parameters (like `enrollment_year`).
  - Added targeted column indexes (`idx_students_enrollment_year`, `idx_course_code`) and unique multi-column indexes (`idx_enrollment_student_course`).
  - Compared execution metrics to prove reduction in query engine search cost and table scan operations.

## Hands-On 5: Document-Oriented NoSQL (MongoDB)
- **Objective**: Model unstructured course feedback data using document collections.
- **Key Implementations**:
  - Created document schema with nested array tags and attachment sub-documents.
  - Performed Mongo CRUD operations including complex array updates (`$push`, `$pull`).
  - Executed multi-stage Aggregation Pipelines utilizing `$match`, `$group`, `$project`, `$unwind`, and `$lookup` (referencing and joining collections).

## Hands-On 6: SQLAlchemy ORM & The N+1 Query Problem
- **Objective**: Integrate MySQL with Python applications through ORM mapping and resolve performance vulnerabilities.
- **Key Implementations**:
  - Defined Python class mappings for relational schemas using `declarative_base`.
  - Configured relationships with bidirectional syncing using `relationship` and `back_populates`.
  - Demonstrated how lazy loading triggers the **N+1 query problem** (1 query for parent records, plus N additional queries for nested records).
  - Resolved the performance issue by applying eager loading with SQLAlchemy's `joinedload()`, forcing a single unified SQL JOIN query.

## Hands-On 7: Schema Migrations with Alembic
- **Objective**: Manage incremental database schema evolutions using version-controlled migrations.
- **Key Implementations**:
  - Setup and configured `alembic` configurations (`alembic.ini`, `env.py`).
  - Automated schema migration creation using Alembic's `--autogenerate` revisions.
  - Altered the live database schema (added `is_active` boolean column, created new `CourseSchedule` relational tables).
  - Performed migration verification tests by executing rollbacks (`downgrade -1`, `downgrade base`) and restoring to HEAD version (`upgrade head`).

---

# How to Run & Verify

### Running MySQL Scripts
Navigate to the hands-on directory and execute the SQL file:
```bash
# Hands-On 1
cd "Module 3 Database Integration/Vishal S/hands_on_1"
mysql -u root -p college_db < hands_on_1.sql

# Hands-On 2
cd "../hands_on_2"
mysql -u root -p college_db < hands_on_2.sql

# Hands-On 3
cd "../hands_on_3"
mysql -u root -p college_db < hands_on_3.sql

# Hands-On 4
cd "../hands_on_4"
mysql -u root -p college_db < hands_on_4.sql
```

### Running MongoDB Scripts
Navigate to hands_on_5 and run:
```bash
cd "Module 3 Database Integration/Vishal S/hands_on_5"
mongosh mongodb://localhost:27017 mongodb_queries.js
```

### Running SQLAlchemy & Alembic Migrations
1. Navigate to the relevant Hands-On directory:
   ```bash
   cd "Module 3 Database Integration/Vishal S/hands_on_6"
   # Or
   cd "Module 3 Database Integration/Vishal S/hands_on_7"
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the migrations/verification scripts:
   ```bash
   # Run SQLAlchemy Table Creation/CRUD
   python models.py
   python crud.py

   # Apply Alembic Migrations
   python -m alembic upgrade head
   ```

---

# Student Info

- **Name:** Vishal S
- **Course:** Digital Nurture 5.0 – Python Full Stack Engineer Track
