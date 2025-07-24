import streamlit as st
import random

# 가위바위보 선택지
choices = ["가위", "바위", "보"]

# 결과 판별 함수
def determine_winner(user, computer):
    if user == computer:
        return "비겼어요! 🤝"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "이겼어요! 🎉"
    else:
        return "졌어요 😢"

# 앱 설정
st.set_page_config(page_title="가위바위보 게임", page_icon="✊", layout="centered")

# 타이틀
st.title("✊ ✋ ✌ 가위바위보 게임")
st.markdown("당신의 선택은 무엇인가요? 버튼을 눌러 시작하세요!")

# 사용자 선택
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("✌ 가위"):
        user_choice = "가위"
with col2:
    if st.button("✊ 바위"):
        user_choice = "바위"
with col3:
    if st.button("✋ 보"):
        user_choice = "보"

# 게임 실행
if user_choice:
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    st.markdown("---")
    st.subheader("🎮 게임 결과")
    st.write(f"당신의 선택: **{user_choice}**")
    st.write(f"컴퓨터의 선택: **{computer_choice}**")
    st.success(result)
