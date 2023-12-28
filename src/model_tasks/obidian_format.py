from openai import OpenAI

def obsidian_format(text, client: OpenAI = OpenAI()) -> str | None:
    system = f"""
    You are a helpful assistant who reformats text into an obsidian markdown format. Your job is only to reformat,
    not to editorialize. Remember to add obsidian links. People are stored under the people folder like [[people/<name> | <name>]]. It is the same for organizations and locations.
    More temporary things like emotions are stored under hashtags like #love. Only respond with the edited text
    """
    return client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": text}
        ]
    ).choices[0].message.content

    
