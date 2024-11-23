from setuptools import setup, find_packages

setup(
    name="plex-chat",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'langchain_community',
        'langchain_core',
        'langchain_ollama',
        'langgraph',
        'plexapi',
    ],
)