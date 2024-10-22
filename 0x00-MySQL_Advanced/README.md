# 0x00-MySQL_Advanced

This directory contains projects and tasks focused on advanced MySQL concepts as part of the ALX Software Engineering program. This project builds on foundational SQL knowledge and covers complex queries, optimization, and advanced database management techniques.

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Project Files](#project-files)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)

## Description

The **0x00-MySQL_Advanced** project introduces advanced MySQL concepts such as:
- Complex queries with multiple JOINs
- Subqueries and nested queries
- Stored procedures and functions
- Triggers
- Views
- Transactions
- Database optimization techniques
- Indexing and performance improvement strategies

This project is designed to enhance your ability to work with MySQL databases at a more sophisticated level, handling large datasets and optimizing queries for better performance.

## Learning Objectives

By completing this project, you should be able to:
- Write complex SQL queries involving multiple JOINs and subqueries
- Use advanced MySQL features like views, triggers, and stored procedures
- Implement database transactions and understand the ACID properties
- Optimize database queries using indexing techniques
- Manage database performance and optimize query execution plans

## Project Files

Here are the key files and scripts found in this project:

- **`0-setup.sql`**: Script to set up the initial database environment.
- **`1-advanced_select.sql`**: SQL queries that demonstrate advanced SELECT statements using multiple joins and subqueries.
- **`2-indexing.sql`**: SQL script for creating and managing indexes to optimize query performance.
- **`3-transactions.sql`**: SQL examples of implementing transactions in MySQL with COMMIT and ROLLBACK.
- **`4-views.sql`**: Example queries to create and manage views in MySQL.
- **`5-stored_procedures.sql`**: SQL script to create stored procedures and functions.
- **`6-triggers.sql`**: SQL script demonstrating the creation and management of triggers in MySQL.

## Installation

To run the scripts in this project, you need to have MySQL installed on your local machine.

### MySQL Installation

On Ubuntu:

```bash
sudo apt update
sudo apt install mysql-server
```

After installation, you can start the MySQL service:
```
sudo service mysql start
```
You can then log in to the MySQL shell:
```
mysql -u root -p
```
### Setting Up the Project

To set up the project, you can run the 0-setup.sql file, which will create the necessary database and tables.
```
mysql -u root -p < 0-setup.sql
```
### Usage

1. Clone the repository to your local machine:
```
git clone https://github.com/PreciousAitanun/alx-backend-storage.git
```

2. Navigate to the project directory:
```
cd alx-backend-storage/0x00-MySQL_Advanced
```

3. Run any of the SQL scripts to execute the tasks in your MySQL database. For example, to run the 1-advanced_select.sql script:
```
mysql -u root -p < 1-advanced_select.sql
```

4. Verify the results by querying your database to see the outcome of the script.
```
SELECT * FROM your_table;
```


Author

Nadira3

GitHub: Nadira3

ALX Software Engineering Program
