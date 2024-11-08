from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from poster_templates.models import Client, Festival  
from .forms import FestivalForm, ClientForm # Import the form    
from django.core.serializers import serialize   

# def admin_clients(request):
#     clients = Client.objects.all()  # Fetch all client records
#     context = {"title": "Clients", 'clients': clients}
#     return render(request, 'greeting/admin/clients.html', context)



# Create your views here.

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:  # Check if the user is active
                    login(request, user)
                    if user.is_superuser:
                        # return render(request, 'greeting/admin/dashboard.html')
                        return redirect('/admin-dashboard')
                    else:
                        # return render(request, 'greeting/user/dashboard.html')
                        return redirect('/user-dashboard')
                else:
                    messages.error(request, "Your account is inactive. Please contact support.")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        if request.user.is_superuser:
            return redirect('/admin-dashboard')  # Redirect to admin login if superuser
        else:
            return redirect('/user-dashboard')

    context = {"title": "Login"}
    return render(request,'greeting/sign-in.html', context)



def dashboard(request):
    return render(request,'greeting/dashboard.html')

def billing(request):
    return render(request,'greeting/billing.html')

def generate_greeting(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        clients = Client.objects.all()
        festivals = Festival.objects.all()
        # Serialize the QuerySets into JSON format for use in JavaScript
        clients_json = serialize('json', clients)
        festivals_json = serialize('json', festivals)
        if request.method == 'POST':
            client_id = request.POST.get("client_id")
            occasion_id = request.POST.get("occasion_id")
            query_params = {'client_id': client_id, 'occasion_id': occasion_id}
            return redirect(f"/greeting-templates/?client_id={query_params['client_id']}&occasion_id={query_params['occasion_id']}")
        context = {
            "title": "Generate Greeting",
            'clients_json': clients_json,
            'festivals_json': festivals_json,
            'clients': clients,
            'festivals': festivals
        }
        return render(request,'greeting/user/generate-greeting.html', context)
    else:
        return redirect('/')

def user_dashboard(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        breadcrumb_items = [
            {'name': 'Dashboard', 'url': '/', 'active': False},
        ]
        context = {
            "title": "User Dashboard",
            'breadcrumb_items': breadcrumb_items
            }
        return render(request,'greeting/user/dashboard.html', context)
    else:
        return redirect('/')

def admin_dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        breadcrumb_items = [
            {'name': 'Dashboard', 'url': '/', 'active': False},
        ]
        context = {
            "title": "Admin Dashboard",
        'breadcrumb_items': breadcrumb_items,
        }
        return render(request,'greeting/admin/dashboard.html', context)
    else:
        return redirect('/')

def admin_clients(request):
    if request.user.is_authenticated and request.user.is_superuser:
        clients = Client.objects.all()       # fetch all records.
        print(clients) 
        breadcrumb_items = [
            {'name': 'Dashboard', 'url': '/', 'active': False},
            {'name': 'Clients', 'url': '/clients/', 'active': True},
        ]
        context = {
            "title": "Clients",
            'clients': clients,
        'breadcrumb_items': breadcrumb_items,
        }
        return render(request,'greeting/admin/clients.html' , context)
    else:
        return redirect('/')

def admin_occasions(request):
    if request.user.is_authenticated and request.user.is_superuser:
        festivals = Festival.objects.all()    # Fetch all festival records
        if request.method == 'POST':
            form = FestivalForm(request.POST)
            if form.is_valid():
                form.save()  # Save the new festival to the database
                messages.success(request, "Festival added successfully!")
                return redirect('/occasions')  # Redirect to the same page to see the new record
        else:
            form = FestivalForm()  # Initialize an empty form for GET requests
        print(festivals)
        breadcrumb_items = [
            {'name': 'Dashboard', 'url': '/', 'active': False},
            {'name': 'Occasions', 'url': '/occasions/', 'active': True},
        ]
        context = {
            "title": "Occasions",
            'festivals': festivals, 'form': form,
        'breadcrumb_items': breadcrumb_items,
        }
        return render(request,'greeting/admin/occasions.html', context)
    else:
        return redirect('/')



def add_new_client(request):

    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = ClientForm(request.POST, request.FILES)  # Get form data from the request
            print('Getting data')
            if form.is_valid():
                print('Data validate')
                form.save()  # Save the new client record to the database
                messages.success(request, "New client added successfully!")  # Show success message
                return redirect('/clients')  # Redirect to the clients page after saving
            else:
                print(form.errors) 
        else:
            form = ClientForm()  # Empty form for GET request
        breadcrumb_items = [
            {'name': 'Dashboard', 'url': '/', 'active': False},
            {'name': 'Clients', 'url': '/clients/', 'active': False},
            {'name': 'Add Client', 'url': '/add-client/', 'active': True},
        ]
        # Render the form in the template
        context = {
            "title": "Add Client",
            'form': form,
            'breadcrumb_items':breadcrumb_items
        }
        return render(request, 'greeting/admin/add_client.html', context)
    else:
        return redirect('/')



def card_view(request):
    return render(request, 'greeting/user/card.html')


def greeting_templates(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        # Get client_id and occasion_id from query parameters
        client_id = request.GET.get('client_id')
        occasion_id = request.GET.get('occasion_id')

        # Initialize client and occasion as None
        client = None
        occasion = None

        # Try to fetch the Client and Occasion from the database
        if client_id and occasion_id:
            client = Client.objects.filter(pk=client_id).first()
            occasion = Festival.objects.filter(pk=occasion_id).first()

        breadcrumb_items = [
            {'name': 'Dashboard', 'url': '/', 'active': False},
            {'name': 'Create Greeting', 'url': '/generate-greeting/', 'active': False},
            {'name': 'Greeting Templates', 'url': '/greeting-templates/', 'active': True},
        ]

        # Prepare context based on whether client and occasion were found
        if client and occasion:
            context = {
                'client': client,
                'occasion': occasion,
                'template': f"greeting/occasions/{occasion.name}/index.html" if occasion else ''   # Replace this with actual template or data you want to show
            }
        else:
            context = {
                'message': "No client or occasion found"
            }
        context['breadcrumb_items'] = breadcrumb_items
        context['title'] = "Greeting Templates"
        return render(request, 'greeting/user/greeting_templates.html', context)
    else:
        return redirect('/')

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('/') 