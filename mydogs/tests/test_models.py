from django.test import TestCase
from mydogs.models import Breed, Dog

class TestModels(TestCase):
    def setUp(self):
        self.breed1 = Breed.objects.create(
            name="Golden Retriever",
            size="LARGE",
            friendliness=5,
            trainability=4,
            sheddingamount=3,
            exerciseneeds=4
        )
        
        self.dog1 = Dog.objects.create(
            name="Buddy",
            age=3,
            breed=self.breed1,
        )

    def test_breed_creation(self):
        breed = Breed.objects.get(name="Golden Retriever")
        self.assertEqual(breed.size, "LARGE")
        self.assertEqual(breed.friendliness, 5)

    def test_dog_creation(self):
        dog = Dog.objects.get(name="Buddy")
        self.assertEqual(dog.age, 3)
        self.assertEqual(dog.breed.name, "Golden Retriever")
