from openai import OpenAI
import re
from pyswip import Prolog

# Initialize Prolog interpreter
prolog = Prolog()

client = OpenAI()

def parse_prolog(prolog_text):
    # Remove the custom delimiter and any leading/trailing whitespace
    prolog_text = prolog_text.strip("```prolog").strip()

    # Remove comments and extra spaces
    prolog_text = re.sub(r'%.*', '', prolog_text).strip()

    # Split lines into statements
    statements = [line.strip() for line in prolog_text.splitlines() if line.strip()]

    facts = []
    rules = []

    for statement in statements:
        if ":-" in statement:
            rules.append(statement[:-1])
        else:
            facts.append(statement[:-1])

    return facts, rules

completion = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": """Convert following sentences to rules and facts of prolog (Do not return any data other than prolog). 
                        if something is metal then it conducts electricity.
                        Insulators do not conduct electricity.
                        If something is made of iron, then it is metal.
                        Nails are made of iron."""
        }
    ]
)

print(completion.choices[0].message.content)

facts, rules = parse_prolog(completion.choices[0].message.content)

print(facts)
print(rules)

for fact in facts:
    prolog.assertz(fact)

for rule in rules:
    prolog.assertz(rule)

query_result = list(prolog.query("conducts_electricity(nails)"))

# Check if query returned any results
if query_result:
    print("True")
else:
    print("False")
