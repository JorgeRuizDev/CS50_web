
from .models import Item
from .models import Bid
from typing import List

def asign_max_bid(listings: List[Item]):

    for listing in listings:
        bids = Bid.objects.filter(item=listing.id)
        max_bid: int = 0

        for bid in bids:
            if bid.ammount > max_bid:
                max_bid = bid.ammount

        if max_bid > 0:
            listing.min_bid = max_bid

