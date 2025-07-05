from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Load environment variables from the .env file
load_dotenv()

# Access the GROQ API key from the environment
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key  # Redundant but ensures it's set

# Initialize the Groq model
llm = ChatGroq(model_name="gemma2-9b-it", temperature=0.7)

def generate_restaurant_name_items(cuisine): 
    prompt_template_name = PromptTemplate(
        input_variable=['cuisine'],
        template="I want to open a restaurant for {cuisine} food,suggest me a fancy name only one"
    ) 
    name_chain=LLMChain(llm=llm,prompt = prompt_template_name,output_key="restaurant_name")


    prompt_template_items = PromptTemplate(
        input_variable=['restaurant_name'],
        template="suggest me a some menu items for {restaurant_name}.Return it as comma separated list with category"
    ) 
    item_chain=LLMChain(llm=llm,prompt = prompt_template_items,output_key="menu_items")

    from langchain.chains import SequentialChain
    chain=SequentialChain(
        chains=[name_chain,item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name','menu_items']
    )
    response=chain({'cuisine':cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_items("italian"))
