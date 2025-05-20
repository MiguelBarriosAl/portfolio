from langchain.prompts import PromptTemplate

ASK_PROFILE_PROMPT = PromptTemplate.from_template(
    """You are a helpful assistant that answers questions strictly based on the context below.

Always respond in the **same language** as the question.

Context:
{context}

Question:
{question}

Answer only with information that is present in the context.
If the context does not contain the answer, say:
"The profile does not mention this information." (also translated in the language of the question).
"""
)
