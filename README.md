
# SQLite Database Learning and Experimentation with Python

This repository is dedicated to learning and experimentation with the SQLite database using Python. It covers the basics of connecting to an SQLite database, executing SQL commands, and performing common database operations such as creating tables, inserting data, querying, updating, and deleting records.

## Description

SQLite is a lightweight, serverless database that stores data in a local file. This repository contains Python code for interacting with SQLite using the `sqlite3` module, providing examples and explanations to help you understand how to work with databases in Python.

## Commands

### Installation (Linux)

To install SQLite3 on a Linux-based system, use the following command:

```bash
sudo apt install sqlite3
```

### Check SQLite Version

To check the version of SQLite installed, run the following command:

```bash
sqlite3 --version
```

### Python Code to Connect to SQLite Database

You can connect to an SQLite database using Python’s built-in `sqlite3` module. If the database file doesn't exist, SQLite will create it for you.

```python
import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Close the connection when done
connection.close()
```

### Basic Commands and Operations

- **Connecting to a Database**: `sqlite3.connect('your_database.db')`
- **Creating a Table**:

```python
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
```

- **Inserting Data**:

```python
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
connection.commit()
```

- **Querying Data**:

```python
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)
```

- **Updating Data**:

```python
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (31, 'Alice'))
connection.commit()
```

- **Deleting Data**:

```python
cursor.execute('DELETE FROM users WHERE name = ?', ('Alice',))
connection.commit()
```

## Useful Links

- [How to Use SQLite3 Module in Python 3 (DigitalOcean)](https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3)
- [Python Package Index: `names`](https://pypi.org/project/names/)

These resources provide additional tutorials and packages that can enhance your SQLite experience and Python development.

## Contribution

Feel free to fork the repository and submit pull requests with any improvements, additional examples, or bug fixes. Contributions to enhance the understanding of SQLite and Python are welcome!

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

