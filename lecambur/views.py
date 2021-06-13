from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect




class HomePageView(TemplateView):
   template_name = 'home.html'
   
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-published_date')
        return context
    
class TopicListView(ListView):
    paginate_by = 4
    model = Post
    template_name = 'actualites.html'
    context_object_name = 'posts'
 
    def get_queryset(self):
        return Post.objects.order_by('-published_date')
        
class PostDetailView(DetailView):
    model = Post
    template_name = 'actualites/article_detail.html'
    
    
def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
        send_mail(subject, message, sender, ['sami.nouari@gmail.com'])
        return HttpResponseRedirect('thanks/')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')
    
    