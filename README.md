# MiniGroqqle: Lightweight Web Search for Python

MiniGroqqle is a minimalist web search component that allows Python developers to easily integrate web search capabilities into their applications. With just a few lines of code, you can perform Google searches and retrieve structured results.

## Features

- Simple and lightweight
- Easy to integrate
- Customizable number of search results
- Returns structured data (title, URL, and description) for each result

## JSON Output

MiniGroqqle now supports JSON output for easy integration with JSON-based applications. To get results in JSON format, simply set the `json_output` parameter to `True` when calling the `search` method:

```python
from minigroqqle import MiniGroqqle

searcher = MiniGroqqle(num_results=3)
results = searcher.search("Python programming", json_output=True)

print(results)  # This will print a JSON string
```

When using JSON output, the results will be returned as a JSON-formatted string instead of a list of dictionaries. This makes it easy to parse and use the results in various applications or to send them over network protocols.

## Installation

To install MiniGroqqle and its dependencies, run:

```bash
pip install requests beautifulsoup4
```

Then, download the `minigroqqle.py` file and place it in your project directory.

## QuickStart

Here's how to quickly get started with MiniGroqqle in your Python application:

1. Import the MiniGroqqle class:

```python
from minigroqqle import MiniGroqqle
```

2. Create an instance of MiniGroqqle:

```python
searcher = MiniGroqqle(num_results=5)  # Specify the number of results you want
```

3. Perform a search:

```python
results = searcher.search("Python programming")
```

4. Process the results:

```python
for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Description: {result['description']}")
    print("---")
```

That's it! You now have web search capabilities in your Python application.

## Example

Here's a complete example that you can run:

```python
from minigroqqle import MiniGroqqle

searcher = MiniGroqqle(num_results=3)
results = searcher.search("Python programming")

for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Description: {result['description']}")
    print("---")
```

## Contributing

We welcome contributions to MiniGroqqle! Please feel free to submit issues, fork the repository and send pull requests!

## License

MiniGroqqle is released under the MIT License. Mention J. Gravelle in your code and documentation if you borrow any of this code.  He's kinda full of himself...

## Disclaimer

This tool is for educational purposes only. Make sure to comply with the terms of service of the search engine you're querying. Be mindful of rate limiting and respect the usage policies of the services you're accessing.