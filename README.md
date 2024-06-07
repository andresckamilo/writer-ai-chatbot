# Writer.AI Chatbot Application

This application is built using the Writer.AI framework, a powerful new tool for creating web content with minimal coding and an intuitive front-end interface.

## Overview

This application features a chatbot that utilizes an OpenAI LLM. The chatbot can be easily extended to integrate with any other AI model, making it highly versatile and adaptable to various use cases.

## Features

- **Low-Code Development**: Leverage the Writer.AI framework to build and customize your chatbot with minimal coding effort.
- **Seamless Integration**: The chatbot is integrated with OpenAI, providing advanced conversational capabilities.
- **Extendable**: Easily extend the application to use different AI models according to your needs.

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/andresckamilo/writer-ai-chatbot.git
   cd writer-ai-chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```

### Running the Application

1. Start the Writer.AI framework:
   ```bash
   writer run chat-assistant
   ```

2. Access the application through the local URL provided in the terminal.

### Extending the Application

To extend the application to use a different AI model, follow these steps:

1. Update the integration code in `main.py` to connect to your preferred AI model's API.
2. Modify the chatbot's logic to handle the responses from the new model.
3. Test the chatbot to ensure it functions as expected with the new AI model.

## Contributing

We welcome contributions! Please fork this repository and submit pull requests to contribute to the project.

## License

This project is licensed under the MIT License.
