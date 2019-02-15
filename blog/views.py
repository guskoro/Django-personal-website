from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post

def index(request):
	# do Queryset
    posts = Post.objects.all();

    context = {
		'app_css':'blog/css/styles.css',
		'banner':'blog/img/banner2.png',
		'contrib':'Macht mit Liebe',
		'heading':'Halo Liebe Leute !',
		'Posts':posts,
 	   	'subheading':'Wilkommen in Meine Website, Wir machen diese website mit Django',
		'title':'Gus | Blog',
		'nav' : [
			['/','Haus'],
	   		['/blog','Blog'],
	   		['/about','Über'],
	   		['/cv','Lebenslauf'],
	   		['/contact', 'Kontakt'],
	   		['/story', 'Geschichte']
		]
	}
    return render(request, 'blog/blog.html', context)

def categoryPost(request, categoryInput):
	posts = Post.objects.filter(category=categoryInput)

	return HttpResponse("category Post");

def singlePost(request, slugInput):
	posts = Post.objects.get(slug=slugInput)

	title = "<h1>{}</h1>".format(posts.title)
	body = "<p>{}<p>".format(posts.body)
	category = "<p>{}<p>".format(posts.category)

	return HttpResponse(title + body + category);