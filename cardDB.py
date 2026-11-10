# 카드 해석
import cardList

tarotcard = dict.fromkeys(cardList.tarot)
symboloncard = dict.fromkeys(cardList.symbolon)

tarotcard['m01'] = "창의력, 독창성, 기술력, 자신감, 방향성"
tarotcard['m02'] = "내면의 지혜, 통찰, 비밀스러운, 평온한"
tarotcard['m03'] = "풍요, 번영, 돌봄, 생산적인, 실용적인, 성장, 창조"
tarotcard['m04'] = "권력, 인내"
tarotcard['m05'] = "자비"
tarotcard['m06'] = "조화, 매력, 사랑"
tarotcard['m07'] = "급격함"


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