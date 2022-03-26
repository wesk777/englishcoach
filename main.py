from reverso_context_api import Client
client = Client("ru", "en")

for context in client.get_translation_samples("привет", cleanup=True):
    print(context)
