#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas flask


# In[3]:


import pandas as pd

# Financial data summary (static for simplicity)
financial_data = {
    "Apple": {"Total Revenue": "-0.39%", "Net Income Growth": "-3.09%", "Cash Flow Growth": "-1.14%"},
    "Microsoft": {"Total Revenue": "11.28%", "Net Income Growth": "10.64%", "Cash Flow Growth": "16.86%"},
    "Tesla": {"Total Revenue": "9.87%", "Net Income Growth": "-16.63%", "Cash Flow Growth": "1.30%"}
}

def simple_chatbot(user_query):
    # Predefined responses
    if user_query == "What is the total revenue for Apple?":
        return f"Apple's total revenue growth is {financial_data['Apple']['Total Revenue']}."
    
    elif user_query == "How has net income changed for Tesla over the last year?":
        return f"Tesla's net income has changed by {financial_data['Tesla']['Net Income Growth']} over the last year."
    
    elif user_query == "What is the cash flow growth for Microsoft?":
        return f"Microsoft's cash flow from operations grew by {financial_data['Microsoft']['Cash Flow Growth']}."
    
    elif user_query == "Compare revenue growth between Apple and Microsoft.":
        return f"Microsoft's revenue growth ({financial_data['Microsoft']['Total Revenue']}) is higher than Apple's ({financial_data['Apple']['Total Revenue']})."
    
    else:
        return "Sorry, I can only provide information on predefined queries."

# Example usage
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot! Ask a question or type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print("Chatbot:", response)


# # Documentation
# 
# ## How it works:
# - The chatbot takes predefined queries and returns financial insights from our dataset.
# - It uses if-else conditions to match user input to stored responses.
# 
# ## Predefined queries it supports:
# - "What is the total revenue for Apple?"
# - "How has net income changed for Tesla over the last year?"
# - "What is the cash flow growth for Microsoft?"
# - "Compare revenue growth between Apple and Microsoft."
# 
# ## Limitations:
# - Only responds to predefined queries.
# - Does not process user-generated queries dynamically.
# - No integration with live financial data sources (e.g., SEC filings).

# In[ ]:




