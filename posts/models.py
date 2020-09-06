from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

from categories.models import Category


class Post(models.Model):
	"""Post model."""

	user = models.ForeignKey(User, on_delete=models.PROTECT)
	profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

	title = models.CharField(max_length=50)
	image_header = models.ImageField(upload_to='posts/photos', default= 'posts/photos/ Sin título.png')
	post = RichTextField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	is_draft = models.BooleanField(default=True)
	url = models.SlugField(max_length=50, unique=True)
	views = models.PositiveIntegerField(default=0)
	categories = models.ManyToManyField(Category)
	hit_count_generic =GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

	class Meta:
		ordering = ('-created', 'title')

	def get_absolute_url(self):
		return ('post:detail', (), {'url' :self.url,})



	def __str__(self):
		"""Return title and username."""
		return '{} by @{}'.format(self.title, self.user.username)


	def save(self, *args, **kwargs):
		self.url = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
	name = models.CharField(max_length=40)
	profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
	text =RichTextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.text, self.name)



