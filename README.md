# Sensitve Topic Mood Bot

Extend the mood bot (`rasa init`) to handle sensitive topics.
Detect sensitive topics using GPT. Via a custom action the `sensitive_topic_flag` gets set. The slot can be used to handle sensitive topics in the conversation.

## Prerequisites

Python >= 3.8

### Create Virtual Environment

``` shell
python -m venv venv
```

### Activate Virtual Environment

``` shell
source venv/bin/activate
```

## Installation

``` shell
pip install -r requirements.txt
```

## Enviroment Variables

[Openai API](https://platform.openai.com) needs API key from OpenAI as enviroment variables in `.env`:

``` shell
export OPENAI_API_KEY =
```

## Train

``` shell
rasa train
```

## Run

Start rasa action server:

``` shell
rasa run actions
```

Talk to the bot:

``` shell
rasa shell
```

## Show case

``` shell
Your input ->  hey                                                                                                                                          
Hey! How are you?
Your input ->  I don't feel very well, i do have a chronic pain, could you advise something?                                                                
Maybe you better talk to a human.
```
