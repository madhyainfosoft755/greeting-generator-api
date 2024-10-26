from django.db import models

# 1. Client Model
class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='client_logos/') # Image field for logo
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15) # Assuming phone numbers as strings
    website = models.URLField(blank=True, null=True)
    tagline =  models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# 2. Festival Model
class Festival(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# 3. Template Model
class Template(models.Model):
    greeting_cards = models.ImageField(upload_to='greeting_cards/')  
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)  # Linking Template to Festival
    #client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Linking Template to Festival

    def __str__(self):
        return f"Template for {self.festival.name}"

# 4. Quatation Model
class Quotation(models.Model):
    quote = models.TextField()
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)  # Linking Quotation to Festival

    def __str__(self):
        return f"Quotation for {self.festival.name}"

        