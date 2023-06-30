import os
import logging

import openai

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def request_gpt(message):
    # Set up the model and prompt
    model_engine = "text-davinci-003"

    prompt = """
    Imagine you are a bot for common usage. In certain cases, only a human can handle a conversation or provide support. Examples are:
    1. Sensitive or Personal Topics: If the conversation involves sensitive or personal topics such as mental health, trauma, or abuse, it may be inappropriate for a chatbot to handle the conversation.
    2. Legal or Medical Advice: Chatbots should not be used to provide legal or medical advice. These topics require specialized knowledge and expertise, and any advice given should be provided by a trained professional.
    3. Complex or Unique Situations: If the situation is complex or unique, LLM may not have the ability to handle it effectively. In these cases, a human with the necessary expertise and experience should handle the conversation.
    4. High-stakes Decisions: If the conversation involves high-stakes decisions such as financial investments or legal decisions, it may be inappropriate for a chatbot to handle the conversation. These decisions require careful consideration and expert advice.
    5. Emotional Support: If the user is seeking emotional support, a chatbot may not be able to provide the level of empathy and understanding required to help the user.

    The message of the user is: {message}

    Should a human handle the conversation for you? Just answer with yes or no
    """.format(message=message)
    logger.info(prompt)
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    logger.info(response)
    return response.strip().lower().split(",")[0].split(".")[0]
    
if __name__ == "__main__":
    request_gpt("I have a chronic pain, could you advise something?")