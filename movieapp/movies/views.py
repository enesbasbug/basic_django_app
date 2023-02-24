from django.shortcuts import render
from .models import Category, Movie

# categorie_list = ["adventure", "romantic", "dram", "science fiction"]
# movie_list = [
#     {
#         "id" : 1,
#         "movie_name" : "movie_1",
#         "movie_description" : "Description for movie - 1",
#         # "image" : "https://picsum.photos/200/300?random=1",
#         "image" : "1.jpg",
#         "homepage" : True
#     },
#     {
#         "id" : 2,
#         "movie_name" : "movie_2",
#         "movie_description" : "Description for movie - 2",
#         # "image" : "https://picsum.photos/200/300?random=2",
#         "image" : "2.jpg",
#         "homepage" : True    
#     },
#     {
#         "id" : 3,
#         "movie_name" : "movie_3",
#         "movie_description" : "Description for movie - 3",
#         # "image" : "https://picsum.photos/200/300?random=3",
#         "image" : "3.jpg",
#         "homepage" : False  
#     },
#     {
#         "id" : 4,
#         "movie_name" : "movie_4",
#         "movie_description" : "Description for movie - 4",
#         # "image" : "https://picsum.photos/200/300?random=4",
#         "image" : "4.jpg",
#         "homepage" : False   
#     },
    
# ]




# Create your views here.
def home(request):
    data = {
        "categories": Category.objects.all(),
        # "movies": Movie.objects.all(),
        "movies": Movie.objects.filter(homepage=True),
    }
    return render(request, "index.html", data)


def movies(request):
    data = {
        "categories": Category.objects.all(),
        "movies": Movie.objects.all(),
    }
    return render(request, "movies.html", data)

def movie_details(request, id):
    data = {
        "movie": Movie.objects.get(id=id),
    }
    return render(request, "details.html", data)