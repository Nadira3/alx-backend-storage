# 0x02. Redis Basics

## Project Overview

This project focuses on the basics of Redis, an in-memory data structure store, used as a database, cache, and message broker. It covers fundamental Redis commands, data types, and concepts essential for understanding how to work with Redis effectively.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Types](#data-types)
- [Commands](#commands)
- [Examples](#examples)
- [Contributions](#contributions)
- [License](#license)

## Installation

To get started with Redis, you need to have Redis installed on your machine. Follow the steps below for installation:

1. **Install Redis** (for Linux):
   ```bash
   sudo apt update
   sudo apt install redis-server
   ```

2. Start Redis server:
```
redis-server
```


3. Access Redis CLI:
```
redis-cli
```

## Usage

This project includes several scripts and examples to demonstrate how to interact with Redis. You can run the provided scripts in the Redis CLI to see the commands in action.

### Data Types

Redis supports several data types:

- **Strings**: The simplest data type, used to store text or binary data.

- **Lists**: Ordered collections of strings, allowing duplicate values.

- **Sets**: Unordered collections of unique strings.

- **Sorted Sets**: Similar to sets but with an associated score for each element, allowing sorted retrieval.

- **Hashes**: Collections of key-value pairs, ideal for representing objects.


### Commands

Here are some basic Redis commands you will learn in this project:

SET key value: Set the value of a key.

GET key: Retrieve the value of a key.

DEL key: Delete a key.

LPUSH key value: Add a value to the start of a list.

RPUSH key value: Add a value to the end of a list.

SADD key value: Add a member to a set.

ZRANGE key start stop: Return a range of members in a sorted set.


### Examples
```
Example 1: Storing a String

SET my_key "Hello, Redis!"
GET my_key
# Output: "Hello, Redis!"
```

Example 2: Working with Lists
```
LPUSH my_list "First Item"
RPUSH my_list "Last Item"
LRANGE my_list 0 -1
# Output: ["First Item", "Last Item"]
```

## Contributions

Contributions are welcome! If you would like to contribute to this project, please fork the repository and create a pull request.

## License

This project is licensed under the ALX Backend Curriculum
