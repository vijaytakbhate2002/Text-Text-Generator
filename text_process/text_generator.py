from openai import OpenAI
import re
from abc import ABC, abstractmethod
import logging
logging.basicConfig(
    filename="model_log.log",
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class TextProcessor:
    @staticmethod
    def clean_text(text):
        logging.info("Text cleaning started...")
        text = re.sub(r'\s+', ' ', text).strip()
        logging.info("Text stripping is done...")
        text = re.sub(r'[^a-zA-Z0-9.,!?\'\"\s]', '', text)
        logging.info("Text cleaned successfully...")
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
        logging.info("Client created sucessfully...")
    
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
            logging.info("Built completion sucessfully...")
        except:
            raise Exception(f"build completion failed for user input = {user_input} and api = {self.api}")
    
    @staticmethod
    def clean_text(text):
        logging.info("Text cleaning started...")
        text = re.sub(r'\s+', ' ', text).strip()
        logging.info("Text stripping is done...")
        text = re.sub(r'[^a-zA-Z0-9.,!?\'\"\s]', '', text)
        logging.info("Text cleaned sucessfully...")
        return text
    
    def parse_chunks(self):
        try:
            logging.info("Trying to parse chunks...")
            for chunk in self.completion:
                logging.info("Chunks parsed sucessfully...")
                if chunk.choices[0].delta.content is not None:
                    logging.info(f"Parsed for {chunk.choices[0].delta.content} ...")
                    self.outputText += chunk.choices[0].delta.content
            logging.info("All Chunks parsed sucessfully...")
        except:
            raise Exception(f"chunk is not possible for this input")
            
    def generate(self):
        try:
            self.parse_chunks()  
            output = TextProcessor.clean_text(self.outputText)
            logging.info("Output generated successfully...")
            return output
        except Exception as e:
            logging.error(f"Text cleaning failed for output_text '{self.outputText}': {str(e)}")
            raise Exception(f"text cleaning is failed for output_text {self.outputText}")

if __name__ == "__main__":
    pass
