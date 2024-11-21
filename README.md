# progarchivespy


[![Package CI](https://github.com/NCatalani/progarchivespy/actions/workflows/python-package.yml/badge.svg)](https://github.com/NCatalani/progarchivespy/actions/workflows/python-package.yml)[![Coverage Status](https://coveralls.io/repos/github/NCatalani/progarchivespy/badge.svg?branch=master)](https://coveralls.io/github/NCatalani/progarchivespy?branch=master)

`progarchivespy` exposes a Python API for interacting with ProgArchives' data through web scraping. It abstracts HTML parsing, providing high-level services to retrieve structured data as Python objects.

## Features

- **Fetch top albums**: Retrieve top progressive rock albums by subgenre, year, or popularity.
- **Scrape detailed album and artist information**: Access names, genres, ratings, and other metadata.
- **Serializable models**: Convert scraped data into structured Python objects.

## Quick Start

```python
from progarchivespy.client import ProgArchivesClient
from progarchives.common import Subgenre

# Initialize the client
client = ProgArchivesClient()

# Fetch top Symphonic Prog albums
top_albums = client.top_albums.query(subgenre=Subgenre.SYMPHONIC_PROG)

# Print album information
for album in top_albums:
    print(album.asdict)  # Serialize to a dictionary
```

## Features

### Implemented
- [x] **Top Albums**: Fetch top albums by subgenre, year, or popularity.

### Planned
- [ ] **Artist Pages**: Retrieve detailed artist information, including discography and biography.
- [ ] **Subgenre Pages**: Extract data about subgenres, including associated artists and albums.
- [ ] **Album Pages**: Access album details such as tracklists, release years, and reviews.

## Limitations

- No official API; relies on scraping.
- Subject to rate limits.
