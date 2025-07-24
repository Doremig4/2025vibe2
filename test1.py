import streamlit as st
from PIL import Image
import random

# 관상 예측 (모의)
def predict_face_reading(image):
    face_shapes = ['계란형', '둥근형', '각진형', '긴형']
    eye_types = ['맑고 또렷한 눈', '부드러운 눈매', '예리한 눈빛']
    mouth_types = ['입꼬리가 올라감', '입꼬리가 내려감', '평평한 입모양']
    overall = ['총명하고 침착한 인상', '활기차고 긍정적인 인상', '차분하고 신중한 인상', '결단력 있는 인상']

    result = {
        '얼굴형': random.choice(face_shapes),
        '눈매': random.choice(eye_types),
        '입모양': random.choice(mouth_types),
        '전체 인상': random.choice(overall)
    }
    return result

# Streamlit 앱 시작
st.set_page_config(page_title="관상 예측기", page_icon="📷", layout="centered")
st.title("📷 얼굴 사진으로 관상 예측하기")
st.markdown("사진을 업로드하면 얼굴을 분석하여 관상을 예측해드립니다.")

# 이미지 업로드
uploaded_file = st.file_uploader("얼굴 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 사진", use_container_width=True)  # ← 여기 수정됨

    if st.button("관상 예측하기"):
        with st.spinner("관상 분석 중..."):
            result = predict_face_reading(image)

        st.success("분석 완료! 아래 결과를 확인하세요:")
        st.markdown("---")
        st.subheader("🔍 관상 분석 결과")
        for key, value in result.items():
            st.write(f"**{key}**: {value}")
        st.markdown("---")
        st.info("※ 이 결과는 재미로 보세요. 실제 운세나 인생을 판단하는 데 사용하지 마세요 😊")

else:
    st.warning("먼저 얼굴 사진을 업로드해주세요.")
