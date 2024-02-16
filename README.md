# PostgreSQL Function and View DDL Extractor

This script is designed to extract the Data Definition Language (DDL) source code of user-defined functions and views from a PostgreSQL database. It organizes the extracted functions and views into separate directories based on their schemas.

## Requirements

- Python 3.x
- `psycopg2` library (for connecting to PostgreSQL)

## Usage

1. Install the `psycopg2` library if you haven't already:

   ```bash
   pip install psycopg2
   ```

2. Configure the scripts:
    
    When you run the scripts (`extract_function_ddl.py` and `extract_view_ddl.py`), they will prompt you to enter the following PostgreSQL connection parameters:

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

    **Note:** The scripts will use the provided values for establishing a connection to the PostgreSQL database.

3. Run the scripts:

   - For extracting function DDLs:

     ```bash
     python extract_function_ddl.py
     ```

   - For extracting view DDLs:

     ```bash
     python extract_view_ddl.py
     ```

4. The scripts will connect to the PostgreSQL database, retrieve the DDL source code of user-defined functions/views, and organize them into separate directories based on their schemas within directories named `function_ddl_files` and `view_ddl_files` respectively.

## Directory Structure

- `function_ddl_files/`: The main directory where function DDL source files are organized by schema.
  - `<schema_name>/`: Subdirectories for each schema, containing function DDLs.
    - `<function_name>.sql`: DDL source files for each user-defined function.

- `view_ddl_files/`: The main directory where view DDL source files are organized by schema.
  - `<schema_name>/`: Subdirectories for each schema, containing view DDLs.
    - `<view_name>.sql`: DDL source files for each view.

## Example Output

After running the scripts, you will have directory structures similar to the following:

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

view_ddl_files/
├── public/
│   ├── view1.sql
│   ├── view2.sql
│   └── ...
├── schema2/
│   ├── view3.sql
│   ├── view4.sql
│   └── ...
└── ...
```