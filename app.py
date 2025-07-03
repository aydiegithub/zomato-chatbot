import chainlit as cl
from src.llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    # Add user message to conversation
    messages.append({"role": "user", "content": message.content})

    # Call OpenAI with the latest user message only
    response = ask_order(message.content)

    # Add assistant's reply to conversation history
    messages.append({"role": "assistant", "content": response})

    # Send the reply to the Chainlit frontend
    await cl.Message(
        content=response,
    ).send()