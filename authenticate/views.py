from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientPrimaryUserForm, ClientTeamMemberForm, ProjectManagerForm, ArtistForm
from django.contrib.auth import authenticate, login

# Create your views here.


def login_user(request):
    print(request)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page or homepage
                    return redirect('home')  # Change 'home' to your desired URL name
                else:
                    # Inactive user account
                    messages.error(request, 'Your account is inactive.')
            else:
                # Authentication failed
                messages.error(request, 'Invalid email or password.')
        except Exception as e:
            # Handle any unexpected errors during authentication
            messages.error(request, 'An error occurred during authentication.')
            # Log the error for debugging purposes
            print(f'Authentication error: {e}')
        # Render the login form
    return render(request, 'authenticate/login.html')


def sign_up(request):
    try:
        if request.method == 'POST':
            form = ClientPrimaryUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Client Primary User registered successfully.')
                return redirect('success_page')
            else:
                messages.error(request, 'Error registering Client Primary User. Please correct the errors below.')
        else:
            form = ClientPrimaryUserForm()
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'authenticate/sign-up.html', {'form': form})


def register_client_primary_user(request):
    try:
        if request.method == 'POST':
            form = ClientPrimaryUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Client Primary User registered successfully.')
                return redirect('success_page')
            else:
                messages.error(request, 'Error registering Client Primary User. Please correct the errors below.')
        else:
            form = ClientPrimaryUserForm()
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'registration/register_client_primary_user.html', {'form': form})


def register_client_team_member(request):
    try:
        if request.method == 'POST':
            form = ClientTeamMemberForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Client Team Member registered successfully.')
                return redirect('success_page')
            else:
                messages.error(request, 'Error registering Client Team Member. Please correct the errors below.')
        else:
            form = ClientTeamMemberForm()
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'registration/register_client_team_member.html', {'form': form})


def register_project_manager(request):
    try:
        if request.method == 'POST':
            form = ProjectManagerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Project Manager registered successfully.')
                return redirect('success_page')
            else:
                messages.error(request, 'Error registering Project Manager. Please correct the errors below.')
        else:
            form = ProjectManagerForm()
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'registration/register_project_manager.html', {'form': form})


def register_artist(request):
    try:
        if request.method == 'POST':
            form = ArtistForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Artist registered successfully.')
                return redirect('success_page')
            else:
                messages.error(request, 'Error registering Artist. Please correct the errors below.')
        else:
            form = ArtistForm()
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'registration/register_artist.html', {'form': form})
