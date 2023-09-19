from konlpy.tag import Kkma
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import re

# 한글 텍스트 파일 읽기
with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 텍스트 데이터 전처리: 숫자 및 특수 문자 제거
text = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', text)

# 형태소 분석기 초기화
kkma = Kkma()

# 명사 추출
nouns = kkma.nouns(text)

# 제외할 단어 리스트
exclude_words = ['내', '우리', '작년', '가지', '그룹', '천억', '억']

# 제외할 단어 제거
filtered_nouns = [noun for noun in nouns if noun not in exclude_words]

# 공백으로 구분된 명사들을 하나의 문자열로 결합
processed_text = ' '.join(filtered_nouns)

# 신한 로고 이미지 로드
logo_mask = np.array(Image.open('test.png'))

# 워드클라우드 생성
wordcloud = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', background_color='white', mask=logo_mask, width=1000, height=1000, max_words=100, max_font_size=300).generate(processed_text)

# 워드클라우드 이미지 출력
plt.figure(figsize=(8, 8), dpi=300)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()