# properties/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

# The cache key to invalidate
CACHE_KEY = 'all_properties'

@receiver(post_save, sender=Property)
def invalidate_property_cache_on_save(sender, instance, created, **kwargs):
    """Deletes the 'all_properties' cache key on property create or update."""
    cache.delete(CACHE_KEY)
    action = "created" if created else "updated"
    logger.info(f"SIGNAL: Property '{instance.title}' {action}. Invalidating cache key: {CACHE_KEY}")

@receiver(post_delete, sender=Property)
def invalidate_property_cache_on_delete(sender, instance, **kwargs):
    """Deletes the 'all_properties' cache key on property deletion."""
    cache.delete(CACHE_KEY)
    logger.info(f"SIGNAL: Property '{instance.title}' deleted. Invalidating cache key: {CACHE_KEY}")