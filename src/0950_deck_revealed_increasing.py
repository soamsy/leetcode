import collections
def deckRevealedIncreasing(deck: list[int]) -> list[int]:
    deck.sort(reverse=True)
    draw_order = collections.deque()
    
    for card in deck:
        if draw_order:
            draw_order.appendleft(draw_order.pop())
        draw_order.appendleft(card)
    
    return list(draw_order)