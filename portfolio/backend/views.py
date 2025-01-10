# from django.http import HttpResponse
from django.shortcuts import render

def landing_page(request):
    context = {
       'about_us': (
            "Aura Lens Studio is where life’s beauty meets the art of photography. "
            "We specialize in capturing life’s cherished moments and turning them into timeless works of art. "
            "From dreamy weddings and professional studio sessions to captivating product shots, breathtaking nature photography, "
            "high-fashion editorials, and dynamic sports captures, our expertise spans a wide range of styles. "
            "Looking for the perfect photographer for your next project? Let’s make it happen!"
        ),
        'services': [
            {'name': "Web Development", 'description': "Building responsive and functional websites."},
            {'name': "Mobile Apps", 'description': "Creating intuitive mobile applications."},
            {'name': "SEO", 'description': "Optimizing your site for better search rankings."},
        ],
        'portfolio': [
            {'title': "Project A", 'image': "project_a.jpg", 'description': "Description of Project A."},
            {'title': "Project B", 'image': "project_b.jpg", 'description': "Description of Project B."},
            {'title': "Project C", 'image': "project_c.jpg", 'description': "Description of Project C."},
        ],
        'contact_us': "Feel free to reach out to us via the contact form or email us at contact@example.com.",
    }
    return render(request, 'landing_page.html', context)