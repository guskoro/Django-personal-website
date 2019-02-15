from django.http import HttpResponse
from django.shortcuts import render

# method veiw index
def index(request):
	context = {
	   'title':'Gus Website',
	   'heading':'Halo Liebe Leute !',
	   'subheading':'Wilkommen in Meine Website, Wir machen diese website mit Django',
	   'contrib':'Macht mit Liebe',
	   'banner':'img/banner2.png',
	   'nav': [
	   		['/','Haus'],
	   		['/blog','Blog'],
	   		['/about','Über'],
	   		['/cv','Lebenslauf'],
	   		['/contact', 'Kontakt'],
	   		['/story', 'Geschichte']
	   ]
	}
	return render(request, 'index.html', context)