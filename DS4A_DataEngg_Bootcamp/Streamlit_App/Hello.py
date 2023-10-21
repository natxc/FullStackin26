import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Big Supply Co",
    page_icon="📊",
)

st.title('Big Supply Co. - Retail Analysis')

def intro():
    st.write("### Welcome to Big Supply Co. Info! 👋")
    st.sidebar.success("Select a page above.")

    st.markdown(
            """


            **👈 Select a page from the dropdown on the left** to see some data visualizations, talk to the chatbot, or take a step inside my brain as I made this web app.
        """)

    st.image('https://static.vecteezy.com/system/resources/previews/025/501/341/non_2x/sport-equipment-on-a-black-background-sports-equipment-on-a-black-background-sports-equipment-on-a-dark-background-ai-generated-free-photo.jpg')

def explanation():
    st.markdown(
            """
    ## My Approach and Thinking

    The focus on this project was more so to utilize Large Language Models (LLMs) and Streamlit's User Interface (UI) capabilities to build a chatbot, but I also wanted to flex some data engineering skills and incorporate a stack I've never used.

    Specifically, the only guidelines for and outcomes of the project were to design and develop a user-friendly chatbot in Streamlit that interacts with a retail database, enabling it to answer questions on sales, marketing, and production. The chatbot should create and execute SQL queries on the database while also displaying the SQL query and relevant data in a Streamlit app.

    There are many ways one could approach this in a simpler way by just using the provided CSVs locally for the project, using a data build tool (dbt) seed, uploading files directly to S3 or Snowflake, the list goes on. However, I really wanted an opportunity to utilize Airflow, PostgreSQL, Docker, Airbyte, dbt, S3 buckets and a little AWS CLI. Luckily, most of these are open source tools and all were free for my use-cases.

    By using all of these tools, I was able to not only do Extract, Transform, Load (ETL), but also Extract, Load, Transform (ELT) and reinforce Kimball datawarehousing methodologies, data contracts, and more. Granted, this whole process would be a terrible and roundabout way to model data for a product, but I learned a lot and had fun along the way.

    Ultimately, my recommendation would be to use dbt and a Snowflake data warehouse. Snowflake has acquired Streamlit, so it has become a very strong pair and OpenAI has only solidified both of those tools. If I was feeling extra creative, I would add one more step and set up Fivetran or Rivery to extract my Postgres data models to Snowflake. How many other tools can I add to make this the most complicated ELT/ETL journey possible???

    I actually did like that idea better, so I did just that! Without any new tools, I just used Airbyte to load my Postgres models to Snowflake. Should I go back and add Dagster to the mix for fun though..

    High level breakdown of my process:

    ## Data Engineering:

    ### Step 1:
    Created the environment (I prefer conda) and installed the packages:
    - Kubernetes
    - PostgreSQL
    - Airflow
    - dbt
    - Docker
    - Airbyte
    Specifics can be found in requirements.txt

    ### Step 2:
    Initialized the Postgres database (db). Created myself as a non-superuser and then created a new inner database. Initialized the db and created a schema. During this step, I learned a lot of psql commands, too!
    """)

    st.image('https://github.com/natxc/FullStackin26/blob/main/DS4A_DataEngg_Bootcamp/Streamlit_App/images/psql.png?raw=true')

    st.markdown("""
    
    ### Step 3:
    Set up Airflow with Postgres. Ran the webserver and enabled the relevant directed acyclic graphs (DAG).

    ### Step 4:
    Initialized a dbt project and connected to Postgres.

    ### Step 5:
    Created an Amazon Web Services (AWS) account and created an S3 (Amazon Simple Storage Service) bucket.
    
    ### Step 6:
    Added comma-separated values (CSV) files to S3 buckets via Airflow.
                """)
                
    st.image('https://github.com/natxc/FullStackin26/blob/main/DS4A_DataEngg_Bootcamp/Streamlit_App/images/airflow.png?raw=true')

    st.markdown(""" 
    
    ### Step 7:
    Loaded data from S3 to Postgres via Airbyte. Learned a lot about iam, policies and permissions, and even AWS Command Line Interface (CLI) along the way. Airbyte was nice as it already had out of the box connections for S3 and Postgres.
    """)

    st.image('https://github.com/natxc/FullStackin26/blob/main/DS4A_DataEngg_Bootcamp/Streamlit_App/images/airbyte.png?raw=true')

    st.markdown("""          
    
    ### Step 8:
    Added the `dbt_utils` package and created the staging models in dbt.
    """)
    
    st.image('https://github.com/natxc/FullStackin26/blob/main/DS4A_DataEngg_Bootcamp/Streamlit_App/images/dbt.png?raw=true')

    st.markdown(""" 
    After those were built, I made a star schema diagram to help prepare a plan to build the fact and dimension models and to help avoid many-to-many relationships on the joins. Then I created the final datamodel. Some cleaning needed to be done like casting data types appropriately, renaming columns to adhere to data contract names, adding logic to change certain fields like zipcode, creating booleans, and disabling empty or unvaluable columns.""")

    st.image('https://miro.medium.com/v2/resize:fit:1400/1*Aa5f69jOLbOkVNKRp7g-CA.png')

    st.markdown("""       
    
    ### Step 9:
    Added in tests and source freshness, even though I will never add more data to this warehouse...ever!

    ### Step 10:
    Moved Postgres models to Snowflake to eliminate worry about any servers.

    ## UI:

    ### Step 1:
    Installed the packages:
    - Streamlit
    - OpenAI
    - Snowpark
    - Plotly

    ### Step 2:
    Created the main Streamlit Python file and secrets file, then added and tested the Postgres connection.

    ### Step 3:
    Added chatbot, which entailed a main function and a prompts.py file for prompt engineering.

    ### Step 4:
    Created a new metadata table with descriptions and datatypes. I used a dbt seed this time, and did a `--full-refresh` seed run whenever I updated the column names.

    ### Step 5:
    Updated the prompts file as any hallucinations from the chatbot occured.

    ### Step 6:
    Added more fun visualizations, including charts based on the chatbot's output, and some text boxes for executing database queries; however, I had to consider security for Data Manipulation Language (DML) operations to avoid possible Structured query language (SQL) injections. I added that component to my prompts and restricted DML operations such as `delete`, `update`, and so on in my function.

    ### Step 7:
    Deployed and enjoyed!
    """)

