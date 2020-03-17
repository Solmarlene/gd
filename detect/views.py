from django.http import HttpResponse
from django.template import loader
from genders.models import Entry

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
    user_word = request.GET['word'].strip()

    if user_word != '':
        genders = Entry.objects.filter(word=user_word).values_list('gender', flat=True)

        if len(genders) < 1:
            gender_detection_result = detect_gender(user_word)

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

        elif len(genders) == 1:
            gender = genders[0]
            if gender == "M":
                result_string = "Masculine"
            elif gender == "F":
                result_string = "Feminine"
            else:
                result_string = "Both"
        else:
            print(genders)
            if 'B' in genders or ('F' in genders and 'M' in genders):
                result_string = "Both"
            elif 'F' in genders:
                result_string = "Feminine"
            else:
                result_string = "Masculine"
                

        context = {
            'word_in_question': user_word,
            'gender_detection_result': result_string,
        }

    else:
        context = {
            'error': "Whoops! You didn’t enter anything, it appears D:"
        }

    template = loader.get_template('result.html')
    final_html = template.render(context, request)
    return HttpResponse(final_html)
