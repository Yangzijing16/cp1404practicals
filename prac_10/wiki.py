"""
Wikipedia API program for CP1404 Practical 10.
Name: Yang Zijing
ID: 14817731
Description: Prompts for a Wikipedia page title or search phrase, displays title, summary, and URL.
Handles DisambiguationError and PageError exceptions. Continues until blank input.
"""
import wikipedia

# Named constants
SEARCH_PROMPT = "Enter page title: "
EXIT_MESSAGE = "Thank you."
DISAMBIGUATION_MESSAGE = "We need a more specific title. Try one of the following, or a new search:"
PAGE_NOT_FOUND_MESSAGE = 'Page id "{}" does not match any pages. Try another id!'


def main():
    """Run Wikipedia search program with user input loop."""
    run_search_loop()


def run_search_loop():
    """Loop to get user input and fetch Wikipedia pages.

    Returns:
        bool: False to exit the program.
    """
    is_running = True
    while is_running:
        search_term = input(SEARCH_PROMPT).strip()
        if not search_term:
            print(EXIT_MESSAGE)
            is_running = False
        else:
            fetch_wikipedia_page(search_term)
    return False


def fetch_wikipedia_page(search_term):
    """Fetch and display Wikipedia page details or handle exceptions.
    """
    try:
        page = wikipedia.page(search_term, auto_suggest=False)
        print(page.title)
        print(wikipedia.summary(search_term, sentences=2))
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(DISAMBIGUATION_MESSAGE)
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(PAGE_NOT_FOUND_MESSAGE.format(search_term))

main()