# properties/views.py

# Ensure all imports are at the top (cache_page, JsonResponse, get_all_properties, get_redis_cache_metrics)
# ...

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
    
    # Ensuring the logger runs before the return
    logger.info("View layer executed.") 
    
    # THIS RETURN STATEMENT MUST BE THE FINAL LINE
    return JsonResponse(data, safe=False)
