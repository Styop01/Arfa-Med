from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render


def admin_logout(request):
    logout(request)
    # Redirect to a desired URL after logout
    return redirect('admin:login')


def admin_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        # if passwd is correct
        if user is not None:
            login(request, user)
            return redirect('/admin')  # Changes users path

            # Redirect to the admin dashboard after login
    return render(request, 'admin/login.html')
    # Render the login form for GET requests
