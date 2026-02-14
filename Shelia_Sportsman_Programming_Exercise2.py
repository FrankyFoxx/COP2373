# -----------------------------------------
# Spam Detection Program
# -----------------------------------------

def get_keywords():
    """Return a list of 30 common spam words/phrases."""
    return [
        "free", "winner", "congratulations", "act now", "limited time",
        "urgent", "risk-free", "no obligation", "guaranteed", "money back",
        "credit", "loan", "debt", "cheap", "discount",
        "save big", "cash", "earn extra", "work from home", "investment",
        "viagra", "weight loss", "miracle", "click here", "call now",
        "no credit check", "winner selected", "prize", "100% free", "exclusive offer"
    ]


def calculate_spam_score(message, keywords):
    """
    Count occurrences of each spam keyword in the message.
    Return the total score and a list of matched keywords.
    """
    message_lower = message.lower()
    spam_score = 0
    matched_keywords = []

    for word in keywords:
        count = message_lower.count(word.lower())
        if count > 0:
            spam_score += count
            matched_keywords.append((word, count))

    return spam_score, matched_keywords


def rate_spam(score):
    """Return a rating based on the spam score."""
    if score == 0:
        return "Very unlikely spam"
    elif score <= 2:
        return "Unlikely spam"
    elif score <= 6:
        return "Possibly spam"
    elif score <= 12:
        return "Likely spam"
    else:
        return "Almost certainly spam"


def main():
    print("=== Spam Detector ===")
    print("Enter your email message below.")
    print("Press ENTER on an empty line to finish.\n")

    # Collect multi-line input
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    message = "\n".join(lines)

    # Process spam detection
    keywords = get_keywords()
    score, matches = calculate_spam_score(message, keywords)
    rating = rate_spam(score)

    # Display results
    print("\n--- RESULTS ---")
    print(f"Spam Score: {score}")
    print(f"Spam Likelihood: {rating}")

    if matches:
        print("\nKeywords Found:")
        for word, count in matches:
            print(f"- '{word}' found {count} time(s)")
    else:
        print("\nNo spam keywords found.")


# Run the program
if __name__ == "__main__":
    main()