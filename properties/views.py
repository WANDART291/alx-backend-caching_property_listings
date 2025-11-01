# properties/views.py
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .utils import get_all_properties # or .models import Property if you haven't done Task 2 yet
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

@cache_page(60 * 15) 
def property_list(request):
    """
    Returns a list of all properties.
    """
    # Use the low-level cached function (assuming you implemented Task 2)
    properties = get_all_properties()

    # ... (rest of the view logic)
    data = [
        # ... (property data processing)
    ]
    
    logger.info("View layer (Task 1) executed.")
    return JsonResponse(data, safe=False)
