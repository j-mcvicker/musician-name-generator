# musician_names
Generates a random list of bands/musicians via the Discogs API. For those critical times when you need a random list of band/musicians.

TO-DO:
- Fix output formatting to remove parentheticals + numbers for duplicate names (e.g. Nirvana (1), Nirvana (2))
- Build GUI
- Print characters that throw UnicodeErrorException
- Hide HTTPError from user
- Eliminate 'Various' from results
- Eliminate releases with multiple artists (for a more heterogenous/random list)
- Eliminate duplicate names generated from same call
