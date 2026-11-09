# 카드 해석
import cardList

tarotcard = dict.fromkeys(cardList.tarot)
symboloncard = dict.fromkeys(cardList.symbolon)

tarotcard['m01'] = "창의성, 독창성, 기술력"


# 검증
missing = [
    card_id
    for card_id, meaning in tarotcard.items()
    if meaning is None
]

print("해석이 없는 카드:", missing)


unknown = set(tarotcard) - set(cardList.tarot)

if unknown:
    raise ValueError(f"잘못된 카드 ID: {unknown}")