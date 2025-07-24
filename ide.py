import streamlit as st
import streamlit.components.v1 as components
import contextlib
import io

st.set_page_config(page_title="🧠 파이썬 IDE", layout="wide")

st.markdown("""
    <h1 style="text-align:center; color:#00ffd5;">🧠 파이썬 IDE</h1>
    <p style="text-align:center; color:#aaa;">줄 번호 + 자동 들여쓰기 포함</p>
""", unsafe_allow_html=True)



# 대체 입력창 (실행용)
code = st.text_area("✏️ 실행할 코드를 입력하세요", height=300)

# 실행
if st.button("▶ 실행"):
    with contextlib.redirect_stdout(io.StringIO()) as f:
        try:
            exec(code, {})
            output = f.getvalue()
            st.success("✅ 실행 완료")
            st.code(output if output else "출력 없음")
        except Exception as e:
            st.error(f"❌ 오류 발생:\n\n{e}")
