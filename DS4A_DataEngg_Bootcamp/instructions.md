# DS4A 2023 - Data Skills For All

## Retail Challenge for Data Engineers
<br>

#### Building an Intelligent Retail Analytics Chatbot in Streamlit 
<br>

### Background


    The retail industry is undergoing a digital transformation, and data-driven decision-making is at its core. A chatbot capable of answering real-time queries related to sales, marketing, customer service issues, and production can be a significant asset. This chatbot will not only provide answers about the proposed retail data, but also display the SQL query used to derive those answers, thereby ensuring transparency and reliability.


    Chatbots play a crucial role in the retail industry by enhancing customer experiences, streamlining operations, and boosting sales. Firstly, they provide immediate and personalized assistance to shoppers, leading to higher customer satisfaction and retention. For instance, a customer browsing an online clothing store can use a chatbot to receive real-time recommendations based on their preferences, sizes, and previous purchases. This interactive guidance helps replicate the in-store shopping experience and increases the likelihood of a purchase.


    Secondly, chatbots streamline routine tasks such as order tracking, returns, and FAQs. By automating these processes, retailers can save time and resources while maintaining consistency in customer interactions. For instance, a chatbot can handle inquiries about shipping status or return procedures, freeing up human agents to focus on more complex customer needs. This efficiency not only reduces operational costs, but also contributes to faster problem resolution, enhancing overall customer satisfaction.


    Lastly, chatbots excel at data collection and analysis. They can gather insights from customer interactions, such as preferences, complaints, and suggestions, which retailers can then use to improve products, services, and marketing strategies. For example, a grocery store chatbot could collect feedback on product quality and suggest improvements, leading to better offerings that cater to customer preferences. By harnessing these insights, retailers can make informed decisions that drive business growth and innovation.


    As a Data Engineer, your main goal in this challenge is to effectively identify and handle the data sources that are relevant for analytics in order to develop a user-friendly AI-powered chatbot for a retail organization. To accomplish this, please thoroughly review the provided instructions and assignment details to fully grasp the task ahead.


    To get a sense of the modern use of chatbots in the retail industry, read the below articles:


- [Retail’s chatbots are evolving, and bringing new challenges](https://www.retailbrew.com/stories/2023/02/14/retail-s-chatbots-are-evolving-and-bringing-new-challenges)
- [Chatbot tech boasts untapped opportunity for retail](https://www.retailcustomerexperience.com/news/chatbot-tech-boasts-untapped-opportunity-for-retail/)
- [Generative AI Chatbots in Retail: The Key to Boosting Sales and Driving Personalization](https://masterofcode.com/blog/generative-ai-in-retail)

<br>

### Objectives


    - Design and develop a chatbot in Streamlit that can interact with the retail database. You should upload the CSV files into a database (locally or Cloud) and create the corresponding tables. See the chatbot demo in the support material section below.

    - Enable the chatbot to answer questions related to sales, marketing, and production. It should create a query that might respond to the answer and run it on the database. (Be careful with possible SQL injections; the application should restrict DML operations such as DELETE, UPDATE, and so on). It’s recommended to use OpenAI API for this.

    - Implement a feature to display the SQL query used to fetch the data for answering the questions.

    - Display the relevant data in a data frame within the Streamlit app.

    - Ensure the chatbot is user-friendly and intuitive using the Streamlit chat widget.


### Data Description

    The provided **Big Supply Co. dataset** consists of information about orders, products, customers, departments, and product categories.

    - **Orders Table:** Contains details about individual orders, including customer ID, product ID, department ID, market, and various other attributes like order status, sales, and profit.

    - **Product Table:** Includes information about individual products, such as product ID, category ID, description, and price.

    - **Customers Table:** Holds data about customers, including their ID, city, country, and segment.

    - **Department Table:** Contains information about the department stores, including their ID and geographical coordinates.

    - **Categories Table:** Holds data about product categories, including their ID and name.

    The detailed description of each dataset field is in the file *BigSupplyCo_Data_Schema_vF* document.


### Support material

    - This is a guide on how the application can look. Feel free to give it your own style and design.

- [Chatbot Demo](https://www.youtube.com/watch?v=TvvEZN_EEpQ)

<br>

    - Streamlit applications for generative AI:
-  [Build powerful apps using generative AI & LLMs • Streamlit](https://streamlit.io/generative-ai)

<br>

    - Open AI Docs for developers:
-  [GPT - OpenAI API](https://platform.openai.com/docs/guides/gpt/chat-completions-api)

<br>

    - Code faster!:
-  [Step-by-Step: How to Setup Copilot Chat in VS Code (microsoft.com)](https://techcommunity.microsoft.com/t5/educator-developer-blog/step-by-step-how-to-setup-copilot-chat-in-vs-code/ba-p/3849227)
  
- [Cursor - The AI-first Code Editor](https://cursor.sh/)
