import sys
import json
from minigroqqle import MiniGroqqle

def print_results(results):
    if isinstance(results, str):
        # Results are in JSON format
        parsed_results = json.loads(results)
        if "error" in parsed_results:
            print(f"Error: {parsed_results['error']}")
        else:
            for i, result in enumerate(parsed_results, 1):
                print(f"Result {i}:")
                print(f"Title: {result['title']}")
                print(f"URL: {result['url']}")
                print(f"Description: {result['description']}")
                print("---")
    else:
        # Results are in list format
        if results and "error" in results[0]:
            print(f"Error: {results[0]['error']}")
        else:
            for i, result in enumerate(results, 1):
                print(f"Result {i}:")
                print(f"Title: {result['title']}")
                print(f"URL: {result['url']}")
                print(f"Description: {result['description']}")
                print("---")

def main():
    if len(sys.argv) < 2:
        print("Usage: python test.py <search query> [--json]")
        sys.exit(1)

    json_output = "--json" in sys.argv
    search_query = " ".join(arg for arg in sys.argv[1:] if arg != "--json")

    searcher = MiniGroqqle(num_results=5)
    results = searcher.search(search_query, json_output=json_output)

    if json_output:
        print(results)  # Print raw JSON string
    else:
        print_results(results)

if __name__ == "__main__":
    main()