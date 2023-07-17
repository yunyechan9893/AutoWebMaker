class Params:
    def __init__(
            self, 
            temperature=0, 
            max_tokens=0, 
            top_p=0, 
            best_of=0, 
            frequency_penalty=0,
            presence_penalty=0
        ):
        '''
        temperature    
        - 설명
            - 1로 갈수록 GPT는 같은 질문에 거의 같은 대답을 한다. GPT의 대답의 랜덤 값을 조절하는 옵션이다.
            - 이 옵션을 0으로 한다면 너무 질문과는 상관없는 대답을 할 수 있으므로 사용 목적에 따라 적당히 조절해야한다.
        - 범위
            - 0 < x < 1
        MAXIMUM LENGTH 
        - 설명
            - GPT의 답변의 최대 길이이다. 이게 길면 자세한 대답을 할 수 있고 짧으면 대답이 중간에 끊길 수 있다. 하지만 무조건 길게 하면 돈이 조금 들 수 있으니 본인 선택에 따라 조절하면 된다.
        - 범위
            - 0 < x

        TOP P
        - 설명
            - 이것도 TEMPERATURE 하고 비슷한 개념인데 질문에 대한 대답으로 몇 퍼센트 이상의 확률을 가진 답변을 할지 정하는 것이다.
        - 범위
            - 0 < x

        FREQUECY PENALTY 
        - 설명
            - 빈도수 패널티이다. GPT가 가끔 똑같은 대답을 할 때가 있는데 이러한 현상을 줄이기 위한 옵션이다.
    
        '''
        self.__temperature = temperature
        self.__max_tokens = max_tokens
        self.__top_p = top_p
        self.__best_of = best_of
        self.__frequency_penalty = frequency_penalty
        self.__presence_penalty = presence_penalty


    def get_temperature(self):
        return self.__temperature
    
    def get_max_tokens(self):
        return self.__max_tokens
    
    def get_top_p(self):
        return self.__top_p
    
    def get_best_of(self):
        return self.__best_of
    
    def get_frequency_penalty(self):
        return self.__frequency_penalty
    
    def get_presence_penalty(self):
        return self.__presence_penalty
        
        
       
        