"""
🧪 Food R&D Platform - 식품 연구개발 플랫폼
"""
import streamlit as st
import sys, os
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

st.set_page_config(page_title="Food R&D Platform", page_icon="🧪", layout="wide")

st.markdown("# 🧪 Food R&D Platform")
st.markdown("#### 식품 연구개발 통합 플랫폼")
st.markdown("---")

# 학생/연구원 이름
name = st.text_input("👤 이름 (저장 시 사용)", value=st.session_state.get("student_name", ""))
st.session_state.student_name = name

# 핵심 기능 5가지
st.markdown("### 🎯 핵심 기능")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("""
    **💰 원가 분석**
    - 원재료 단가 DB (36종)
    - 배합비 → 원가 자동계산
    - 원가 구성 시각화
    """)

with c2:
    st.markdown("""
    **⚗️ 배합비 설계**
    - 100% 기준 배합표
    - AI 자동 생성
    - CSV 직접 작성
    """)

with c3:
    st.markdown("""
    **🔀 표준배합비 비교**
    - 5종 표준배합비 내장
    - 내 배합 vs 표준 비교
    - 차이 분석 차트
    """)

with c4:
    st.markdown("""
    **🔬 AI 공정 분석**
    - PDF 업로드 학습
    - AI 연구원 분석
    - HACCP/CCP 검토
    """)

with c5:
    st.markdown("""
    **🏷️ 표시사항 검토**
    - 식품등의 표시기준 PDF 학습
    - 필수항목 적합성 비교표
    - AI 적합성 검토
    """)

st.markdown("---")

# 워크플로우
st.markdown("### 📐 R&D 워크플로우")
st.markdown("""
```
📈 매출 분석 → 🏷️ 브랜드 분석 → 🤖 AI 제품카드 생성
                                       ↓
                           ⚗️ 배합비 설계 (100% 기준)
                          ╱          |          ╲
                    💰 원가분석   🔀 표준비교   ✏️ 배합연습
                                     |
                           🏭 공정 설계 & 리스크
                                     |
                           🔬 AI 공정 분석 (PDF 학습)
                                     |
                           🏷️ 표시사항 검토 (표시기준 PDF)
                                     |
                           📋 규제 서류 & 품목제조보고
```
""")

# 전체 페이지 목록
st.markdown("---")
st.markdown("### 📂 전체 메뉴")

pages = [
    ("📈 매출추이", "매출 트렌드, 카테고리 순위, 성장률"),
    ("🏷️ 브랜드분석", "브랜드별 매출, 점유율, YoY 비교"),
    ("🤖 AI제품카드", "9종 제품 카드 → AI 배합비 자동 생성"),
    ("⚗️ 배합비설계", "100% 기준 배합표 + 표준배합비 비교 + 원가 연동"),
    ("🏭 공정리스크", "8단계 공정 흐름, HACCP CCP, 리스크 매트릭스"),
    ("📋 규제서류", "품목제조보고서, 식품안전나라 연계"),
    ("✏️ 배합연습", "CSV 작성 연습 + 검증 + 표준 비교 + 저장"),
    ("💰 원가분석", "원재료 단가 DB + 원가표 자동 계산"),
    ("🔬 AI공정분석", "PDF 학습 → AI 연구원 공정 리스크 분석"),
    ("🏷️ 표시사항", "식품등의 표시기준 PDF 학습 → 적합성 비교표"),
]

for i, (name, desc) in enumerate(pages, 1):
    st.markdown(f"**{i}. {name}** — {desc}")

st.markdown("---")
st.caption("← 사이드바에서 원하는 메뉴를 선택하세요")
st.caption("© 2025 Food R&D Platform | Powered by Streamlit + Claude AI")
