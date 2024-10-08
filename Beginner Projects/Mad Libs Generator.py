# Mad Libs Generator

def get_word(prompt):
    """Prompt the user to enter a word."""
    return input(f"Enter a {prompt}: ")

def create_story(adjective, noun, verb, adverb):
    """Create a story using the provided words."""
    story = (
        f"It was a {adjective} day. I saw a {noun} {verb}ing {adverb} down the street."
    )
    return story

def main():
    """Main function to run the Mad Libs Generator."""
    print("Welcome to the Mad Libs Generator!")
    adjective = get_word("adjective")
    noun = get_word("noun")
    verb = get_word("verb")
    adverb = get_word("adverb")

    story = create_story(adjective, noun, verb, adverb)
    print("\nHere's your story:")
    print(story)

if __name__ == "__main__":
    main()
