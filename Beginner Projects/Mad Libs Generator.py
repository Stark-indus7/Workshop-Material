# Mad Libs Generator
import functools


def greet(func):
    """Decorator to run certain lines before and after the code!
    """
    @functools.wraps(func)
    def decorator(*args,**kwargs):
        print("Good Morning!")
        result = func(*args,**kwargs)
        print("Thanks For Using Our Code!")
        return result
    return decorator    

def get_word(prompt):
    """Prompt the user to enter a word."""
    while True:
        word = input(f"Enter a {prompt}: ").strip()
        if word.isalpha():
            return word
        else:
            print("Invalid input. Please enter alphabetic characters only.")

def create_story(adjective, noun, verb, adverb):
    """Create a story using the provided words."""
    story = (
        f"It was a {adjective} day. I saw a {noun} {verb}ing {adverb} down the street."
    )
    return story


@greet
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
