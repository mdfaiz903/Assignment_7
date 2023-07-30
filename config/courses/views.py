from django.shortcuts import render,HttpResponse

# Create your views here.
def django_with_ai(request):
    course1 = "Web development"
    course2 = "Machine learning"
    course3 = "Deep learning"
    context = {
        'c1':course1,
        'c2':course2,
        'c3':course3,
        'c4': 8 ,
        'c5':'odd',
        'list':[1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,'courses/cours.html',context)

