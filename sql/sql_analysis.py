import pandas as pd
from sqlalchemy import create_engine

# CSV load karo
df = pd.read_csv("data/cleaned/healthcare_cleaned.csv")

# SQLite database create karo
engine = create_engine("sqlite:///healthcare.db")

# Data ko SQL table mein save karo
df.to_sql(
    "hospital_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into SQL!")