from django.shortcuts import render
from datetime import datetime

def index(request):
    # Example of dynamic content
    context = {
        'page_title': 'Welcome to ByteBros Smart System',
        'welcome_message': 'Empowering smarter business decisions.',
        'featured_products': [
            {'name': 'Smart Beer Monitor', 'price': 1200, 'available': True},
            {'name': 'Order Management Pro', 'price': 950, 'available': False},
            {'name': 'AI Profit Predictor', 'price': 1500, 'available': True},
        ],
        'announcements': [
            {'title': 'System Update', 'detail': 'New dashboard features added!'},
            {'title': 'Offer', 'detail': 'Get 10% off all smart tools this week!'},
        ],
        'today': datetime.now()
    }
    return render(request, 'home/index.html', context)
