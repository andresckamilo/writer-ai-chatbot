
import writer as wf
import os
import uvicorn

def _run_model(model,content):
    import os
    from dotenv import load_dotenv
    from openai import OpenAI
    import instructor
    import logfire

    load_dotenv()

    logfire.configure(token=os.getenv("LOGFIRE_API_KEY"))

    client = instructor.patch(
        OpenAI(
        )
    )
    logfire.instrument_openai(client)

    return client.chat.completions.create(
        messages = content, 
        model=model,
        stream=True
    )

# Initialize the application state
wf.init_state(
    {"my_app": {"title": "CHAT ASSISTANT"}, 
     "conversation": [], "selected": 'a',
     "model": "gpt-3.5-turbo"}
)


def handle_simple_message(state, payload):
    state["conversation"].append({"role": "user", "content": payload["content"]})
    response = _run_model(state["model"],state["conversation"])

    state["conversation"].append({"role": "assistant", "content": ""})
    for rsp in response:
        state["conversation"][-1]["content"] += rsp.choices[0].delta.content or ""
        state["conversation"] = state["conversation"]
    # Explicitly setting the state to ensure the changes are detected

def handle_button_click(state):
    models = {
    "b": "gpt-3.5-turbo",
        "a": "gpt-4o",
    }
    state["model"] = models[state["selected"]]
    print(state["model"])
