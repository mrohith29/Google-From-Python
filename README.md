# Google-From-Python
You can learn how to make google search using python using this repo.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install googlesearch.

<!-- ```bash -->

    pip install googlesearch

<!-- ```  -->

## Usage

```python

from googlesearch import search

query = "Geeksforgeeks"

for url in search(query, tld="com", num=10, stop=10, pause=2):
    print(url)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

