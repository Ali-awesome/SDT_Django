from django.shortcuts import render

# Create your views here.
d = {
    'sport1' : "cricket",
    'sport2' : "football",
    'sport3' : "basketball",
    'person' : [
        {
            'name' : "Helal",
            'age' : 24,
            'job' : "Mechanic"
        },
        {
            'name' : "Mehedi",
            'age' : 25,
            'job' : "Chemist"
        },
        {
            'name' : "Saki",
            'age' : 22,
            'job' : "Engineer"
        },
        {
            'name' : "Ali",
            'age' : 26,
            'job' : "Merchendiser"
        }
    ]
}
def app(request):
    return render(request, 'contextapp/app.html', d)