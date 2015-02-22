# from django.template import RequestContext
# from django.shortcuts import render_to_response
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib import auth
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponseRedirect,Http404,HttpResponse
# from django.template.loader import get_template
# from django.template import Context
# from django.core.mail import send_mail, EmailMessage
# from django.contrib.auth import logout
# from cabs.models import *
# from django.contrib.auth.decorators import login_required
# from cabs.views import *

# def home(request):
# 	if request.user.is_authenticated():
# 		context = RequestContext(request)
# 		context_dict = {}
# 		return render_to_response('home.html', context_dict, context)
# 	else:
# 		context = RequestContext(request)
# 		context_dict = {}
# 		return render_to_response('about.html', context_dict, context)