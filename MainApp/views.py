from django.shortcuts import render

# Create your views here.


def basehtml(request):
    return render(request, 'base.html')


def recipies(request):

    if request.method == 'POST':  
        data = request.POST
        recipie_name = data['recipie_name']
        recipie_description = data['recipie_description']
        if request.FILES['recipie_image']:
            recipie_image = request.FILES['recipie_image']
        print(recipie_name)
        print(recipie_description)
        print(recipie_image)

    return render(request, 'recipies.html')
