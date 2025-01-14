import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab.settings')  
django.setup()

from mydogs.models import Breed, Dog

def populate():
    golden_retriever = Breed.objects.create(
        name="Golden Retriever",
        size="LARGE",
        friendliness=9,
        trainability=8,
        sheddingamount=7,
        exerciseneeds=8
    )

    labrador = Breed.objects.create(
        name="Labrador",
        size="LARGE",
        friendliness=8,
        trainability=7,
        sheddingamount=6,
        exerciseneeds=7
    )

    german_shepherd = Breed.objects.create(
        name="German Shepherd",
        size="LARGE",
        friendliness=7,
        trainability=9,
        sheddingamount=5,
        exerciseneeds=9
    )

    Dog.objects.create(
        name="Buddy",
        age=3,
        breed=golden_retriever,
        gender="Male",
        color="Golden",
        favoritefood="Chicken",
        favoritetoy="Ball"
    )

    Dog.objects.create(
        name="Bella",
        age=2,
        breed=labrador,
        gender="Female",
        color="Black",
        favoritefood="Beef",
        favoritetoy="Frisbee"
    )

    Dog.objects.create(
        name="Max",
        age=4,
        breed=german_shepherd,
        gender="Male",
        color="Brown",
        favoritefood="Fish",
        favoritetoy="Rope"
    )

    print("Database populated successfully!")

if __name__ == "__main__":
    populate()
