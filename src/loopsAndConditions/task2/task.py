from __future__ import annotations


def task(bookings: list[list[int]], targetCount: int):
    targetSeats = '0' * targetCount
    for index in range(len(bookings)):
        booking = bookings[index]
        bookingString = ''.join(str(item) for item in booking)
        if targetSeats in bookingString:
            return index

    return False
