import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing) to allow web pages
# to request data from this API.
# This is essential for web-based mind map viewers.
origins = [
    "*",  # In a production environment, you would restrict this to specific domains.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the mind map data from the JSON file when the application starts.
# It includes error handling in case the file is not found or is not valid JSON.
try:
    with open('mindmap.json', 'r', encoding='utf-8') as f:
        mindmap_data = json.load(f)
except FileNotFoundError:
    mindmap_data = {"error": "The mindmap.json file was not found."}
except json.JSONDecodeError:
    mindmap_data = {"error": "There was an error decoding the mindmap.json file."}


# Define the API endpoint that will serve the mind map data.
# When a GET request is made to /api/mindmap, this function will be called.
@app.get("/api/mindmap")
def get_mindmap_data():
    """
    This endpoint returns the structured mind map data loaded from the
    mindmap.json file.
    """
    return mindmap_data
