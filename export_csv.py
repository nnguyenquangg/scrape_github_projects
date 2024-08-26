import pandas as pd

async def export_csv(data):
    df = pd.DataFrame(data,columns=['name', 'description', 'language'])
    df.to_csv('github_repos.csv', index=False,)
    