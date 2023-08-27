from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .scraper import PopularScraper, TopTenScraper, MostViewedScraper
from .models import PopularMangaModel, TopTenMangaModel, MostViewedMangaModel

router = APIRouter()

@router.get("/")
async def root():
	return { "message": "MangaAPI V1 API" }

@router.get("/popular", response_model=list[PopularMangaModel])
async def get_trending_mangas() -> list[PopularMangaModel]:
	response = PopularScraper().scrape()
	return response

@router.get("/top-10", response_model=list[TopTenMangaModel])
async def get_top_ten() -> list[TopTenMangaModel]:
	response = TopTenScraper().scrape()
	return response

@router.get("/most-viewed/{chart}", response_model=List[MostViewedMangaModel])
async def get_most_viewed(chart: str):
	most_viewed_scraper = MostViewedScraper()
	
	if chart in most_viewed_scraper.CHARTS:
		data = most_viewed_scraper.scrape_chart(chart)
		return data
	else:
		message = {"message": "Invalid time period specified."}
		return JSONResponse(content=message, status_code=400)