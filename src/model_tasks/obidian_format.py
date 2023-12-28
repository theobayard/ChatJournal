from openai import OpenAI

def obsidian_format(text, client: OpenAI = OpenAI()):
    prompt = f"""
    You are a helpful assistant who reformats text into an obsidian markdown format. Your job is only to reformat,
    not to editorialize. 
    """
