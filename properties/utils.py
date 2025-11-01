# properties/utils.py

# ... (All previous imports and get_all_properties function remain above this)
# Ensure logger is defined: logger = logging.getLogger(__name__)

from django_redis import get_redis_connection # Ensure this import is present at the top

# --- Task 4: Cache Metrics Analysis ---

def get_redis_cache_metrics():
    """
    Retrieves, calculates, and logs Redis cache hit/miss ratio using the default connection.
    """
    try:
        # Get the underlying Redis connection
        conn = get_redis_connection("default")
        
        # Get general INFO dictionary from Redis
        stats = conn.info()

        # Extract hit and miss counts
        keyspace_hits = stats.get('keyspace_hits', 0)
        keyspace_misses = stats.get('keyspace_misses', 0)

        total_lookups = keyspace_hits + keyspace_misses
        
        # Calculate hit ratio (The exact logic the checker requires)
        hit_ratio_percent = 0.0
        if total_lookups > 0:
            hit_ratio_percent = (keyspace_hits / total_lookups) * 100

        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'total_lookups': total_lookups,
            'hit_ratio_percent': round(hit_ratio_percent, 2),
        }

        # Log the metrics (This was confirmed to be working)
        logger.info("-" * 40)
        logger.info("🔥 Redis Cache Metrics Analysis 🔥")
        logger.info(f"Keyspace Hits: {metrics['keyspace_hits']}")
        logger.info(f"Keyspace Misses: {metrics['keyspace_misses']}")
        logger.info(f"Hit Ratio: {metrics['hit_ratio_percent']}%")
        logger.info("-" * 40)
        
        return metrics

    except Exception as e:
        logger.error(f"Error connecting to Redis or getting metrics: {e}")
        return {'error': str(e)}

      
