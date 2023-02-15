import openai
from utils.helper_functions import load_key

openai.api_key = load_key(r'/home/omrijsharon/PycharmProjects/setitfree/credentials/key.yaml')
completion = openai.Completion.create(engine="davinci", prompt="where are you now?", temperature=1.0, max_tokens=5)
print(completion)