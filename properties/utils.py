# properties/utils.py
from django.core.cache import cache
from .models import Property
import logging

# Required for Task 4
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

# --- Task 2: Low-Level Queryset Caching ---

def get_all_properties():
    """
    Fetches all Property objects, caching the queryset results in Redis for 1 hour (3600s).
    Cache Key: 'all_properties'
    """
    cache_key = 'all_properties'
    cache_timeout = 3600  # 1 hour

    # 1. Check Redis for the cached data
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        logger.info(f"CACHE HIT: Low-Level cache for '{cache_key}' was used.")
        return cached_data
    
    # 2. Cache Miss - Fetch from the database
    logger.info(f"CACHE MISS: Low-Level cache for '{cache_key}' not found. Hitting the database...")
    
    # Fetch from DB and immediately convert to a list to store the data
    properties = list(Property.objects.all().order_by('-created_at')) 
    
    # 3. Store the data in Redis
    cache.set(cache_key, properties, cache_timeout)
    logger.info(f"Stored {len(properties)} properties into low-level cache key '{cache_key}'.")
    
    return properties


# --- Task 4: Cache Metrics Analysis ---

def get_redis_cache_metrics():
    """
    Retrieves, calculates, and logs Redis cache hit/miss ratio using the default connection.
    """
    try:
        # Get the underlying Redis connection using django-redis utility
        conn = get_redis_connection("default")
        
        # Get general INFO dictionary from Redis, which contains keyspace stats
        stats = conn.info()

        # Extract hit and miss counts
        keyspace_hits = stats.get('keyspace_hits', 0)
        keyspace_misses = stats.get('keyspace_misses', 0)

        total_lookups = keyspace_hits + keyspace_misses
        
        # Calculate hit ratio
        hit_ratio_percent = 0.0
        if total_lookups > 0:
            hit_ratio_percent = (keyspace_hits / total_lookups) * 100

        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'total_lookups': total_lookups,
            'hit_ratio_percent': round(hit_ratio_percent, 2),
        }

        # Log the metrics for analysis
        logger.info("-" * 40)
        logger.info("🔥 Redis Cache Metrics Analysis 🔥")
        logger.info(f"Keyspace Hits: {metrics['keyspace_hits']}")
        logger.info(f"Keyspace Misses: {metrics['keyspace_misses']}")
        logger.info(f"Hit Ratio: {metrics['hit_ratio_percent']}%")
        logger.info("-" * 40)
        
        return metrics

    except Exception as e:
        logger.error(f"Error connecting to Redis or getting metrics: {e}. Ensure your local Redis server is running!")
        return {'error': str(e)}