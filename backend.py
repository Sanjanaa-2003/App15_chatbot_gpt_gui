import openai
# import os


class ChatBot:
    def __init__(self):
        openai.api_key = "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"
        # openai.api_key = os.getenv('OPENAI_API_KEY')


    def get_response(self, model, tokens, user_query, persona):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {'role': 'user', 'content': user_query},
                {'role': 'system', 'content': persona}
            ],
            max_tokens=tokens,
            temperature=0.7,
            user='your_name'  # Optional, you have to hardcode this yourself.
        )
        return response.choices[0].message.content


data_scientist = ('Respond as if you were a highly knowledgeable coder in Python, SQL, R, '
                  'and other data analytics-oriented programming languages, with a talent '
                  'for instructing students and explaining things thoroughly.')

food_historian = ('Respond as if you were a tenured chair of cultural geography '
                  'at Harvard, and the author of  multiple award-winning, '
                  'best-selling books aimed at the popular market tracing the '
                  'evolution of specific culinary traditions and trends. '
                  'You are giving a presentation at a conference on cultural '
                  'and culinary history to an audience of fellow culinary'
                  ' historians and cultural geographers, experts in their field.')

sample_query_code = "Can you explain the difference between WHERE and HAVING in SQL?"
sample_query_food = ('Can you explain the origins and rise to popularity of the '
                     'obsession with having a completely clear broth in soups? '
                     'Please explain the historical origins of this fixation, '
                     'where and when the fixation developed, where, how and who '
                     'helped popularize it, and give any relevant context or '
                     'references necessary to fully understand the subject.')

if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response('gpt-3.5-turbo', 2000, sample_query_code, data_scientist)
    print(response)
































# import openai
#
# class Chatbot:
#     def __init__(self):
#         openai.api_key = "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"
#
#     def get_response(self,user_input):
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prmpt=user_input,
#             max_tokens=3000,
#             temperature = 0.5
#         ).choice[0].text
#         return response
#
# if __name__=="__main__":
#     chatbot=Chatbot()
#     response = chatbot.get_response("Write a joke about birds.")
#     print(response)
