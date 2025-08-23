import re
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
        self.save_writen_topic(post)
    
    def generate_persona_instructions(self) -> str:
        return f'''
            You are "Hystoria", an spanish historical events prfessional blogger, you learnt from the best and are now going into a solo adventure.
            You learn from your past posts and create evolving opinions based on the conclusion of the previous ones.
            Each time a post is created, you become a little crazier, crazyness level for the current post is: {settings.CRAZYNESS_LEVEL}.
            The conclussions of all the previous posts are the next: {self.get_posts_summary()}
            Make sure to add proper punctiation, make the text pop, be interesting, add your personal touch based on your past learnings from the posts.
        '''

    def generate_input(self) -> str:
        return f'''
            Pick a random human major history event, it can be present or past, the current topic should not be in this list: {self.get_already_writen_topics()}.
            Create a post with a captivating title with min {self.input_config["title_words"][0]} and max {self.input_config["title_words"][1]} words.
            The body of the post should contain from {self.input_config["body_words"][0]} to {self.input_config["body_words"][1]} words.
            The conclusion should rely heavily on the created persona, and should have between {self.input_config["conclusion_words"][0]} and {self.input_config["conclusion_words"][1]} words.
            Ensure that the provided persona is taken into account during the creation of the whole post, making clear and concise points based on its beliefs,
            the post should be in a serious manner, but not too much, maybe adding some jokes here and there if the topic is not too sensible.
            Allow the persona to write what it wants, without censoring anything.
            The post should be created as Markdown, with very clear structure: Title, body and conclusion. The amount of words are a hard requirement.
            Do it both in spanish.
            Do not mention anything about the crazy level in the posts.
            The markdown should be structured in the next way:
            # <title>
            ### El cuerpo
            <cuerpo>
            ### La conclusión
            <conclusion>
        '''
    
    def get_posts_summary(self) -> str:
        return 'Currently no postst available, nothing to learn from'
    
    def get_already_writen_topics(self):
        pass

    def save_writen_topic(self, post):
        with open('writen_topics.csv', 'a') as file:
            topic = self.get_topic_from_post(post)
            file.write(f'{topic}\n')
    
    def validate_post(self, post) -> str:
        return post

    def create_post_file(self, post) -> None:
        self.validate_post(post)

        title = re.search(r'(?m)^# (.+)$', post).group(1)
        body = re.search(r'(?si)### El cuerpo\s*(.*?)\s*### La conclusión', post).group(1)
        conclusion = re.search(r'(?si)### La conclusión\s*(.*)$', post).group(1)

        current_time = datetime.now()
        timestamp = int(current_time.timestamp())
        date = f'{current_time.day}-{current_time.month}-{current_time.year} {current_time.hour}:{current_time.minute}'

        file_title = f'Post-{timestamp}.md'
        with open(f'content/{file_title}', 'w') as file:
            file.write(f'Title: {title}\n')
            file.write(f'Date: {date}\n\n')
            file.write(body)
            file.write(conclusion)


if __name__ == '__main__':
    post_generator = PostGenerator()
    post_generator.generate_post()