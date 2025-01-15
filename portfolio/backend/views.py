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
            {'name': "Nature Shoot", 'description': "Explore the beauty of nature through stunning shots of landscapes, wildlife, and natural wonders."},
            {'name': "Studio Shoot", 'description': "Professional portraits, headshots, and family photos in our studio."},
            {'name': "Wedding Shoot", 'description': "Timeless wedding photos that capture the joy of your special day."},
            {'name': "Product Shoot", 'description': "High-quality images that showcase your products' features."},
            {'name': "Fashion Shoot", 'description': "Creative and vibrant fashion photography."},
            {'name': "Sports Shoot", 'description': "Dynamic, high-energy shots of sports moments."},
        ],
        'portfolio': [
            {'title': "Nature Project 1", 'image': "images/nature1.png", 'description': "Description of nature project 1."},
            {'title': "Nature Project 2", 'image': "images/nature2.png", 'description': "Description of nature project 2."},
            {'title': "Nature Project 3", 'image': "images/nature3.png", 'description': "Description of nature project 3."},
            {'title': "Wedding Project 1", 'image': "images/wedding1.png", 'description': "Description of wedding project 1."},
            {'title': "Wedding Project 2", 'image': "images/wedding2.png", 'description': "Description of wedding project 2."},
            {'title': "Wedding Project 3", 'image': "images/wedding3.png", 'description': "Description of wedding project 3."},
            {'title': "Fashion Project 1", 'image': "images/fashion1.png", 'description': "Description of fashion project 1."},
            {'title': "Sports Project 1", 'image': "images/sports1.png", 'description': "Description of sports project 1."},
        ],
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
