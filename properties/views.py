# properties/views.py

# ... (all code before the return statement)

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
    
    return JsonResponse(data, safe=False)
    
