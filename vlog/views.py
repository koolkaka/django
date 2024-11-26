from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import VlogPost
from .forms import VlogPostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages

class VlogListView(ListView):
    model = VlogPost
    template_name = 'vlog_list.html'
    context_object_name = 'vlogs'
    paginate_by = 10

class VlogDetailView(DetailView):
    model = VlogPost
    template_name = 'vlog_detail.html'
    context_object_name = 'vlog'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please enter the fields in the correct format.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)
        
def profile(request):
    user_posts = VlogPost.objects.filter(author=request.user)
    return render(request, 'profile.html', {'user_posts': user_posts})


class VlogCreateView(LoginRequiredMixin, CreateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = "vlog_form.html"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.video_url = self.convert_youtube_url(form.instance.video_url)
        messages.success(self.request, "Your vlog has been created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))

    def convert_youtube_url(self, url):
        if "watch?v=" in url:
            return url.replace("watch?v=", "embed/")
        elif "youtu.be/" in url:
            return url.replace("youtu.be/", "www.youtube.com/embed/")
        return url

class VlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = "vlog_form.html"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.video_url = self.convert_youtube_url(form.instance.video_url)
        messages.success(self.request, "Your vlog has been updated successfully!")
        return super().form_valid(form)

    def convert_youtube_url(self, url):
        if "watch?v=" in url:
            return url.replace("watch?v=", "embed/")
        elif "youtu.be/" in url:
            return url.replace("youtu.be/", "www.youtube.com/embed/")
        return url

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        vlog = self.get_object()
        return self.request.user == vlog.author

class VlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        vlog = self.get_object()
        return self.request.user == vlog.author
