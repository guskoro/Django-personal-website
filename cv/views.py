from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title':'Gus | Lebenslauf',
		'contrib':'Macht mit Liebe',
		'heading':'Halo Liebe Leute !',
 	   	'subheading':'Wilkommen in Meine Website, Wir machen diese website mit Django',
		'banner':'cv/img/banner2.png',
		'app_css':'cv/css/styles.css',
		'nav': [
			['/','Haus'],
	   		['/blog','Blog'],
	   		['/about','Über'],
	   		['/cv','Lebenslauf'],
	   		['/contact', 'Kontakt'],
	   		['/story', 'Geschichte']
		]
	}
	return render(request, 'cv/cv.html', context)
