import os
import argparse
from dotenv import load_dotenv
from langchain_core.globals import set_debug
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from utils.sanity import CheckEnvironment
from tools.plex import Init, PLEX_TOOLS
from prompts.system import PLEX_SYSTEM_PROMPT_STRING

def main():
    parser = argparse.ArgumentParser(description='Plex Chat - Chat with your Plex Library')
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode',
        default=False
    )
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Prompt for the Plex server"
    )
    args = parser.parse_args()
    set_debug(args.debug)
    # Load .env file
    load_dotenv()
    # Ollama things
    model = os.getenv("MODEL")
    server_url = os.getenv("SERVER_URL")
    context_size = os.getenv("CTX")
    # Hashtag Plex things
    plex_server_name = os.getenv("PLEX_SERVER_NAME")
    # Check environment, right now it's just if the model is there
    if not CheckEnvironment(model):
        print("Sorry something is wrong with the environment. Check the log")
    # Init the Plex API
    Init(plex_server_name)
    # This should allow us to use the tools as well. So let's get to work!
    model = ChatOllama(model=model, temperature=0, base_url=server_url, num_ctx=context_size)
    agent_executor = create_react_agent(model, PLEX_TOOLS, state_modifier=PLEX_SYSTEM_PROMPT_STRING)
    for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content=args.prompt)]},
        stream_mode="values",
    ):
        message = chunk["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

if __name__ == '__main__':
    main()