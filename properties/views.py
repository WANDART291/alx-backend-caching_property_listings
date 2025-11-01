# properties/views.py
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties, get_redis_cache_metrics
from django.shortcuts import render # You may keep or remove this
import logging

logger = logging.getLogger(__name__)

# Task 1: Apply view-level caching using the required expression
@cache_page(60 * 15)
def property_list(request):
    """
    Returns a list of all properties using multi-level caching and logs metrics.
    """
    # Task 2: Use the low-level cached function
    properties = get_all_properties()

    # Task 4: Log cache metrics (must be called after get_all_properties)
    metrics = get_redis_cache_metrics()

    # Prepare data for JSON response
    data = [
        {
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'location': p.location,
            'created_at': p.created_at.isoformat(),
        } for p in properties
    ]
    
    logger.info("View layer executed.") 
    
    # Final return statement
    return JsonResponse(data, safe=False)
    
