import uvicorn
from fastapi import FastAPI
from api.components.routes import route


tags_metadata = [
    {"name": "level",
    "description": "You must select a risk level: **high /medium /none**"},
    {"name":'all_events',
    "description": "You can choose whether to receive the full text or just a summary of data: **True or False**"},
    {'name':'agg',
     "description": "You must choose between the option: **min /max /avg** "},
    {'name': 'free_text',
     'description': 'You can type free text to search, and you must also select operator: and / or'}

   ]



app = FastAPI(openapi_tags=tags_metadata)


app.include_router(route)



if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)