# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def above_5_5(movie):
    """Check if the IMDB score of a movie is above 5.5."""
    return movie["imdb"] > 5.5

def filter_above_5_5(movies):
    """Return a sublist of movies with an IMDB score above 5.5."""
    return [movie for movie in movies if above_5_5(movie)]

def filter_by_category(movies, category):
    """Return movies under a specific category."""
    return [movie for movie in movies if movie["category"] == category]

def filter_by_name(movies, name):
    """Return movies with a specific name."""
    return [movie for movie in movies if movie["name"] == name]

def average_imdb_score(movies):
    """Compute the average IMDB score of a list of movies."""
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

def average_imdb_score_by_category(movies, category):
    """Compute the average IMDB score of movies under a specific category."""
    category_movies = filter_by_category(movies, category)
    return average_imdb_score(category_movies)


category = input("Enter category: ")
film_name = input("Enter film name: ")

filtered_movies = filter_by_category(movies, category)
if film_name:
    filtered_movies = filter_by_name(filtered_movies, film_name)

print("Filtered movies:")
for movie in filtered_movies:
    print(movie)

print("Average IMDB score:", average_imdb_score(filtered_movies))