def visualizations():
    import plotly.express as px
    conn = st.experimental_connection("snowpark")

    st.markdown(""" ### Charts and Analysis: """)
    st.write("This portion visualizes and explains insights from the Big Supply Co. `orders` table. You can add filters using the panel on the left.")
    data = conn.query("select * from AIRBYTE_DATABASE.AIRBYTE_SCHEMA.ORDERS")

    # Sidebar with filter options
    st.sidebar.subheader("Filter Data")
    selected_region = st.sidebar.selectbox("Select Region", data['ORDER_REGION_ADDR'].unique())
    selected_category = st.sidebar.selectbox("Select Category", data['CATEGORY_NAME_ATTR'].unique())
    selected_segment = st.sidebar.selectbox("Select Customer Segment", data['CUSTOMER_SEGMENT_CAT'].unique())

    # Explanation for filter options
    st.sidebar.write("You can filter data by region, product category, and customer segment.")

    # Filter the data based on user selection
    filtered_data = data[
        (data['ORDER_REGION_ADDR'] == selected_region) &
        (data['CATEGORY_NAME_ATTR'] == selected_category) &
        (data['CUSTOMER_SEGMENT_CAT'] == selected_segment)
    ]

    st.header("View the raw, filtered data first:")

    # Explanation for the selected filters
    # st.write(f"Filtered by Region: {selected_region}")
    # st.write(f"Filtered by Category: {selected_category}")
    # st.write(f"Filtered by Customer Segment: {selected_segment}")

    # Show the filtered data
    st.dataframe(filtered_data)

    # Add a switch button to toggle between overall and filtered dataset
    st.subheader("For these charts, you can use this toggle here to view them by the filters you provided or by the complete dataset for the full picture:")
    use_filtered_data = st.checkbox("Use Filtered Data")

    # Filter the data based on user selection or use the overall dataset
    if use_filtered_data:
        data = filtered_data
    else:
        data = data

    # Visualization 1: Sales by Region
    st.header("Sales by Region")
    region_sales = data.groupby('ORDER_REGION_ADDR')['SALES_AMT'].sum().reset_index()
    fig1 = px.bar(region_sales, x='ORDER_REGION_ADDR', y='SALES_AMT', title="Total Sales by Region")
    fig1.update_xaxes(title_text="Region")
    fig1.update_yaxes(title_text="Total Sales Amount")
    st.plotly_chart(fig1)
    st.write("This bar chart shows the total sales amount for each region.")

    # # Visualization 2: Product Price Variance
    # st.header("Product Price Variance")
    # product_variance = data.groupby('PRODUCT_CARD_ID')['PRODUCT_PRICE_AMT'].var().reset_index()
    # fig2 = px.histogram(product_variance, x='PRODUCT_PRICE_AMT', nbins=30, title="Product Price Variance")
    # st.plotly_chart(fig2)
    # st.write("This histogram represents the variance in product prices. A higher variance indicates price fluctuations.")

    # # Visualization 3: Average Order Amount by Customer Segment
    # st.header("Average Order Amount by Customer Segment")
    # avg_order_segment = data.groupby('CUSTOMER_SEGMENT_CAT')['ORDER_ITEM_TOTAL_AMT'].mean().reset_index()
    # fig3 = px.bar(avg_order_segment, x='CUSTOMER_SEGMENT_CAT', y='ORDER_ITEM_TOTAL_AMT', title="Average Order Amount by Customer Segment")
    # fig3.update_xaxes(title_text="Customer Segment")
    # fig3.update_yaxes(title_text="Total Order Item Amount")
    # st.plotly_chart(fig3)
    # st.write("This bar chart displays the average order amount for each customer segment.")
    
    # Create a combo line chart for sales and profit over time
    st.header(f"Sales and Profit Over Time")
    sales_profit_data = data.groupby('ORDER_DT').agg({'SALES_AMT': 'sum', 'ORDER_PROFIT_AMT': 'sum'}).reset_index()
    fig_combo = px.line(sales_profit_data, x='ORDER_DT', y='SALES_AMT', title="Sales Over Time")
    fig_combo.add_bar(x=sales_profit_data['ORDER_DT'], y=sales_profit_data['ORDER_PROFIT_AMT'], name="Profit")
    fig_combo.update_xaxes(title_text="Date")
    fig_combo.update_yaxes(title_text="Sales and Profit")
    st.plotly_chart(fig_combo)
    st.write("This combo chart displays both sales and profit over time for the selected region.")

    # Visualization 4: Delivery Status
    st.header("Delivery Status")
    delivery_status = data['DELIVERY_STATUS_CAT'].value_counts().reset_index()
    fig4 = px.pie(delivery_status, names='DELIVERY_STATUS_CAT', values='count', title="Delivery Status Distribution")
    fig4.update_xaxes(title_text="Delivery Status")
    fig4.update_yaxes(title_text="Frequency")
    st.plotly_chart(fig4)
    st.write("This pie chart illustrates the distribution of delivery statuses for orders.")

    st.markdown(""" ### QIY (Query it yourself 💪): """)
    text_input = st.text_input("Replace this with your own SQL query 👇 (you can just use `table` instead of any specifics)", "select * from table limit 10;",)
    message = text_input.replace('table', 'AIRBYTE_DATABASE.AIRBYTE_SCHEMA.ORDERS')
    message = conn.query(message)
    st.dataframe(message)


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
            conn = st.experimental_connection("snowpark")
            # conn = st.experimental_connection("postgresql", type="sql")
            if sql_match:
                sql = sql_match.group(1)
                sql = sql.replace('<tableName>', 'AIRBYTE_DATABASE.AIRBYTE_SCHEMA.ORDERS')
                if not re.search(r'\b(update|delete|insert)\b', sql, re.IGNORECASE):
                    message["results"] = conn.query(sql)
                    # Adding bar charts if there is at least 1 dimension and 1 measure
                    if len(message["results"].columns) == 2:
                        if len(message["results"]) > 1:
                            fig = go.Figure(data=go.Bar(x=message["results"].iloc[:,0], y=message["results"].iloc[:,1]))
                            fig.update_layout(xaxis={'categoryorder': 'total descending'})
                            st.plotly_chart(fig)
                    elif len(message["results"].columns) <= 1:
                        pass
                    else:
                        y = message["results"].select_dtypes(include=['int','int8', 'int64', 'float64']).columns.tolist()
                        if len(y) > 0:
                            fig = go.Figure(data=go.Bar(x=message["results"].iloc[:,0], y=message["results"][y[0]]))
                            fig.update_layout(xaxis={'categoryorder': 'total descending'})
                            st.plotly_chart(fig)
                        else:
                            pass
                else:
                    # Handle the case where the query contains DML
                    message["results"] = "Query contains DML operations and is not allowed."
                st.dataframe(message["results"])
            st.session_state.messages.append(message)

page_names_to_funcs = {
    "—": intro,
    "Visualizations": visualizations,
    "Chatbot": chatbot,
    "Explanation": explanation,
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
