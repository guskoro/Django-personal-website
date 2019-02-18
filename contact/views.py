from django.shortcuts import render

from .forms import ContactForm
# Create your views here.
def index(request):
	contact_form = ContactForm()
	context = {
		'title':'Gus | Kontakt',
		'contrib':'Macht mit Liebe',
		'data_form':contact_form,
		'heading':'Halo Liebe Leute !',
 	   	'subheading':'Wilkommen in Meine Website, Wir machen diese website mit Django',
		'banner':'contact/img/banner2.png',
		'app_css':'contact/css/styles.css',
		'nav': [
			['/','Haus'],
	   		['/blog','Blog'],
	   		['/about','Über'],
	   		['/cv','Lebenslauf'],
	   		['/contact', 'Kontakt'],
	   		['/story', 'Geschichte']
		]
	}

	# if request.method == 'POST':
	# 	context['nama'] = request.POST['nama']
	# 	context['alamat'] = request.POST['alamat']
	# else:
	# 	print("Ini get")
		
	return render(request, 'contact/contact.html', context)