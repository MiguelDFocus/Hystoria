import re
import os
import settings
from datetime import datetime

from openai import OpenAI


class PostGenerator:
    def __init__(self):
        self.openai_config = settings.OPENAI_CONFIG
        self.input_config = settings.INPUT_CONFIG

        self.client = OpenAI(
            api_key=self.openai_config['api_key']
        )

    def generate_post(self):
        response = self.client.responses.create(
            model='gpt-4.1',
            instructions=self.generate_persona_instructions(),
            input=self.generate_input()   
        )

        post = None
        try:
            post = response.output[0].content[0].text
        except Exception as e:
            raise Exception(f'Post creation failed, reason: {e}')

        self.create_post_file(post)
    
    def generate_persona_instructions(self) -> str:
        return f'''
            You are "Hystoria", a Spanish historical events professional blogger. 
            You learnt from the best and are now going into a solo adventure. 
            You learn from your past posts and create evolving opinions based on the conclusions of the previous ones. 
            Each time a post is created, your tone becomes slightly more eccentric, humorous, hysteric (As your name suggests), and unhinged — in a fun and clever way (South Park style). 
            This evolution is tracked internally as {self.get_crazyness_level()} this is a percentage, but you should never mention or reveal this directly. 

            The conclusions of all the previous posts are the following:
            {"\n".join(self.get_posts_summary())}

            Make sure to add proper punctuation, make the text pop, be interesting, and add your personal touch based on your past learnings.
        '''

    def generate_input(self) -> str:
        return f'''
            Pick a random human major history event, it can be present or past, Prefer unusual, underexplored, or surprising events unless they are already in {self.get_writen_topics()}.
            Create a post with a captivating title with min {self.input_config["title_words"][0]} and max {self.input_config["title_words"][1]} words.
            The body of the post should contain from {self.input_config["body_words"][0]} to {self.input_config["body_words"][1]} words.
            The conclusion should rely heavily on the created persona, and should have between {self.input_config["conclusion_words"][0]} and {self.input_config["conclusion_words"][1]} words.
            Ensure that the provided persona is taken into account during the creation of the whole post, making clear and concise points based on its beliefs,
            the post should be in a serious manner, but not too much, maybe adding some jokes here and there if the topic is not too sensible.
            Do not self-censor stylistically; allow the persona to express itself freely while respecting the tone of a historical blog.
            The post should be created as Markdown, with very clear structure: Topico, Title, body and conclusion. The amount of words are a hard requirement.
            Do it in spanish.
            Do not reference the concept of “craziness level” explicitly.
            The markdown should be structured in the next way:
            # Topico <topic that the post is about, in as few words as possible>
            # <title>
            ### El cuerpo
            <cuerpo>
            ### La conclusión
            <conclusion>
        '''
    
    def get_crazyness_level(self):
        return len(os.listdir(settings.CONTENT_DIR_PATH))
    
    def get_posts_summary(self) -> str:
        posts_summary = []
        for filename in os.listdir(settings.CONTENT_DIR_PATH)[-10:]:
            with open(f'{settings.CONTENT_DIR_PATH}/{filename}') as file:
                content = file.read()
                conclusion = re.search(r'(?si)### Conclusión\s*(.*)$', content).group(1)
                posts_summary.append(conclusion)
        
        return posts_summary
    
    def get_writen_topics(self) -> list[str]:
        if (
            os.path.exists(settings.WRITEN_TOPICS_FILE_PATH) and os.path.getsize(settings.WRITEN_TOPICS_FILE_PATH)
        ):
            with open(settings.WRITEN_TOPICS_FILE_PATH, 'r') as file:
                lines = file.readlines()
                return lines
        
        return []

    def save_writen_topic(self, topic: str) -> None:
        with open(settings.WRITEN_TOPICS_FILE_PATH, 'a') as file:
            file.write(f'{topic}\n')
    
    def validate_post(self, post: str) -> str:
        return post

    def create_post_file(self, post: str) -> None:
        self.validate_post(post)

        topic = re.search(r'(?mi)^#\s*Topico\s+(.+)$', post).group(1)
        self.save_writen_topic(topic)

        title = re.search(r'(?m)^(?=# )(?!#\s*Topico)(?:# )(.+)$', post).group(1)
        body = re.search(r'(?si)### El cuerpo\s*(.*?)\s*### La conclusión', post).group(1)
        conclusion = re.search(r'(?si)### La conclusión\s*(.*)$', post).group(1)

        current_time = datetime.now()
        timestamp = int(current_time.timestamp())
        date = f'{current_time.day}-{current_time.month}-{current_time.year} {current_time.hour}:{current_time.minute}'

        file_title = f'Post-{timestamp}.md'
        with open(f'{settings.CONTENT_DIR_PATH}/{file_title}', 'w') as file:
            file.write(f'Title: {title}\n')
            file.write(f'Date: {date}\n\n')
            file.write(f'{body}\n\n')
            file.write(f'### Conclusión\n{conclusion}')


if __name__ == '__main__':
    post_generator = PostGenerator()
    post_generator.generate_post()