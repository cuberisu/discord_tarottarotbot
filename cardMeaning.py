# 카드 해석
import cardName

tarot_name = cardName.tarot_name
symbolon_name = cardName.symbolon_name

tarot_meaning = dict.fromkeys(tarot_name)
symbolon_meaning = dict.fromkeys(symbolon_name)

tarot_meaning['m01'] = "창의력, 독창성, 기술력, 자신감, 방향성"
tarot_meaning['m02'] = "내면의 지혜, 통찰, 비밀스러운, 평온한"
tarot_meaning['m03'] = "풍요, 번영, 돌봄, 생산적인, 실용적인, 성장, 창조"
tarot_meaning['m04'] = "권력, 인내"
tarot_meaning['m05'] = "자비"
tarot_meaning['m06'] = "조화, 매력, 사랑"
tarot_meaning['m07'] = "급격함"


# 유효성 검사
missing = [
    card_id
    for card_id, meaning in tarot_meaning.items()
    if meaning is None
]

print(f"전체 타로 카드: {len(tarot_name)}장")
print(f"해석 작성 완료: {len(tarot_name) - len(missing)}장")
print(f"해석 미작성: {len(missing)}장")