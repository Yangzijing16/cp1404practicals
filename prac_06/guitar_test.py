"""
Test program for Guitar class.
Estimated time: 15 minutes
Actual start time: 03:02 PM, July 06, 2025
Actual end time: 03:20 PM
"""

from guitar import Guitar

# Test guitars
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 1512.90)

# Test get_age
print(f"Gibson L-5 CES get_age() - Expected 103. Got {guitar1.get_age()}")
print(f"Another Guitar get_age() - Expected 12. Got {guitar2.get_age()}")

# Test is_vintage
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {guitar2.is_vintage()}")