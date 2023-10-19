import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Big Supply Co",
    page_icon="📊",
)

st.title('Big Supply Co - Retail Analysis')

def intro():
    st.write("### Welcome to Big Supply Co, Info! 👋")
    st.sidebar.success("Select a page above.")

    st.markdown(
            """


            **👈 Select a page from the dropdown on the left** to see some data visualizations, talk to the chatbot, or take a step inside my brain as I made this web app.
        """)

    st.image('https://static.vecteezy.com/system/resources/previews/025/501/341/non_2x/sport-equipment-on-a-black-background-sports-equipment-on-a-black-background-sports-equipment-on-a-dark-background-ai-generated-free-photo.jpg')

def explanation():
    st.markdown(
            """
    # My Approach and Thinking

    The focus on this project was moreso utilizing LLMs and Streamlit's UI capabilities to build a chatbot, but I wanted to flex some data engineering skills too and incorporate a stack I've never used before.

    Specifically, the only guidelines for and outcomes of the project are as follows: Design and develop a user-friendly chatbot in Streamlit that interacts with a retail database, enabling it to answer questions on sales, marketing, and production. The chatbot should create and execute SQL queries on the database while also displaying the SQL query and relevant data in a Streamlit app.

    There are many ways one could approach this in a simpler way; just using the provided CSVs locally for the project, using a dbt seed, uploading files directly to S3 or Snowflake, the list goes on. However, I really wanted an opportunity to utilize Airflow, PostgreSQL, Docker, Airbyte, dbt, S3 buckets and a little AWS CLI. Luckily, most of these are open source tools too and all were free for my use-cases.

    By using all of these tools, I was able to not only do ETL, but also ELT and reinforce kimball datawarehousing methodologies, data contracts, and more. Granted, this process would be a terrible and roundabout way to model data for a product, but I learned a lot and had fun along the way.

    Ultimately, my recommendation would be to use dbt and a Snowflake data warehouse. Snowflake has acquired Streamlit so it has become a very strong pair and OpenAI has only solidified both of those tools. If I was feeling extra fun, I would set up Fivetran or Rivery to extract my Postgres data models to Snowflake and then use Snowpark for this. How many other tools can I add to make the most complicated ELT/ETL journey possible???

    You know what, I actually do like that idea better. So I did just that! Well, no new tools, just using Airbyte to load my Postgres models to Snowflake.

    High level breakdown of my process:

    Data Engineering:

    Step 1:
    Creating the environment (I prefer conda) and installing the packages:
    - Kubernetes
    - PostgreSQL
    - Airflow
    - dbt
    - Docker
    - Airbyte
    Specifics can be found in requirements.txt

    Step 2:
    Initiliaze my postgres db. Create myself as a non-superuser and then create a new inner database. Also added postgres files to gitignore. Initialized the db and created a schema. Learned a lot of psql commands too!
    """)

    st.image('./images/psql.png')

    st.markdown("""
    Step 3:
    Getting airflow setup with postgres. Running the webserver and enabling a DAG.

    Step 4:
    Initilizaing a dbt project and connecting to postgres.

    Step 5:
    Create an AWS account and create an S3 bucket.
    
    Step 6:
    Add CSVs to S3 buckets via Airflow.
                """)
                
    st.image('./images/airflow.png')

    st.markdown(""" 
    Step 7:
    Load data from S3 to PostgreSQL via Airbyte. I learned a lot about iam, policies and permissions, and even AWS CLI along the way. Airbyte was nice as it already had out of the box connections for S3 and Postgres.
    """)

    st.image('./images/airbyte.png')

    st.markdown("""          
    Step 8:
    Add the dbt_utils packages and in dbt start to create the staging, dim, and facts models. Then create the final datamodel. Some cleaning needed to be done like casting data types appropriately, renaming columns to stick to data contract names, logic to change certain fields like zipcode or creating booleans, and commenting out empty or non valuable columns. I also made a star schema diagram to help plan this all out.

    Step 9:
    Add in tests and source freshness, even though I will never add more data to this warehouse ever :)

    Step 10:
    Move Postgres models to Snowflake so I don't have to worry about any servers.

    UI:

    Step 1:
    Installing the packages:
    - Streamlit
    - OpenAI
    - Snowpark
    - Plotly

    Step 2:
    Create Streamlit python file and secrets file then add and test the Postgres connection.

    Step 3:
    Add chatbot! Which entailed a main file and a promps.py file for prompt engineering.

    Step 4:
    In dbt, I created a new metadata table with descriptions and datatypes. Used a dbt seed this time ;) And did a `--full-refresh` seed run whenever I would update the column names as I went.

    Step 5:
    Updated the prompts file as any hallucinations from the chatbot occured!

    Step 6:
    Add more fun visualizations including charts based on the chatbot's output. And some text boxes for executing database queries. But I had to consider security for DML operations and be careful with possible SQL injections. I had to restrict DML operations such as DELETE, UPDATE, and so on.

    Step 5:
    Deploy!
    """)

def visualizations():
    pass

def chatbot():
    import openai
    import re
    from prompts import get_system_prompt

    # # Initialize the chat messages history
    openai.api_key = st.secrets.OPENAI_API_KEY
    if "messages" not in st.session_state:
        # system prompt includes table information, rules, and prompts the LLM to produce
        # a welcome message to the user.
        st.session_state.messages = [{"role": "system", "content": get_system_prompt()}]

    # Prompt for user input and save
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})

    # display the existing chat messages
    for message in st.session_state.messages:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])
            if "results" in message:
                st.dataframe(message["results"])

    # If last message is not from assistant, we need to generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            response = ""
            resp_container = st.empty()
            for delta in openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            ):
                response += delta.choices[0].delta.get("content", "")
                resp_container.markdown(response)

            message = {"role": "assistant", "content": response}
            # Parse the response for a SQL query and execute if available
            sql_match = re.search(r"```sql\n(.*)\n```", response, re.DOTALL)
            if sql_match:
                sql = sql_match.group(1)
                conn = st.experimental_connection("postgresql", type="sql")
                message["results"] = conn.query(sql)
                st.dataframe(message["results"])
            st.session_state.messages.append(message)


page_names_to_funcs = {
    "—": intro,
    "Explanation": explanation,
    "Visualizations": visualizations,
    "Chatbot": chatbot,
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()