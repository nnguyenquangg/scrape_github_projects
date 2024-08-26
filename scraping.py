import aiohttp
from bs4 import BeautifulSoup
from export_csv import export_csv

async def scrape_github_projects(username):
    repos = []
    page = 1

    async with aiohttp.ClientSession() as session:
        while True:
            paginated_url =  f"https://github.com/{username}?page={page}&tab=repositories"
            print(paginated_url)
            async with session.get(paginated_url) as response:
                if response.status == 200:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    
                    repo_list = soup.find_all('li', class_='col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source')
                    if not repo_list:
                        break

                    for repo in repo_list:
                        name = repo.find('a', itemprop='name codeRepository').text.strip()
                        description = repo.find('p', itemprop='description').text.strip() if repo.find('p', itemprop='description') else 'No description'
                        language = repo.find('span', itemprop='programmingLanguage').text.strip() if repo.find('span', itemprop='programmingLanguage') else 'Not specified'
                        link = "https://github.com" + repo.find('a', itemprop='name codeRepository')['href']
                        repos.append({
                            'name': name,
                            'description': description,
                            'language': language,
                            'link': link
                        })

                    next_button = soup.find('a', class_='next_page')
                    if not next_button:
                        break

                    page += 1
                else:
                    print(f'Failed to retrieve the page. Status code: {response.status}')
                    break
        await export_csv(repos)
        return repos