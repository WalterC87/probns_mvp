from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *

def userType_view(request, desc):
	"""try:
		user_type = tipoUsuario.objects.get(description=desc)
	except tipoUsuario.DoesNotExist:
		raise Http404"""

	user_type = get_object_or_404(tipoUsuario, description=desc)

	return render(request)