import random, string
from django.db import models, IntegrityError
from bloom_filter import BloomFilter

# Using bloom filter for minimizing access to the database for every repeated id for this instance
MAX_ELEMENTS = 1000000
EPSILON = 0.1
BLOOM = BloomFilter(max_elements=MAX_ELEMENTS, error_rate=EPSILON)

class User(models.Model):
    real_world_id = models.CharField(max_length=10, unique=True)
    username = models.CharField(max_length=50)
    timeZone = models.CharField(null=False, max_length=64)   

    def _getUniqueId(self):
        exists = True
        while exists:
            rwid = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 9))
            if rwid in BLOOM:           # If bloom has seen the data no need to access database
                continue                # prevents repeated access to db for seen random id's
            else:
                exists = User.objects.filter(real_world_id=rwid).exists()
                BLOOM.add(rwid)         # Bloom sees the data

        return rwid

    def save(self, *args, **kwargs):
        
        if self.real_world_id == None or not self.real_world_id:            
            self.real_world_id = self._getUniqueId()

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.username)