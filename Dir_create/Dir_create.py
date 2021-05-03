import os


def ask_values(prompt, input_msg):
    choices = []
    print(f"{prompt} (press <ENTER> when finished)")
    while True:
        choice = raw_input(input_msg) #input("") is vulnerable to code exec
        if choice:
            choices.append(choice)
        else:
            return choices


languages = ask_values(
    "Enter the languages",
    "Enter the language name (ex.: Golang, Python, etc.): "
)
print("=> languages:", languages)
print()

directories = ask_values(
    "Enter the directories",
    "Enter the directorie name (ex.: DS, Learn, Web, etc.): "
)
print("=> directories:", directories)
print()


# Root directory of you directory tree
root_dir = os.path.abspath(".")

print("Creating directories...")
for dir_name in languages:
    for lang in directories:
        path = os.path.join(root_dir, dir_name, lang)
        try:
            os.makedirs(path)
        except FileExistsError:
            pass
print("Done.")
