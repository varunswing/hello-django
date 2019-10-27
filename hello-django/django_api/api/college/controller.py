from django.http import JsonResponse

def get_students(request):
    data = {
        "all_students": [
            {
                "Name": "Varun Sharma",
                "Roll No.": 101
            },
            {
                "Name": "Varun Sharma",
                "Roll No.": 102
            },
            {
                "Name": "Varun Sharma",
                "Roll No.": 103
            }
        ]
    }
    return JsonResponse(data)