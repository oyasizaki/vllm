from langflow.custom import Component
from langflow.io import MessageTextInput, StrInput, FloatInput, IntInput, Output
from langflow.schema import Message
import requests

class VLLMChatComponent(Component):
    display_name = "vLLM TinyLlama Chat"
    description = "Connects to local vLLM server using chat completions API"
    icon = "cloud"

    inputs = [
        MessageTextInput(
            name="user_message",
            display_name="User Message",
            info="The message to send to the chat model",
            value="Hello!"
        ),
        StrInput(
            name="api_url",
            display_name="vLLM API URL",
            info="The URL of the vLLM chat completions endpoint",
            value="http://localhost:8000/v1/chat/completions"  # Changed here
        ),
        StrInput(
            name="model_name",
            display_name="Model Name",
            info="Name of the model loaded in vLLM",
            value="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        ),
        IntInput(
            name="max_tokens",
            display_name="Max Tokens",
            info="Maximum tokens to generate",
            value=150,
            advanced=True
        ),
        FloatInput(
            name="temperature",
            display_name="Temperature",
            info="Controls randomness",
            value=0.7,
            advanced=True
        ),
    ]

    outputs = [
        Output(display_name="Response", name="output", method="chat"),
    ]

    def chat(self) -> Message:
        """Send chat message to vLLM and return response."""
        try:
            payload = {
                "model": self.model_name,
                "messages": [{"role": "user", "content": self.user_message}],
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
            }

            response = requests.post(
                self.api_url,
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=30
            )
            response.raise_for_status()

            result = response.json()
            reply = result["choices"][0]["message"]["content"]
            
            return Message(text=reply)

        except Exception as e:
            return Message(text=f"Error: {str(e)}")
