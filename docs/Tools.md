**Plex Tools Documentation**
=====================================

### Most Recently Added TV Shows Tool (`mostRecentlyAddedTVShows`)

#### Description
This tool returns the most recently added TV shows to your Plex library. By default, it lists the 5 most recent additions.

#### Usage
```python
mostRecentlyAddedTVShows(howMany=10)
```
Replace `10` with the desired number of TV shows you want listed.

### Search for TV Show Tool (`searchForTVShow`)

#### Description
This tool allows you to search for specific TV shows in your Plex library. It returns a list of matching shows based on the provided search term.

#### Usage
```python
searchForTVShow(searchTerm="Game of Thrones", maxResults=10)
```
Replace `"Game of Thrones"` with the desired search term and `10` with the desired number of results.

### Update TV Shows Library Tool (`updateTVShowsLibrary`)

#### Description
This tool synchronizes your TV shows library with the hard drive, updating any changes or new additions.

#### Usage
```python
updateTVShowsLibrary()
```
No arguments are required for this tool.

### Update Movies Library Tool (`updateMoviesLibrary`)

#### Description
This tool synchronizes your movies library with the hard drive, updating any changes or new additions.

#### Usage
```python
updateMoviesLibrary()
```
No arguments are required for this tool.