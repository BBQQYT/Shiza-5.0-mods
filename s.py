import requests
from bs4 import BeautifulSoup

def get_mod_info(mod_name):
    base_url = "https://www.curseforge.com"
    search_url = f"{base_url}/minecraft/mc-mods/{mod_name}/files/all"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    mod_links = soup.find_all("a", class_="project-avatar")
    
    for link in mod_links:
        project_id = link.get("data-id")
        print(f"Мод: {mod_name}, ProjectID: {project_id}")

# Пример использования:
mod_names = ["mod1", "mod2", "mod3"]  # Замените этот список названиями ваших модов

for mod_name in mod_names:
    get_mod_info(mod_name)
