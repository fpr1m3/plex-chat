# plex-chat
Local LLM powered chat with tools to work with Plex Media Server

## Install
I recommend using a virtual environment to keep things nice and happy. I'm using `python 3.12` as one of the packages complains on `3.13`.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You will need to get Plex token. I ended up following the instructions [here](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/).

## Usage

```bash
python src/main.py --prompt "What shows do we have that have America in the name?"
```

## Known limitations
* So currently I'm working on the assumption that your libraries are going to be the same number as mine. Really not the way to be doing it, ideally we can use the `plexapi` to query the server for it's different sections and setup accordingly. If you need to set your TV or Movies library to be a different number, you can do that in `src/tools/plex.py` in the `Init()` function.

* I write really crap code, so there's going to be so much that can be added and changed... I'll get to that eventually.

## Shoutouts
There's a few projects that without which this would've been so much harder and would've made me nope out:

* [python-plexapi](https://github.com/pkkid/python-plexapi) - Huge shoutout for this complete package
* [langgraph](https://github.com/langchain-ai/langgraph) - You know 'em, you love 'em.
* [langchain](https://github.com/langchain-ai/langchain) - Same here, big thanks for all this package does
* [ollama](https://github.com/ollama/ollama) - Couldn't forget the backend!