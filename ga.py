import streamlit as st
import random

# 선택지
choices = ["가위", "바위", "보"]

# 결과 판별 함수
def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "win"
    else:
        return "lose"

# 앱 설정
st.set_page_config(page_title="가위바위보 & 묵찌빠", page_icon="✊", layout="centered")
st.title("✊ ✋ ✌ 가위바위보 & 묵찌빠 게임")

# 탭 생성
tab1, tab2 = st.tabs(["가위바위보", "묵찌빠"])

# 🎮 가위바위보 탭
with tab1:
    st.subheader("가위바위보 게임")
    st.markdown("당신의 선택은 무엇인가요? 버튼을 눌러 시작하세요!")

    col1, col2, col3 = st.columns(3)
    user_choice = None

    with col1:
        if st.button("✌ 가위", key="rps_scissors"):
            user_choice = "가위"
    with col2:
        if st.button("✊ 바위", key="rps_rock"):
            user_choice = "바위"
    with col3:
        if st.button("✋ 보", key="rps_paper"):
            user_choice = "보"

    if user_choice:
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)

        st.markdown("---")
        st.subheader("🎮 결과")
        st.write(f"당신의 선택: **{user_choice}**")
        st.write(f"컴퓨터의 선택: **{computer_choice}**")

        if result == "win":
            st.success("이겼어요! 🎉")
        elif result == "lose":
            st.error("졌어요 😢")
        else:
            st.info("비겼어요! 🤝")

# 🎮 묵찌빠 탭
with tab2:
    st.subheader("묵찌빠 게임")

    if "muk_phase" not in st.session_state:
        st.session_state.muk_phase = "start"
        st.session_state.attacker = None

    if st.session_state.muk_phase == "start":
        st.write("먼저 선공을 정하기 위한 가위바위보를 해주세요!")

        col1, col2, col3 = st.columns(3)
        starter_choice = None

        with col1:
            if st.button("✌ 가위", key="muk_start_scissors"):
                starter_choice = "가위"
        with col2:
            if st.button("✊ 바위", key="muk_start_rock"):
                starter_choice = "바위"
        with col3:
            if st.button("✋ 보", key="muk_start_paper"):
                starter_choice = "보"

        if starter_choice:
            computer_choice = random.choice(choices)
            result = determine_winner(starter_choice, computer_choice)

            st.write(f"당신: **{starter_choice}**")
            st.write(f"컴퓨터: **{computer_choice}**")

            if result == "win":
                st.success("당신이 선공입니다!")
                st.session_state.attacker = "user"
                st.session_state.muk_phase = "muk"
            elif result == "lose":
                st.error("컴퓨터가 선공입니다!")
                st.session_state.attacker = "computer"
                st.session_state.muk_phase = "muk"
            else:
                st.info("비겼습니다! 다시 시도하세요.")

    elif st.session_state.muk_phase == "muk":
        st.write(f"🎯 공격자: **{'당신' if st.session_state.attacker == 'user' else '컴퓨터'}**")
        st.write("묵찌빠 손을 선택하세요!")

        col1, col2, col3 = st.columns(3)
        muk_choice = None

        with col1:
            if st.button("✌ 가위", key="muk_play_scissors"):
                muk_choice = "가위"
        with col2:
            if st.button("✊ 바위", key="muk_play_rock"):
                muk_choice = "바위"
        with col3:
            if st.button("✋ 보", key="muk_play_paper"):
                muk_choice = "보"

        if muk_choice:
            computer_choice = random.choice(choices)
            st.write(f"당신: **{muk_choice}**")
            st.write(f"컴퓨터: **{computer_choice}**")

            if muk_choice == computer_choice:
                winner = "당신" if st.session_state.attacker == "user" else "컴퓨터"
                st.success(f"{winner}의 승리! 🎉")
                st.session_state.muk_phase = "start"
            else:
                new_attacker = None
                result = determine_winner(muk_choice, computer_choice)
                if result == "win":
                    new_attacker = "user"
                elif result == "lose":
                    new_attacker = "computer"
                else:
                    new_attacker = st.session_state.attacker  # draw

                st.session_state.attacker = new_attacker
                st.info("게임 계속!")

    # 초기화 버튼
    if st.button("🔄 묵찌빠 초기화"):
        st.session_state.muk_phase = "start"
        st.session_state.attacker = None
