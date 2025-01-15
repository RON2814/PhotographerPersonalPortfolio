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
            {'title': "Nature Project 1", 'image': "nature1.png", 'description': "Description of nature project 1."},
            {'title': "Nature Project 2", 'image': "nature2.png", 'description': "Description of nature project 2."},
            {'title': "Nature Project 3", 'image': "nature3.png", 'description': "Description of nature project 3."},
            {'title': "Nature Project 4", 'image': "nature4.png", 'description': "Description of nature project 4."},
            {'title': "Nature Project 5", 'image': "nature5.png", 'description': "Description of nature project 5."},
            {'title': "Nature Project 6", 'image': "wedding1.png", 'description': "Description of nature project 1."},
            {'title': "Nature Project 7", 'image': "wedding2.png", 'description': "Description of nature project 2."},
            {'title': "Nature Project 8", 'image': "wedding3.png", 'description': "Description of nature project 3."},
            {'title': "Nature Project 9", 'image': "wedding4.png", 'description': "Description of nature project 4."},
            {'title': "Nature Project 10", 'image': "wedding5.png", 'description': "Description of nature project 5."},
            {'title': "Project B", 'image': "project_b.jpg", 'description': "Description of Project B."},
            {'title': "Project C", 'image': "project_c.jpg", 'description': "Description of Project C."},
        ],
        'contact_us': "Feel free to reach out to us via the contact form or email us at contact@example.com.",
    }
    return render(request, 'landing_page.html', context)