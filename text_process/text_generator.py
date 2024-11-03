from openai import OpenAI
import re
from abc import ABC, abstractmethod

class TextProcessor:
    @staticmethod
    def clean_text(text):
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'[^a-zA-Z0-9.,!?\'\"\s]', '', text)
        return text

class GeneratorAbstract(ABC):

    def __init__(self, api:str, model:str="microsoft/phi-3.5-mini-instruct"):
        self.model = model
        self.api = api

    @abstractmethod
    def create_client(self):
       pass
    
    @abstractmethod
    def build_completion(self, user_input:str="Let's start our discussion"):
       pass
    
    @staticmethod
    def clean_text(text):
        pass

    @abstractmethod
    def parse_chunks(self):
        pass

    @abstractmethod
    def generate(self):
        pass

class TextGenerator(GeneratorAbstract):

    def __init__(self, api: str, model: str = "qwen/qwen2-7b-instruct"):
        super().__init__(api, model)
        self.outputList = []
        self.outputText = ""

    def create_client(self):
        self.client = OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = self.api)

    
    def build_completion(self, user_input:str="Let's start our discussion"):
        try:
            self.completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role":"user","content":user_input}],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            stream=True
            )
        except:
            return f"build completion failed for MODEL = {self.model} and API = {self.api}"
    
    @staticmethod
    def clean_text(text):
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'[^a-zA-Z0-9.,!?\'\"\s]', '', text)
        return text
    
    def parse_chunks(self):
        try:
            for chunk in self.completion:
                if chunk.choices[0].delta.content is not None:
                    self.outputText += chunk.choices[0].delta.content
        except:
            return f"chunk is not possible MODEL = {self.model} and API = {self.api} "
            
    def generate(self):
        try:
            self.parse_chunks()  
            output = TextProcessor.clean_text(self.outputText)
            return output
        
        except:
            return f"text cleaning is failed for input text, input should be clean also check (MODEL = {self.model} and API = {self.api})"

if __name__ == "__main__":
    pass
