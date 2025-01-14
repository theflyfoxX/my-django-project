from django.test import TestCase
from django.urls import reverse
from mydogs.models import Dog, Breed

class TestDogViews(TestCase):
    def setUp(self):
        self.breed = Breed.objects.create(
            name="Golden Retriever",
            size="Large",
            friendliness=5,
            trainability=5,
            sheddingamount=4,
            exerciseneeds=4
        )
        self.dog = Dog.objects.create(
            name="Buddy",
            age=3,
            breed=self.breed
        )

    def test_dog_list_view(self):
        # Test GET request to dog list
        response = self.client.get(reverse('dogs_list'))
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(len(response.json()), 1)   
        self.assertEqual(response.json()[0]['name'], 'Buddy')  

    def test_dog_detail_view(self):
      response = self.client.get(reverse('dogs_detail', args=[self.dog.id]))
      self.assertEqual(response.status_code, 200)  # Check HTTP status code
      self.assertEqual(response.json()['name'], 'Buddy')  # Check dog name
      self.assertEqual(response.json()['breed'], self.breed.id)  # Check breed ID


    def test_dog_detail_not_found(self):
        # Test GET request for a non-existent dog
        response = self.client.get(reverse('dogs_detail', args=[999])) 
        self.assertEqual(response.status_code, 404)  
