import streamlit as st
from streamlit_chat import message

# 페이지 설정
st.set_page_config(page_title="채팅 데모", page_icon="💬", layout="centered")
st.title("💬 나와의 대화")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "content": "안녕하세요! 무엇이든 물어보세요 😊"}
    ]

# 채팅 출력
for msg in st.session_state.messages:
    message(msg["content"], is_user=(msg["role"] == "user"))

# 사용자 입력 받기
user_input = st.chat_input("메시지를 입력하세요...")

# 입력이 있을 경우
if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True)

    # 간단한 AI 응답 (모의)
    if "안녕" in user_input:
        ai_response = "안녕하세요! 반가워요 👋"
    elif "이름" in user_input:
        ai_response = "저는 당신의 AI 챗봇이에요."
    elif "잘가" in user_input:
        ai_response = "다음에 또 봐요! 👋"
    else:
        ai_response = "음... 그건 잘 모르겠어요. 다른 걸 물어보실래요?"

    # AI 응답 저장
    st.session_state.messages.append({"role": "ai", "content": ai_response})
    message(ai_response, is_user=False)
