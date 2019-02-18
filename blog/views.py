from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post

def index(request):
	# do Queryset
    posts = Post.objects.all();
    categories = Post.objects.values('category').distinct();
    context = {
		'app_css':'blog/css/styles.css',
		'banner':'blog/img/banner2.png',
		'Categories':categories,
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
	categories = Post.objects.values('category').distinct();
	context = {
		'app_css':'blog/css/styles.css',
		'banner':'blog/img/banner2.png',
		'Categories':categories,
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
	return render(request, 'blog/category.html', context)

def detailPost(request, slugInput):
	posts = Post.objects.get(slug=slugInput)
	categories = Post.objects.values('category').distinct();
	context = {
		'app_css':'blog/css/styles.css',
		'banner':'blog/img/banner2.png',
		'Categories':categories,
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
	return render(request, 'blog/detail.html', context)