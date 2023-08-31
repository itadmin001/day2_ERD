import requests
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
x=0
data = []
ids = []
output = {}

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="ITadmin0ut@",
    host="localhost",
    database="theater"
)

engine = create_engine(url)

# engine = create_engine('postgresql+psycopg2://postgres:ITadmin0ut@\
# @postgres/theater')

Session = sessionmaker(bind=engine)
session = Session()


for y in range(1,6):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjg3MjVlZDI0Nzc2ZmZkNmQxOTAyNjE3ODE3ZGFiOSIsInN1YiI6IjY0ZWZiZWMxM2E5OTM3MDExY2JkNDg4OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmRjJfChKiVwHB5gkT7738EkCRrGH8Dq2BULptzlURQ"
    }
   
    response = requests.get(url, headers=headers)
    data.append(response.json())
    
    for value in data:
        print(f"x:{x} y:{y}")
        ids.append(data[0]['results'][x]['id'])
        x+=1
for id in ids:       
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYjg3MjVlZDI0Nzc2ZmZkNmQxOTAyNjE3ODE3ZGFiOSIsInN1YiI6IjY0ZWZiZWMxM2E5OTM3MDExY2JkNDg4OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LmRjJfChKiVwHB5gkT7738EkCRrGH8Dq2BULptzlURQ"
    }

    response = requests.get(url, headers=headers)

    results = response.json()
    with engine.connect() as conn:
        if results['id'] != 615656: ## <<-- manually pre-inserted value ##
            movie = text(f"INSERT INTO Movie (movie_id,movie_name,movie_cat,movie_len,movie_rating,movie_rel_date) VALUES({results['id']},\'{results['title']}\',\'{results['genres'][0]['name']}\',{results['runtime']},'R',\'{results['release_date']}\')".replace(':',""))
            
            session.execute(movie)
            session.commit()
   
