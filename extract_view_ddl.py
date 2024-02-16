import psycopg2
import os
import codecs
import re


def clean_filename(filename):
    # Invalid characters
    invalid_chars = re.compile(r'[\/:*?"<>|]')

    cleaned_filename = re.sub(invalid_chars, "", filename)

    return cleaned_filename


def main():
    db_params = {
        "host": input("Enter database host:\n"),
        "port": input("Enter database port:\n"),
        "user": input("Enter username:\n"),
        "password": input("Enter password:\n"),
        "dbname": input("Enter database name:\n"),
    }

    # SQL query to retrieve view DDL
    query = """
        SELECT 
            schemaname,
            viewname,
            definition AS viewddl
        FROM pg_views;
    """

    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        cur.execute(query)

        function_data = cur.fetchall()

        # Create and save .sql files in separate schema directories
        for function_row in function_data:
            schemaname, viewname, viewddl = function_row
            
            # Clean invalid characters
            schemaname = clean_filename(schemaname)
            viewname = clean_filename(viewname)
            
            schema_directory = os.path.join("view_ddl_files", schemaname)
            
            os.makedirs(schema_directory, exist_ok=True)
            if len(viewname) > 200:
                filename = os.path.join(
                    schema_directory, f"{viewname[:200] + '...'}.sql"
                )
            else:
                filename = os.path.join(schema_directory, f"{viewname}.sql")
            with codecs.open(filename, mode="w", encoding="utf-8") as sql_file:
                sql_file.write(viewddl)

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
