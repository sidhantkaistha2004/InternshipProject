def word_count(sentence):
    """Count the number of words in a given sentence."""
    words = sentence.split()
    return len(words)

def main():
    """Main function to handle user input and display output."""
    try:
        # Prompt user for input
        user_input = input("Enter a sentence or paragraph: ")

        # Check for empty input
        if not user_input.strip():
            raise ValueError("Input cannot be empty.")

        # Count words using the word_count function
        count = word_count(user_input)

        # Display the word count
        print(f"Word Count: {count}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
