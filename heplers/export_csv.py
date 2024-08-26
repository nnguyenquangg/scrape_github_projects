import pandas as pd
import os

async def export_csv(name,data):
    os.makedirs('export_files', exist_ok=True)
    df = pd.DataFrame(data,columns=['name', 'description', 'language'])
    df.to_csv(f"export_files/{name}_github_repos.csv", index=False,)
    