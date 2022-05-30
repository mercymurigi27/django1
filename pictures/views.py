from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.get_all_images()
    length = len(images)
    locations = Location.objects.all()

    context ={
        "images":images,
        "locations":locations,
        "length":length
    }

    return render(request,'pictures/index.html',context)

def search(request):

    if 'category' in request.GET and request.GET["category"]:
        query = request.GET.get("category")
        res = Image.search_by_category(query)
        length = len(res)
        message = f'Search results for {query}'
        locations = Location.objects.all()
        
        
        context = {
            'images': res,
            "message":message,
            "length":length,
            "query":query,
            "locations":locations
        }

        return render(request,'pictures/search.html',context)

    else:
        message = 'You have not searched for any item'
        return render(request,'pictures/search.html',message)
def filter_location(request):
    if 'location' in request.GET and request.GET["location"]:
        query = request.GET.get("location")
        res = Image.filter_by_location(query)
        locations = Location.objects.all()
        length = len(res)
        message = f'{query}'

        context = {
            'images': res,
            "message":message,
            "length":length,
            "locations":locations,
            "query":query
        }

        
        
        return render(request,'pictures/location.html',context)

    else:
        return render(request,'pictures/location.html',context)
