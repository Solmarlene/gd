from django.http import HttpResponse

from .gender_detector import detect_gender


def index(request):
    return HttpResponse('''
        <html>
        <form method=GET action="./detect/">
            <input type="text" name="word" placeholder="Enter a word">
            <button type="submit">Check gender</button>
        </form>
    ''')


def detect(request):
    user_word = request.GET['word']

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

    return HttpResponse(gender_detection_result)
