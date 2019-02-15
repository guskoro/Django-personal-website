from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title':'Gus | Über',
		'contrib':'Macht mit Liebe',
		'heading':'Halo Liebe Leute !',
 	   	'subheading':'Wilkommen in Meine Website, Wir machen diese website mit Django',
		'app_css':'about/css/styles.css',
		'banner':'about/img/banner2.png',
	   	'nav': [
	   		['/','Haus'],
	   		['/blog','Blog'],
	   		['/about','Über'],
	   		['/cv','Lebenslauf'],
	   		['/contact', 'Kontakt'],
	   		['/story', 'Geschichte']
	   ]
	}
	return render(request, 'about/about.html', context)

def story(request):
	context = {
		'title':'Gus | Geschichte',
		'contrib':'Macht mit Liebe',
		'heading':'Halo Liebe Leute !',
 	   	'subheading':'Wilkommen in Meine Website, Wir machen diese website mit Django',
		'app_css':'about/css/styles.css',
		'banner':'about/img/banner2.png',
	   	'nav': [
	   		['/','Haus'],
	   		['/blog','Blog'],
	   		['/about','Über'],
	   		['/cv','Lebenslauf'],
	   		['/contact', 'Kontakt'],
	   		['/story', 'Geschichte']
	   ]
	}
	return render(request, 'about/story.html', context)