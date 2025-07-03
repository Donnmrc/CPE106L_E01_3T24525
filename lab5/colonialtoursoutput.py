import sqlite3

def list_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    
    return [table[0] for table in tables if table[0] != 'sqlite_sequence']

def print_table_data(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    print(f"\n{'='*40}\nTable: {table_name}\n{'='*40}")
    if not rows:
        print("(No data)")
    else:
        # Calculate column widths
        col_widths = [max(len(str(col)), max((len(str(row[i])) for row in rows), default=0)) for i, col in enumerate(col_names)]
        # Print header
        header = " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(col_names))
        print(header)
        print("-" * len(header))
        # Print rows
        for row in rows:
            print(" | ".join(str(item).ljust(col_widths[i]) for i, item in enumerate(row)))
    conn.close()

if __name__ == "__main__":
    db_path = "colonial_tours.db"
    tables = list_tables(db_path)
    print("Tables in colonial_tours.db:")
    for table in tables:
        print_table_data(db_path, table)