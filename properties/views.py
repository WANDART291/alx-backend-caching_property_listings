# properties/views.py (Final update)
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .utils import get_all_properties, get_redis_cache_metrics # <-- IMPORT METRICS
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

# Task 1: View-level caching (Outer layer: 15 minutes)
@cache_page(900)
def property_list(request):
    """
    Returns a list of all properties using multi-level caching and logs metrics.
    """
    # Task 2: Use the low-level cached function
    properties = get_all_properties()

    # Task 4: Log cache metrics (must be called after get_all_properties to reflect latest hit/miss)
    metrics = get_redis_cache_metrics()

    data = [
        # ... (data processing remains the same)
        {
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'location': p.location,
            'created_at': p.created_at.isoformat(),
        } for p in properties
    ]
    
    logger.info("View layer (Task 1) executed.")
    # For testing, you can return metrics in the response:
    # return JsonResponse({'properties': data, 'metrics': metrics}, safe=False)
    return JsonResponse(data, safe=False)