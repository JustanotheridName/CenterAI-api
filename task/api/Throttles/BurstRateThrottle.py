from rest_framework.throttling import UserRateThrottle

class BurstRateThrottle(UserRateThrottle):
    rate = '20/minute'