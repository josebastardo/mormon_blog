from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
# Forms
from .forms import SignupForm, profileForm
from .models  import Profile
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


class SignupView(FormView):
	"""Users sign up view."""
	template_name = 'users/register.html'
	form_class = SignupForm
	success_url = reverse_lazy('users:registerok')
	def form_valid(self, form):
		"""Save form data."""
		form.save()
		return super().form_valid(form)

@login_required
def user_details(request):
   if request.method == 'POST':
       form = profileForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')

