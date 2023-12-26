from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate

from few_shots import few_shots

import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()

def get_few_shot_db_chain():
    config = dotenv_values(".env")
    db_user = config["PG_USER"]
    db_password = config["PG_PASSWORD"]
    db_host = config["PG_HOST"]
    db_name = config["DB_NAME"]

    db = SQLDatabase.from_uri(f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}")
    llm = GooglePalm(temperature=0.1)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    example_selector = SemanticSimilarityExampleSelector.from_examples( 
        examples=few_shots,
        embeddings=embeddings,
        vectorstore_cls=Chroma,
        k=2 
    )

    example_prompt = PromptTemplate(
        input_variables=["answer", "question", "sql_query","sql_result"],
        template="Answer: {answer}\nQuestion: {question}\nSQLQuery: {sql_query}\nSQLResult: {sql_result}"
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"], #These variables are used in the prefix and suffix
    )
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain