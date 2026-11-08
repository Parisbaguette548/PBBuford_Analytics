import os
import glob
import pandas as pd
from sqlalchemy import create_engine

DB_USER = "macbookpro"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "pbbuford"

engine = create_engine(
    f"postgresql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

csv_folder = "/Users/macbookpro/Desktop/sample"

csv_files = glob.glob(os.path.join(csv_folder, "*.csv"))

for file_path in csv_files:

    print(f"Processing {os.path.basename(file_path)}")

    df = pd.read_csv(file_path, header=None)
    
    header = df.iloc[0]

    order_no = header[1]
    customer_no = header[3]
    order_date = header[4]
    delivery_date = header[5]
    supplier = df.iloc[1][1]
    delivery_status = header[13]

    current_category = None

    rows = []

    for _, row in df.iterrows():

        record_type = str(row[0])

        if record_type == "C":
            current_category = row[1]

        elif record_type == "P":

            rows.append(
                {
                    "order_no": order_no,
                    "customer_no": customer_no,
                    "order_date": order_date,
                    "delivery_date": delivery_date,
                    "supplier": supplier,
                    "category": current_category,
                    "item_no": row[1],
                    "case_qty": row[2],
                    "split_qty": row[3],
                    "pack_size": row[5],
                    "brand": row[6],
                    "description": row[7],
                    "manufacturer_no": row[8],
                    "per_lb_flag": row[9],
                    "case_price": row[10],
                    "each_price": row[11],
                    "delivery_status": delivery_status,
                    "source_file": os.path.basename(file_path)
                }
            )

    bronze_df = pd.DataFrame(rows)
    print("CSV rows:", len(bronze_df))
    print("Processed rows:", len(rows))
    print("test")
    print(bronze_df.head())

    bronze_df.to_sql(
        "bronze_sysco_orders",
        engine,
        if_exists="append",
        index=False
    )

    # print(f"{len(bronze_df)} rows loaded")

print("Load completed")