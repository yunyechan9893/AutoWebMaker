import openai
import time
from config.config import DevelopmentConfig as conf

openai.api_key = conf.OPENAI_API_SECRET_KEY
model = "gpt-3.5-turbo-16k-0613"


# 메세지 초기화
def create_message( prompt ):
    return [
        {"role": "system", "content": prompt}
        ]

# 대화 user 메세지 append
def put_query_message( message, query ):
    message.append({"role": "user", "content": query})

# 대화 assistant 메세지 append
def put_answer_message( message, answer ):
    message.append({"role": "assistant", "content": answer})

# 대화 system 메세지 append
def put_system_message( message, answer ):
    message.append({"role": "system", "content": answer})

# 처음 메세지 user, assistant 메세지 삭제
# 일정 토큰 이상일 때 동작
def del_message(messages, idx=2):
    del messages[idx]
    del messages[idx]

    return messages


def post_query( model, gpt_params, messages ):
        
    # 파라미터
    temperature = gpt_params.get_temperature()
    max_tokens = gpt_params.get_max_tokens()
    top_p = gpt_params.get_top_p()
    best_of = gpt_params.get_best_of()
    frequency_penalty = gpt_params.get_frequency_penalty()
    presence_penalty = gpt_params.get_presence_penalty()
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    
    return response['choices'][0]['message']['content']

def get_gpt_answer(model, gpt_params, messages):
    try:
        print(gpt_params)
        print(type(gpt_params))
        return post_query( model, gpt_params, messages )
    except openai.error.RateLimitError as e:
        retry_time = e.retry_after if hasattr(e, 'retry_after') else 15
        print(f"Rate limit exceeded. Retrying in {retry_time} seconds...")
        time.sleep(retry_time)
        return post_query( model, messages )

    except openai.error.APIError as e:
        retry_time = e.retry_after if hasattr(e, 'retry_after') else 15
        print(f"API error occurred. Retrying in {retry_time} seconds...")
        time.sleep(retry_time)
        return post_query( model, messages )

    except OSError as e:
        retry_time = 5  # Adjust the retry time as needed
        print(f"Connection error occurred: {e}. Retrying in {retry_time} seconds...")      
        return post_query( model, messages )




         