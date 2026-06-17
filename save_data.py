from app.services.scraper import scrape_website
from app.services.vector_db import collection

content = scrape_website("https://ashar.innovatesoftwaresolution.com/")

collection.add(
    documents=[content],
    ids=["client_1"]
)

print("DATA SAVED")