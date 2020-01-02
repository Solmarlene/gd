import spacy


processor = spacy.load('es_core_news_sm')


def detect_gender(text):
    """
    Takes text, detects gender of the first word (if applicable)
    and returns a string "feminine", "masculine", or "n/a".
    """
    processed_text = processor(text)
    first_word = processed_text[0]

    tag = first_word.tag_
    # "NOUN__Gender=Fem|Number=Sing"

    return tag
