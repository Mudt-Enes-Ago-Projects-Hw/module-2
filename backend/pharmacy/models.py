from django.db import models
from algorithms.generateID import generate_id


class Medicine(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Generate unique ID
            while True:
                new_id = generate_id()
                if not Medicine.objects.filter(id=new_id).exists():
                    self.id = new_id
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
