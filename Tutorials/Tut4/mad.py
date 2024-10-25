# def get_word(prompt):
#     """Prompt the user to enter a word."""
#     while True:
#         word = input(f"Enter a {prompt}: ").strip()
#         if word.isalpha():
#             return word
#         else:
#             print("Invalid input. Please enter alphabetic characters only.")

# def create_story(adjective, noun, verb, adverb):
#     """Create a story using the provided words."""
#     story = (
#         f"It was a {adjective} day. I saw a {noun} {verb}ing {adverb} down the street."
#     )
#     return story
def get_word(word):
    while True:
        word = input(f"Enter The {word} : ").strip()
        if word.isalpha():
            return word
        else:
            print("Invalid Word!")

def create_story(adjective,noun,verb,adverb):
    story = (f"It was a {adjective} day. I saw {noun} {verb}ing {adverb} down the street.")
    return story

def mad_libs():
    adjective = get_word("adjective")
    noun = get_word("noun")
    verb = get_word("verb")
    adverb = get_word("adverb")

    story = create_story(adjective,noun,verb,adverb)
    print()
    print(story)

mad_libs()