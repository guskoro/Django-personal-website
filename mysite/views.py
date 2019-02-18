from django.http import HttpResponse
from django.shortcuts import render

from .forms import FormField
# method veiw index
def index(request):
	form_field = FormField()
	context = {
		'banner':'img/banner2.png',
		'contrib':'Macht mit Liebe',
		'data_form':form_field,
		'heading':'Halo Liebe Leute !',
		'subheading':'Wilkommen in Meine Website, Wir machen diese website mit Django',
		'title':'Gus Website',
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