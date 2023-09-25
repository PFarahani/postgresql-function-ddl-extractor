import psycopg2
import os

def main():
    db_params = {
        "dbname": "database_name",
        "user": "database_username",
        "password": "database_password",
        "host": "database_host",
        "port": "database_port"
    }

    # SQL query to retrieve function DDL
    query = """
        SELECT 
            nspname AS schema_name,
            concat(proname, '(', pg_get_function_identity_arguments(p.oid), ')') AS function_name,
            pg_get_functiondef(p.oid) AS function_ddl
        FROM 
            pg_proc p
        JOIN 
            pg_namespace n ON p.pronamespace = n.oid
        WHERE 
            nspname NOT LIKE 'pg_%'
            AND nspname != 'information_schema'
            AND proisagg = FALSE;
    """

    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        cur.execute(query)

        function_data = cur.fetchall()

        # Create and save .sql files in separate schema directories
        for function_row in function_data:
            schema_name, function_name, function_ddl = function_row
            schema_directory = os.path.join("function_ddl_files", schema_name)
            os.makedirs(schema_directory, exist_ok=True)
            if len(function_name) > 200:
                filename = os.path.join(schema_directory, f"{function_name[:200] + '...'}.sql")
            else:
                filename = os.path.join(schema_directory, f"{function_name}.sql")
            with open(filename, mode="w") as sql_file:
                sql_file.write(function_ddl)

        print("DDL source files extracted successfully.")
        
    except Exception as e:
        print("An error occurred:", e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    main()