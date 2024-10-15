import json
import requests

from bs4 import BeautifulSoup
from typing import List, Dict, Any, Union
from urllib.parse import quote_plus

class MiniGroqqle:
    def __init__(self, num_results: int = 10):
        self.num_results = num_results
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

    def search(self, query: str, json_output: bool = False) -> Union[List[Dict[str, Any]], str]:
        encoded_query = quote_plus(query)
        search_url = f"https://www.google.com/search?q={encoded_query}&num={self.num_results * 2}"
        
        try:
            response = requests.get(search_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            search_results = []
            for g in soup.find_all('div', class_='g'):
                anchor = g.find('a')
                title = g.find('h3').text if g.find('h3') else 'No title'
                url = anchor.get('href', '') if anchor else ''
                
                description = ''
                description_div = g.find('div', class_=['VwiC3b', 'yXK7lf'])
                if description_div:
                    description = description_div.get_text(strip=True)
                else:
                    description = g.get_text(strip=True)
                
                if url.startswith('http'):
                    search_results.append({
                        'title': title,
                        'description': description,
                        'url': url
                    })
            
            results = search_results[:self.num_results]
            
            if json_output:
                return json.dumps(results, indent=2)
            else:
                return results
        except requests.RequestException as e:
            error_message = f"Error performing search: {str(e)}"
            if json_output:
                return json.dumps({"error": error_message})
            else:
                return [{"error": error_message}]

# Example usage
if __name__ == "__main__":
    searcher = MiniGroqqle(num_results=5)
    results = searcher.search("Python programming")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Description: {result['description']}")
        print("---")