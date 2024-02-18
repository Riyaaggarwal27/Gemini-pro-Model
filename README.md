# Gemini-pro-LLM-Chatbot
This Streamlit application implements a chatbot that responds to SQL queries. It leverages the Gemini Pro LLM model for natural language understanding and generation.
The SQL Retriever Chatbot allows users to input SQL-related queries and receive responses in real-time. It utilizes the Google GenAI API for generating SQL queries based on the user's input.

KEY FEATURES:  
SQL Query Generation: Input a natural language SQL-related query, and the chatbot will generate the corresponding SQL query.

Database Interaction: The generated SQL query is executed against an SQLite database (users.db) containing tables such as user_details, products, and orders. The results of the query are displayed to the user.

Chat History: View the history of interactions between the user and the chatbot.

