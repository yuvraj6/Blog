from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comment
from blog.forms import Postform,Commentform
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required#to check for authentication of user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    DeleteView,UpdateView)


# Create your views here.

class AboutView(TemplateView):
    template_name='about.html'


class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
        #above is like the select query where the to select all the post where the publsh Date
        # is less than equal to current time and order by the publish date
class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    # above two variables are required whenver we use LoginRequiredMixin to authenticate user
    form_class=Postform
    model=Post

class PostUpdateView(UpdateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=Postform
    model=Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('create_date')

##comment form views#############
@login_required#this decorator is required that the user is logged in to comment on any blog
#every post has primary key (pk) so in order to comment on post we are taking request and pk
#to do that
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    #when someone filled the form and hit enter then the below part will execute teo check
    if request.method == 'POST':
        form=Commentform(request.POST)
        if form.is_valid():#meaning no detail is missing
            comment=form.save(commit=False)#to rememeber the form and here false as we are not commitng to db
            comment.post=post #models.py hascomment model which has field ' post' as a foreign key of Post model
            comment.save()
            return redirect('post_detail',pk=post.pk)#and when every thing is fine ust post this to post detail page with the
            #blog post primary key where we are commeting
    else:#just keep rendering the commnet form
        form=Commentform()
    return render(request,'blog/comment_form.html',{'form':form})



@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
