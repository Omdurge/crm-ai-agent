from backend.services.rag import search_rag
from backend.services.gemini_service import generate_response


def generate_reply(customer_message: str):

    results = search_rag(customer_message)

    context = "\n\n".join(
        results["documents"][0]
    )

    prompt = f"""
        You are a professional CRM support agent.

        Customer message:
        {customer_message}

        Knowledge Base:
        {context}

        Rules:
        - Only use information from the knowledge base.
        - Never invent company policies.
        - Never claim actions were already taken.
        - Never claim an escalation was performed.
        - Never claim an account was reviewed.
        - Never claim a refund was approved.
        - Ask for missing information when needed.
        - Keep the response professional and concise.

        Write a support email reply.
        """

    return generate_response(prompt)