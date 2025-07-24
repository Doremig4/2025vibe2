import streamlit as st
import streamlit.components.v1 as components
import contextlib
import io

st.set_page_config(page_title="🧠 파이썬 IDE", layout="wide")

st.markdown("""
    <h1 style="text-align:center; color:#00ffd5;">🧠 힙한 파이썬 IDE</h1>
    <p style="text-align:center; color:#aaa;">줄 번호 + 자동 들여쓰기 포함</p>
""", unsafe_allow_html=True)

# ▶ CodeMirror 에디터 삽입
components.html("""
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/codemirror.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.7/mode/python/python.min.js"></script>
    <style>
        .CodeMirror {
            border: 2px solid #00ffd5;
            border-radius: 8px;
            height: auto;
            font-size: 15px;
        }
    </style>
    <textarea id="code" name="code">
# 예시 코드
for i in range(5):
    print("Hello, Python!")
    </textarea>
    <script>
        var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
            mode: "python",
            lineNumbers: true,
            indentUnit: 4,
            smartIndent: true,
            theme: "default",
            lineWrapping: true,
            matchBrackets: true,
        });

        // Streamlit에 값 보낼 수 없으므로 텍스트 영역은 read-only
    </script>
""", height=400)

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
