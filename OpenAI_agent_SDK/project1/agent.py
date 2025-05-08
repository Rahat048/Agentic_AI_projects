import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

from dotenv import load_dotenv
import os

load_dotenv()

or_api_key = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

set_tracing_disabled(disabled=True)

client = AsyncOpenAI(
    api_key=or_api_key,
    base_url=BASE_URL
)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in english.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent,
        "pakistan's largest city name?.",
    )
    print(result.final_output)

# run async function properly
if __name__ == "__main__":
    asyncio.run(main())
