from django.http import HttpResponse
from django.template import loader

from .gender_detector import detect_gender


def index(request):
    template = loader.get_template('home.html')
    final_html = template.render({}, request)
    return HttpResponse(final_html)


def format_gender(dr):
    parts = dr.split("|")
    pretty_gender = None
    for part in parts:
        if "Gender" in part:
            short_gender = part.split("=")[1]
            if short_gender == "Fem":
                pretty_gender = "Feminine"
            else:
                pretty_gender = "Masculine"
    return pretty_gender


def detect(request):
    user_word = request.GET['word']

    gender_detection_result = detect_gender(user_word)

    format_gender(gender_detection_result)



    # "BLAHBLAHBLAH_Gender=Masc|BLAHBLAHBLAH"
    # 1. Check whether substring “Gender” appears at all
    # TIP: use gender_detection_result.find()

    # 2. If it appears, take part after the “=” until the “|”
    # TIP: try using string replacement or regexp (regular expression) matching

    # 3. If that part is “Masc”, then return “this word is of masculine gender”.
    # If it is “Fem”, return “this word is of feminine gender”.
    # And in all other cases, return “could not detect gender”.
    # TIP: use if/elif/else conditionals

    result_string = format_gender(gender_detection_result)

    template = loader.get_template('result.html')

    context = {
        'word_in_question': user_word,
        'gender_detection_result': result_string,
    }

    final_html = template.render(context, request)
    return HttpResponse(final_html)
