from prometheus_client import Counter

bookings_created_total = Counter(
    'bookings_created_total',
    'Total number of bookings created'
)
