from rag.rag_system import retrieve_answer
from openai import OpenAI

client = OpenAI()

def get_answer(query: str) -> str:
    retrieved_answers = retrieve_answer(query)

    prompt = f"Answer the following query based on the information provided:\nQuery: {query}\nInformation:\n"
    for answer in retrieved_answers:
        prompt += f"- {answer}\n"
    prompt += "\nAnswer:"

    response = client.Completion.create(
        engine="gpt-4o-mini",
        prompt=prompt,
        max_tokens=400
    )
    
    final_answer = response.choices[0].text.strip()
    return final_answer
