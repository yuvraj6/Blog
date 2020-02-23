from django import forms
from blog.models import Post,Comment

class Postform(forms.ModelForm):

    class Meta():
        model=Post
        fields=('author','title','text')
        #here textinputclass is a css which is under staticfolder of application not project(mysite)
        #we will create both the class
        #postcontent is the content which user will type in the blog
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }



class Commentform(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
