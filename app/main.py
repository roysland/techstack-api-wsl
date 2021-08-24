from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from helpers import db
app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return { "message": "Hello world" }

@app.get("/trending")
async def trending():
    statement = """
       SELECT 
	techs.tech, count(*) count,
    tech_definitions.category,
    tech_definitions.tech_group,
    tech_definitions.variation_of
FROM techs 

LEFT JOIN tech_definitions ON lower(techs.tech) = lower(tech_definitions.name)

GROUP BY techs.tech 
HAVING count(techs.tech)
ORDER BY count DESC; 
    """
    results = db.cursor.execute(statement).fetchall()

    return { "data": results }
    
@app.get('/jobdensity')
async def jobdensity():
    statement = """
        SELECT locations.kommune, count(*) as count FROM locations GROUP BY locations.kommune;
    """
    results = db.cursor.execute(statement).fetchall()
    return { "data": results }

@app.get('/allTechs')
async def allTags():
    statement = """
        SELECT tech, count(*) as count FROM techs GROUP BY tech ORDER BY count DESC; 
    """
    results = db.cursor.execute(statement).fetchall()

    return { "data": results }

@app.get('/locations')
async def getLocations():
    statement = """

    """
    results = db.cursor.execute(statement).fetchall()

    return { "data": results }