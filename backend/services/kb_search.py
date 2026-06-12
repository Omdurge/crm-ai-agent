import os


KB_PATH = "knowledge_base"


def search_knowledge_base(query: str):

    query = query.lower()

    matches = []

    for filename in os.listdir(KB_PATH):

        filepath = os.path.join(KB_PATH, filename)

        if not os.path.isfile(filepath):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if query in content.lower():
            matches.append({
                "file": filename,
                "content": content
            })

    return matches