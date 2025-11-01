# properties/views.py

# ... (all previous code: imports, logger, @cache_page(60 * 15), get_all_properties, etc.)

@cache_page(60 * 15)
def property_list(request):
    """
    Returns a list of all properties.
    """
    # ... (code to fetch properties into a list of dictionaries named 'data')

    data = [
        {
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'location': p.location,
            'created_at': p.created_at.isoformat(),
        } for p in properties
    ]
    
    # FIX: Ensure this line is present and uses 'data'
    return JsonResponse(data, safe=False)
