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
    
    Open the script file (`extract_function_ddl.py`) and set the following PostgreSQL connection parameters:

     ```python
     db_params = {
         "dbname": "database_name",
         "user": "database_username",
         "password": "database_password",
         "host": "database_host",
         "port": "database_port"
     }
     ```

    Replace `"database_name"`, `"database_username"`, `"database_password"`, `"database_host"`, and `"database_port"` with the actual PostgreSQL connection details.

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