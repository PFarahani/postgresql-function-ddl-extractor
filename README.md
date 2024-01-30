# PostgreSQL Function DDL Extractor

This script is designed to extract the Data Definition Language (DDL) source code of user-defined functions from a PostgreSQL database. It organizes the extracted functions into separate directories based on their schemas.

## Requirements

- Python 3.x
- `psycopg2` library (for connecting to PostgreSQL)

## Usage

1. Install the `psycopg2` library if you haven't already:

   ```bash
   pip install psycopg2
   ```

2. Configure the script:
    
    When you run the script (`extract_function_ddl.py`), it will prompt you to enter the following PostgreSQL connection parameters:

    ```python
    db_params = {
        "host": input("Enter database host:\n"),
        "port": input("Enter database port:\n"),
        "user": input("Enter username:\n"),
        "password": input("Enter password:\n"),
        "dbname": input("Enter database name:\n"),
        }
    ```

    Simply respond to the prompts by entering the appropriate values for your PostgreSQL connection.

    **Note:** The script will use the provided values for establishing a connection to the PostgreSQL database.

3. Run the script:

   ```bash
   python extract_function_ddl.py
   ```

4. The script will connect to the PostgreSQL database, retrieve the DDL source code of user-defined functions, and organize them into separate directories based on their schemas within a directory named `function_ddl_files`.

## Directory Structure

- `function_ddl_files/`: The main directory where DDL source files are organized by schema.
  - `<schema_name>/`: Subdirectories for each schema, containing function DDLs.
    - `<function_name>.sql`: DDL source files for each user-defined function.

## Example Output

After running the script, you will have a directory structure similar to the following:

```
function_ddl_files/
├── public/
│   ├── function1.sql
│   ├── function2.sql
│   └── ...
├── schema2/
│   ├── function3.sql
│   ├── function4.sql
│   └── ...
└── ...
```