from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Conference  # Import the Conference model (adjust the import statement based on your model's location)
from home.models import Workshop  # Import the Conference model (adjust the import statement based on your model's location)
from home.models import Concert  # Import the Conference model (adjust the import statement based on your model's location)
from home.models import Seminar  # Import the Conference model (adjust the import statement based on your model's location)
from home.models import CommunityMeetup  # Import the Conference model (adjust the import statement based on your model's location)
from home.models import Category, Event
from . import views  # Import the views module

#from math import ceil
# Create your views here


from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Category, Event
from django.shortcuts import render, redirect
from django.urls import reverse


def delete_event(request, event_id):
	if request.method == 'POST':
		event = Event.objects.get(id=event_id)
		event.delete()
	return redirect(reverse('category_list'))


def create_event(request):
	if request.method == 'POST':
		# Retrieve data from the POST request
		name = request.POST.get('name')
		category_id = request.POST.get('category')
		start_date = request.POST.get('start_date')
		end_date = request.POST.get('end_date')
		priority = request.POST.get('priority')
		description = request.POST.get('description')
		location = request.POST.get('location')
		organizer = request.POST.get('organizer')

		# Retrieve the Category object
		category = Category.objects.get(pk=category_id)

		# Create the Event object
		event = Event.objects.create(
			name=name,
			category=category,
			start_date=start_date,
			end_date=end_date,
			priority=priority,
			description=description,
			location=location,
			organizer=organizer
		)

		# Redirect to the event list page
		return redirect('category_list')
	else:
		categories = Category.objects.all()
		return render(request, 'create_event.html', {'categories': categories})


def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.method == 'POST':
		# Update event fields based on form data
		event.name = request.POST.get('name')
		event.start_date = request.POST.get('start_date')
		event.end_date = request.POST.get('end_date')
		event.priority = request.POST.get('priority')
		event.description = request.POST.get('description')
		event.location = request.POST.get('location')
		event.organizer = request.POST.get('organizer')
		event.save()
		return redirect('category_list')
	else:
		# Render update event page with event data
		return render(request, 'update_event.html', {'event': event})

# def category_list(request):
# 	categories = Category.objects.all()
# 	return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories}) 

def create_category(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		Category.objects.create(name=name)
		return redirect('category_list')
	return render(request, 'create_category.html')


def delete_category(request, category_id):
	category = Category.objects.get(pk=category_id)
	if category.event_set.exists():
		messages.error(
			request, "You cannot delete this category as it contains events.")
	else:
		category.delete()
		messages.success(request, "Category deleted successfully.")
	return redirect('category_list')

def category_events(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	events = category.event_set.all()
	return render(request, 'category_events.html', {'category': category, 'events': events})

def event_chart(request):
	categories = Category.objects.all()
	pending_counts = {}
	for category in categories:
		pending_counts[category.name] = Event.objects.filter(
			category=category,
			start_date__gt=timezone.now()
		).count()
	return render(request, 'event_chart.html', {'pending_counts': pending_counts})



def index(request):

	# if request.method == 'POST':
	# 	name= request.POST[name]


    # Fetch data for different types of events
    conferences = Conference.objects.all()
    workshops = Workshop.objects.all()
    concerts = Concert.objects.all()
    seminars = Seminar.objects.all()
    community_meetups = CommunityMeetup.objects.all()

    #print(products)  # Debugging print statement
    # n= len(products)
    # nSlides= n//4 + ceil((n/4)%(n//4))

    
    # Pass the data to the template context
    context = {
        'conferences': conferences,
        'workshops': workshops,
        'concerts': concerts,
        'seminars': seminars,
        'community_meetups': community_meetups,
    }
     
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html' )
    #return HttpResponse("this is aboutpage")

def tracker(request):
    return render(request, 'tracker.html' )

def productview(request):
    return render(request, 'prodview.html' )

def checkout(request):
    return render(request, 'checkout.html' )



def services(request):
    return render(request, 'services.html' )
    #return HttpResponse("this is services page")

def about(request):
    return render(request, 'about.html')

def viewevent(request):
    return render(request, 'viewevent.html')

def createevent(request):
    return render(request, 'createevent.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save ()
        messages.success(request, 'Message sent.')
        # messages.success(request, "Your profile was updated.")  # ignored
    return render(request, 'contact.html' )

    #return HttpResponse("this is contact page")


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('category_list')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


from .models import Conference, Workshop, Concert, Seminar, CommunityMeetup

def search(request):
    search_query = request.GET.get('search')

    conferences = Conference.objects.filter(title__icontains=search_query)
    workshops = Workshop.objects.filter(title__icontains=search_query)
    concerts = Concert.objects.filter(title__icontains=search_query)
    seminars = Seminar.objects.filter(title__icontains=search_query)
    community_meetups = CommunityMeetup.objects.filter(title__icontains=search_query)

    context = {
        'conferences': conferences,
        'workshops': workshops,
        'concerts': concerts,
        'seminars': seminars,
        'community_meetups': community_meetups,
        'search_query': search_query
    }

    return render(request, 'search.html', context)

