from django.shortcuts import render, get_object_or_404, redirect
from backend.models import PortfolioProject
from backend.forms import PortfolioProjectForm

# Create a project
def create_project(request):
    if request.method == 'POST':
        form = PortfolioProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = PortfolioProjectForm()
    return render(request, 'create_project.html', {'form': form})

# Read (list) projects
def project_list(request):
    projects = PortfolioProject.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

# Update a project
def update_project(request, pk):
    project = get_object_or_404(PortfolioProject, pk=pk)
    if request.method == 'POST':
        form = PortfolioProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = PortfolioProjectForm(instance=project)
    return render(request, 'update_project.html', {'form': form})

# Delete a project
def delete_project(request, pk):
    project = get_object_or_404(PortfolioProject, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'delete_project.html', {'project': project})

# Landing page
def landing_page(request):
    # Fetch portfolio projects dynamically from the database
    portfolio_projects = PortfolioProject.objects.all()

    context = {
        'about_us': (
            "Aura Lens Studio is where life’s beauty meets the art of photography. "
            "We specialize in capturing life’s cherished moments and turning them into timeless works of art. "
            "From dreamy weddings and professional studio sessions to captivating product shots, breathtaking nature photography, "
            "high-fashion editorials, and dynamic sports captures, our expertise spans a wide range of styles. "
            "Looking for the perfect photographer for your next project? Let’s make it happen!"
        ),
        'services': [
            {'name': "Nature Shoot", 'description': "Explore the beauty of nature through stunning shots of landscapes, wildlife, and natural wonders."},
            {'name': "Studio Shoot", 'description': "Professional portraits, headshots, and family photos in our studio."},
            {'name': "Wedding Shoot", 'description': "Timeless wedding photos that capture the joy of your special day."},
            {'name': "Product Shoot", 'description': "High-quality images that showcase your products' features."},
            {'name': "Fashion Shoot", 'description': "Creative and vibrant fashion photography."},
            {'name': "Sports Shoot", 'description': "Dynamic, high-energy shots of sports moments."},
        ],
        # Use the dynamically fetched portfolio data
        'portfolio': portfolio_projects,
        'contact_us': (
            "Feel free to reach out to us via email, phone, or visit us at our studio."
        ),
        'contact_details': {
            'phone1': "+9617792345",
            'phone2': "+8909087933",
            'email': "auralens@gmail.com",
            'address': "Bacoor City, Molino 1 St. to Heaven #169",
            'social_media': {
                'facebook': "https://www.facebook.com",
                'linkedin': "https://www.linkedin.com",
                'youtube': "https://www.youtube.com",
                'instagram': "https://www.instagram.com",
            },
        },
    }
    return render(request, 'landing_page.html', context)
