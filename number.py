import streamlit as st
import random

# 난이도에 따른 범위와 시도 횟수
difficulty_settings = {
    "쉬움 (1~10)": {"max": 10, "tries": 5},
    "보통 (1~50)": {"max": 50, "tries": 7},
    "어려움 (1~100)": {"max": 100, "tries": 10},
}

# 앱 초기 설정
st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🔢", layout="centered")
st.title("🔢 숫자 맞추기 게임")

# 난이도 선택
difficulty = st.selectbox("난이도를 선택하세요:", list(difficulty_settings.keys()))

max_number = difficulty_settings[difficulty]["max"]
max_tries = difficulty_settings[difficulty]["tries"]

# 세션 상태 초기화
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, max_number)
    st.session_state.tries_left = max_tries
    st.session_state.history = []

# 사용자 입력
guess = st.number_input(f"1부터 {max_number} 사이의 숫자를 입력하세요:", min_value=1, max_value=max_number, step=1)

# 제출 버튼
if st.button("확인"):
    if st.session_state.tries_left <= 0:
        st.warning("게임이 종료되었습니다. '다시 시작'을 눌러주세요.")
    else:
        if guess == st.session_state.answer:
            st.success(f"정답입니다! 🎉\n\n총 {max_tries - st.session_state.tries_left + 1}번 만에 맞췄어요!")
            st.session_state.tries_left = 0
        else:
            st.session_state.tries_left -= 1
            hint = "너무 작아요 🔻" if guess < st.session_state.answer else "너무 커요 🔺"
            st.session_state.history.append((guess, hint))
            if st.session_state.tries_left > 0:
                st.warning(f"{hint} (남은 시도: {st.session_state.tries_left})")
            else:
                st.error(f"😢 실패! 정답은 {st.session_state.answer}였습니다.")

# 시도 기록 표시
if st.session_state.history:
    st.markdown("### 📝 시도 기록")
    for i, (g, h) in enumerate(st.session_state.history, 1):
        st.write(f"{i}회차 👉 {g} → {h}")

# 다시 시작 버튼
if st.button("🔄 다시 시작"):
    st.session_state.answer = random.randint(1, max_number)
    st.session_state.tries_left = max_tries
    st.session_state.history = []
    st.success("게임이 초기화되었습니다! 다시 도전하세요 💪")
