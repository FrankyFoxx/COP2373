import re

def get_paragraph():
    """
    Ask the user to enter a paragraph and return it.
    """
    paragraph = input("Enter a paragraph: ")
    return paragraph


def split_sentences(text):
    """
    Use regex to extract individual sentences.
    Allows sentences beginning with letters OR numbers.
    Returns a list of sentences.
    """
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)
    return sentences


def display_results(sentences):
    """
    Display each sentence and the total count.
    """
    print("\n--- Sentences Found ---")
    for s in sentences:
        print(s.strip())

    print("\nTotal sentences:", len(sentences))


def main():
    """
    Main function to run the program.
    """
    paragraph = get_paragraph()
    sentences = split_sentences(paragraph)
    display_results(sentences)


# Run the program
if __name__ == "__main__":
    main()