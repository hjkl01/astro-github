import asyncio
import json
from crawlee.crawlers._beautifulsoup import BeautifulSoupCrawler
from crawlee.proxy_configuration import ProxyConfiguration


async def scrape_github_trending():
    repos = []

    async def handler(context):
        soup = context.soup

        # Find all repository articles
        repo_articles = soup.find_all("article", class_="Box-row")

        for article in repo_articles:
            try:
                # Repository name and link
                h2_elem = article.find("h2", class_="h3")
                if not h2_elem:
                    continue
                repo_link = h2_elem.find("a")
                if not repo_link:
                    continue
                href = repo_link.get("href")
                if not href:
                    continue
                href_str = str(href)
                repo_name = href_str.strip("/")
                repo_url = f"https://github.com{href_str}"

                # Description
                desc_elem = article.find("p", class_="col-9")
                description = desc_elem.text.strip() if desc_elem else ""

                # Language
                lang_elem = article.find("span", itemprop="programmingLanguage")
                language = lang_elem.text.strip() if lang_elem else ""

                # Stars and Forks
                stats = article.find_all("a", class_="Link--muted")
                stars = ""
                forks = ""
                for stat in stats:
                    href_stat = stat.get("href", "")
                    if href_stat and "stars" in href_stat:
                        stars = stat.text.strip()
                    elif href_stat and "forks" in href_stat:
                        forks = stat.text.strip()

                # Today's stars
                today_stars_elem = article.find("span", class_="d-inline-block float-sm-right")
                today_stars = today_stars_elem.text.strip() if today_stars_elem else ""

                repo_info = {
                    "name": repo_name,
                    "url": repo_url,
                    "description": description,
                    "language": language,
                    "stars": stars,
                    "forks": forks,
                    "today_stars": today_stars,
                }
                repos.append(repo_info)

            except Exception as e:
                print(f"Error parsing repo: {e}")
                continue

    proxy_config = ProxyConfiguration(proxy_urls=["http://localhost:7890"])
    crawler = BeautifulSoupCrawler(proxy_configuration=proxy_config)
    crawler.router.default_handler(handler)

    await crawler.add_requests(
        [
            "https://github.com/trending",
            "https://github.com/trending/python",
            "https://github.com/trending/lua",
            "https://github.com/trending/go",
            "https://github.com/trending/rust",
            "https://github.com/trending/javascript",
        ]
    )
    await crawler.run()

    return repos


if __name__ == "__main__":
    trending_repos = asyncio.run(scrape_github_trending())
    urls = list(set([trending_repo["url"] for trending_repo in trending_repos]))
    for url in urls:
        with open("./urls.txt", "a") as f:
            f.write(f"{url}\n")
    # print(json.dumps(trending_repos, indent=4, ensure_ascii=False))

    # Optionally save to file
    # with open("trending_repos.json", "w", encoding="utf-8") as f:
    #     json.dump(trending_repos, f, indent=4, ensure_ascii=False)
    print("Data saved to trending_repos.json")
