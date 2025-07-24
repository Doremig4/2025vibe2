import streamlit as st
import streamlit.components.v1 as components
import contextlib
import io

st.set_page_config(page_title="🔥 Python IDE", layout="wide")

st.markdown("""
    <style>
    .editor {
        height: 400px;
        border: 2px solid #00ffd5;
        border-radius: 10px;
        overflow: hidden;
    }
    </style>

    <h1 style='text-align:center; color:#00ffd5;'>🔥 Python IDE</h1>
    <p style='text-align:center; color:#888;'>Streamlit + 힙한 다크 테마 코드 에디터</p>
""", unsafe_allow_html=True)

# 🎨 코드 입력 (심플하게)
default_code = '''# 예시 코드
for i in range(1, 6):
    print(f"{i}번째 출력")'''

code = st.text_area("✏️ 파이썬 코드를 작성하세요", value=default_code, height=300, label_visibility="collapsed")

# ▶️ 실행 버튼
if st.button("▶️ 실행"):
    with contextlib.redirect_stdout(io.StringIO()) as f:
        try:
            exec(code, {})
            output = f.getvalue()
            st.success("✅ 실행 완료")
            st.code(output if output else "출력 없음", language="text")
        except Exception as e:
            st.error(f"❌ 오류 발생:\n\n{e}")
