# app.py

import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="인터랙티브 바람개비",
    page_icon="🎡",
    layout="wide"
)

# Streamlit 앱 제목
st.title("🎡 인터랙티브 바람개비 앱")
st.write("버튼을 클릭하거나 바람개비를 직접 클릭하여 돌려보세요!")

# 제공된 HTML, CSS, JavaScript 코드를 그대로 문자열로 저장
pinwheel_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인터랙티브 바람개비</title>
    <style>
        /* 기본 페이지 스타일 */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f0f8ff; /* 하늘색 배경 */
            font-family: 'Malgun Gothic', sans-serif;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
        }

        /* 메인 컨테이너 (미리보기 + 앱) */
        .main-container {
            display: flex;
            flex-wrap: wrap; /* 화면이 작아지면 줄바꿈 */
            gap: 40px;
            justify-content: center;
            align-items: flex-start;
        }
        
        /* 각 섹션의 컨테이너 */
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        h2 {
            margin-top: 0;
            color: #333;
        }

        /* 바람개비 컨테이너 */
        .pinwheel-container {
            position: relative;
            width: 200px;
            height: 200px;
            margin: 20px auto;
            /* 버튼으로 회전 시 부드러운 전환 효과 */
            transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
        }

        /* 인터랙티브 바람개비에만 커서 포인터 적용 */
        #interactive-pinwheel-section .pinwheel-container {
            cursor: pointer;
        }

        /* 바람개비 날개 */
        .blade {
            position: absolute;
            width: 100px;
            height: 100px;
            transform-origin: 100% 100%; /* 회전축을 오른쪽 아래로 설정 */
            clip-path: polygon(0 0, 100% 0, 100% 100%); /* 삼각형 모양으로 자르기 */
            border: 1px solid rgba(0,0,0,0.2);
        }

        .blade1 { background-color: #ff4d4d; transform: rotate(0deg); } /* 빨강 */
        .blade2 { background-color: #ffff66; transform: rotate(90deg); } /* 노랑 */
        .blade3 { background-color: #4d4dff; transform: rotate(180deg); } /* 파랑 */
        .blade4 { background-color: #cc66cc; transform: rotate(270deg); } /* 보라 */
        
        /* 바람개비 중앙 핀 */
        .pin {
            width: 24px;
            height: 24px;
            background: #444;
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%); /* 정확한 중앙 정렬 */
            z-index: 1;
            border: 2px solid white;
            box-shadow: 0 0 5px rgba(0,0,0,0.3);
        }

        /* 클릭 시 연속 회전 애니메이션 */
        .spin {
            animation: spin-animation 2s linear infinite;
        }

        @keyframes spin-animation {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        /* 컨트롤 버튼 영역 */
        .controls {
            margin-top: 20px;
        }

        .controls h3 {
            margin: 20px 0 10px 0;
            color: #555;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }

        .button-group {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
        }

        button {
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 8px;
            background-color: #007bff;
            color: white;
            transition: background-color 0.3s, transform 0.1s;
            min-width: 80px;
        }
        
        button.reset-button {
             background-color: #28a745; /* 초록색 */
        }

        button:hover {
            background-color: #0056b3;
            transform: translateY(-2px); /* 살짝 위로 이동 */
        }

        button.reset-button:hover {
            background-color: #218838;
        }
        
    </style>
</head>
<body>

<div class="main-container">

    <div class="container">
        <h2>처음 모양</h2>
        <div class="pinwheel-container">
            <div class="blade blade1"></div>
            <div class="blade blade2"></div>
            <div class="blade blade3"></div>
            <div class="blade blade4"></div>
            <div class="pin"></div>
        </div>
    </div>

    <div id="interactive-pinwheel-section" class="container">
        <h2>바람개비 돌리기</h2>
        <div class="pinwheel-container" id="pinwheel">
            <div class="blade blade1"></div>
            <div class="blade blade2"></div>
            <div class="blade blade3"></div>
            <div class="blade blade4"></div>
            <div class="pin"></div>
        </div>

        <div class="controls">
            <button class="reset-button" onclick="resetRotation()">처음 모양으로</button>
            <h3>시계 방향 (CW)</h3>
            <div class="button-group">
                <button onclick="rotateBy(90)">90°</button>
                <button onclick="rotateBy(180)">180°</button>
                <button onclick="rotateBy(270)">270°</button>
                <button onclick="rotateBy(360)">360°</button>
            </div>
            <h3>시계 반대 방향 (CCW)</h3>
            <div class="button-group">
                <button onclick="rotateBy(-90)">-90°</button>
                <button onclick="rotateBy(-180)">-180°</button>
                <button onclick="rotateBy(-270)">-270°</button>
                <button onclick="rotateBy(-360)">-360°</button>
            </div>
        </div>
    </div>
</div>

<script>
    // JS 요소 가져오기
    const pinwheel = document.getElementById('pinwheel');
    let currentRotation = 0; // 현재 회전 각도를 저장하는 변수

    // 바람개비 클릭 시 자동 회전 시작/정지
    pinwheel.addEventListener('click', () => {
        // 'spin' 클래스가 있으면 제거하고, 없으면 추가
        pinwheel.classList.toggle('spin');
        // 자동 회전 시작 시, transform 스타일을 초기화하여 애니메이션이 현재 위치부터 시작하도록 함
        if (pinwheel.classList.contains('spin')) {
            pinwheel.style.transform = `rotate(${currentRotation}deg)`;
        }
    });

    // 지정된 각도만큼 회전하는 함수
    function rotateBy(degrees) {
        // 자동 회전 중이었다면 멈춤
        if (pinwheel.classList.contains('spin')) {
            pinwheel.classList.remove('spin');
        }
        
        // 현재 각도에 새로운 각도를 더함
        currentRotation += degrees;
        // 바람개비의 transform 스타일을 직접 변경하여 회전
        pinwheel.style.transform = `rotate(${currentRotation}deg)`;
    }

    // 처음 모양으로 되돌리는 함수
    function resetRotation() {
        // 자동 회전 멈춤
        if (pinwheel.classList.contains('spin')) {
            pinwheel.classList.remove('spin');
        }
        // 회전 각도 초기화
        currentRotation = 0;
        // transform 스타일 초기화
        pinwheel.style.transform = 'rotate(0deg)';
    }
</script>

</body>
</html>
"""

# Streamlit 앱에 HTML 컴포넌트 삽입
# height를 700으로 설정하여 모든 콘텐츠가 잘리지 않도록 함
components.html(pinwheel_html, height=700, scrolling=True)
