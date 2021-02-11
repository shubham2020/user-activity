from django.db import models

class ActivityPeriod(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	user = models.ForeignKey('Member.User', related_name='activity_periods', on_delete=models.CASCADE)

	def __str__(self):
		return "{} {}".format(self.start_time, self.end_time)