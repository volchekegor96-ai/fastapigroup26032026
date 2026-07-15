from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from storage import storage
from schemas import TourCreateSchema, TourUpdateSchema

router = APIRouter(prefix="/api/tours", tags=["Tours"])


def tour_helper(tour) -> dict:
    return {
        "id": str(tour["_id"]),
        "title": tour["title"],
        "country": tour["country"],
        "price": tour["price"],
        "duration_days": tour["duration_days"],
        "description": tour["description"],
        "is_available": tour["is_available"]
    }


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_tour(tour_data: TourCreateSchema):
    new_tour = await storage.tours.insert_one(tour_data.model_dump())
    created_tour = await storage.tours.find_one({"_id": new_tour.inserted_id})
    return tour_helper(created_tour)


@router.get("/", response_model=list)
async def get_all_tours():
    tours = []
    async for tour in storage.tours.find():
        tours.append(tour_helper(tour))
    return tours


@router.get("/{id}", response_model=dict)
async def get_tour(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Некоректний id")
    tour = await storage.tours.find_one({"_id": ObjectId(id)})
    if not tour:
        raise HTTPException(status_code=404, detail="Тур не знайдено")
    return tour_helper(tour)


@router.put("/{id}", response_model=dict)
async def update_tour(id: str, tour_data: TourUpdateSchema):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Некоректний id")

    update_dict = {k: v for k, v in tour_data.model_dump().items() if v is not None}

    if len(update_dict) >= 1:
        update_result = await storage.tours.update_one(
            {"_id": ObjectId(id)}, {"$set": update_dict}
        )
        if update_result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Тур не знайдено або дані не змінено")

    existing_tour = await storage.tours.find_one({"_id": ObjectId(id)})
    if not existing_tour:
        raise HTTPException(status_code=404, detail="Тур не знайдено")
    return tour_helper(existing_tour)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_tour(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Некоректний id")
    delete_result = await storage.tours.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Тур успішно видалено"}
    raise HTTPException(status_code=404, detail="Тур не знайдено")
from fastapi import APIRouter, status

from schemas import BookCreateSchema

api_router = APIRouter(
    prefix='/api/books'
)


@api_router.get('')
def index_books():
    return 2222


@api_router.post('', status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreateSchema) -> BookCreateSchema:
    """the single endpoint for creating book in storage"""
    print(book)
    print(type(book))
    return book
