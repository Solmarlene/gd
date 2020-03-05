from django.http import HttpResponse

from .gender_detector import detect_gender


def index(request):
    return HttpResponse('''
        <html>
            <head>
                <title>Spanish word gender detection</title>
                <style>
                    html, body {
                        height: 100vh;
                    }
                    body {
                        margin: 0;
                        display: flex;
                        flex-flow: column;
                        align-items: center;
                        justify-content: center;
                    }
                </style>
            </head>
            <body>
                <svg xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 350">
                    <path d="M156.4,339.5c31.8-2.5,59.4-26.8,80.2-48.5c28.3-29.5,40.5-47,56.1-85.1c14-34.3,20.7-75.6,2.3-111  c-18.1-34.8-55.7-58-90.4-72.3c-11.7-4.8-24.1-8.8-36.8-11.5l-0.9-0.9l-0.6,0.6c-27.7-5.8-56.6-6-82.4,3c-38.8,13.6-64,48.8-66.8,90.3c-3,43.9,17.8,88.3,33.7,128.8c5.3,13.5,10.4,27.1,14.9,40.9C77.5,309.9,111,343,156.4,339.5z"/>
                </svg>
                <form method=GET action="./detect/">
                    <input type="text" name="word" placeholder="Enter a word">
                    <button type="submit">Check gender</button>
                </form>
            </body>
        </html>
    ''')


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

    return HttpResponse(format_gender(gender_detection_result))
