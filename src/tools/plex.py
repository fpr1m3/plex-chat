import os
from plexapi.myplex import MyPlexAccount
from langchain_core.tools import tool

_plex = None
_movies = None
_tv = None

def Init(server_name: str):
    global _tv
    global _movies
    global _plex
    print("Logging into Plex...")
    account = MyPlexAccount(token=os.getenv("PLEX_TOKEN"))
    _plex = account.resource(server_name).connect()
    _movies = _plex.library.sectionByID(1)
    _tv = _plex.library.sectionByID(2)
    print("Plex setup complete")

@tool
def mostRecentlyAddedTVShows(howMany: int = 5) -> str:
    """Return the most recently added TV Shows

    Args:
        howMany: How many TV shows you want to have listed? Default to 5
    """
    print("Checking most recent TV shows...")
    episodes = _tv.recentlyAddedEpisodes(maxresults=howMany)
    returnList = ["Here's the recently added TV Shows:"]
    for episode in episodes:
        returnList.append(f'{episode.show().title} - Season {episode.seasonNumber} - Episode #{episode.episodeNumber}: {episode.title}')
    return '\n'.join(returnList)

@tool
def searchForTVShow(searchTerm: str, maxResults: int = 5) -> str:
    """Return a list of shows based on a search term.
     If nothing is found, it will return nothing.
     If it returns something, match it with what the  user is looking for.

    Args:
        searchTerm: What you want to search for?
        maxResults: How many results do you want? Default 5
    """
    print("Searching for TV Show...")
    shows = _tv.search(title=searchTerm, sort="titleSort:desc", maxresults=maxResults, libtype='show')
    returnList = ["Shows matching your query:"]
    for show in shows:
        returnList.append(f'{show.title}')
    return '\n'.join(returnList)

@tool
def updateTVShowsLibrary():
    """Sync the TV Shows library with the hard drive"""
    print("Updating TV Shows...")
    _tv.update()

@tool
def updateMoviesLibrary():
    """Sync the Movies library with the hard drive"""
    print("Updating Movies...")
    _movies.update()

PLEX_TOOLS = [mostRecentlyAddedTVShows, searchForTVShow, updateMoviesLibrary, updateTVShowsLibrary]