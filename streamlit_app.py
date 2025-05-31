import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot")
def get_bot_response(user_input):
    user_input = user_input.lower()

    # Friendly greetings
    if "hi" in user_input or "hello" in user_input:
        return "Hello there!  Ask me anything fun or interesting!"
    elif "how are you" in user_input:
        return "I'm a bot, but I'm doing great! Thanks for asking "
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a wonderful day! "

    # Fun questions
    elif "joke" in user_input:
        return "Why did the computer go to the doctor? Because it had a virus! "
    elif "riddle" in user_input:
        return "Riddle: What has keys but can't open locks? \nAnswer: A piano!"
    elif "fact" in user_input:
        return "Fun Fact: A day on Venus is longer than its year!"

    # General knowledge
    elif "capital of japan" in user_input:
        return "The capital of Japan is Tokyo "
    elif "tallest building" in user_input:
        return "The tallest building is the Burj Khalifa in Dubai, standing at 828 meters!"

    # Space and science
    elif "sun" in user_input:
        return "The Sun is a star that provides light and heat to Earth."
    elif "moon" in user_input:
        return "The Moon is Earth's only natural satellite. It affects the tides on Earth."
    elif "planet" in user_input:
        return "There are 8 planets in our solar system. Earth is the third from the Sun."

    # Animals
    elif "fastest animal" in user_input:
        return "The cheetah is the fastest land animal, reaching speeds up to 120 km/h!"
    elif "largest animal" in user_input:
        return "The blue whale is the largest animal to have ever lived."

    # History
    elif "mahatma gandhi" in user_input:
        return "Mahatma Gandhi was a leader of India's independence movement known for nonviolent protest."
    elif "who discovered america" in user_input:
        return "Christopher Columbus is credited with discovering America in 1492."

    # Default fallback
    else:
        return "Hmm... I don’t know that yet. Try asking me about space, animals, facts, jokes, or history!"

# Streamlit app interface
st.set_page_config(page_title="Smart Chatbot", page_icon="")
st.title(" Smart & Fun Chatbot")
st.write("Chat with me! Ask questions, hear a joke, or learn a fun fact!")

# Input from user
user_input = st.text_input("You:", "")

# Show chatbot response
if user_input:
    response = get_bot_response(user_input)
    st.text_area("Bot:", value=response, height=100)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
