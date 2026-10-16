import json
import requests

def fetch_top_repos(language="python", limit=5):
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch data from GitHub API")
        return

    data = response.json()
    repos = data.get("items", [])[:limit]
    
    results = []
    for repo in repos:
        results.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "description": repo["description"],
            "url": repo["html_url"]
        })

    # Save output to JSON
    with open("top_repos.json", "w") as f:
        json.dump(results, f, indent=4)
        
    print(f"Successfully saved top {limit} {language} repositories to top_repos.json")

if __name__ == "__main__":
    fetch_top_repos(language="python", limit=5)
