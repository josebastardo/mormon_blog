
from hitcount.views import HitCountDetailView
from django.shortcuts import  get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from posts.forms import CommentForm
from django.db.models import Q

# Models
from posts.models import Post
from categories.models import Category

# Forms

class PostCountHitDetailView(HitCountDetailView):
    model = Post        # your model goes here
    count_hit = True    # set to True if you want it to try and count the hit


class SearchResultsView(ListView):
	model = Post
	template_name = 'posts/search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		object_list = Post.objects.filter( Q (categories__name=query) | Q(user__username__icontains=query) | Q(title__icontains=query) )

		return object_list



class PostsFeedView(ListView):
	"""Index."""
	template_name = 'posts/index.html'
	model = Post
	ordering = ('-created',)
	paginate_by = 6
	context_object_name = 'posts'
	#queryset = Post.objects.filter(is_draft=False)
	posts = Post.objects.filter(is_draft=False)	


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context


@staff_member_required
class PostsUpdate(UpdateView):
	model = Post    
	fields = ['title', 'post']



def view_post(request, url):	
	post = get_object_or_404(Post, url=url)     	
	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.name=request.user.username
		comment.profile=request.user.profile
		comment.save()
		request.session["name"] = comment.name

		return redirect(request.path)

	form.initial['name'] = request.session.get('name')

	return render(request, 'posts/detail.html',{'post': post, 'form':form, })




@login_required
def save_comment(request):
    if request.method == 'POST':
        url = request.POST['url']
        post = {
            'user': request.user.id,
            'profile': request.user.id,
            'comment': request.POST['comment'],
            'post': request.POST['post']
        }
        form = CreateCommentForm(post)
        if form.is_valid():
            form.save()
            return redirect('comments:comments')  #redirect('posts:detail', url=url)
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)

