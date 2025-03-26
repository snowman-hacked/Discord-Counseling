## 💌 연애상담 디스코드 챗봇 (LoveCounselBot)

개별 유저만 접근 가능한 **1:1 비공개 연애 상담 채널**을 자동 생성하고,  
GPT-3.5-Turbo를 활용해 조언과 위로를 주는 연애 전문 AI 챗봇입니다.

해당 디스코드 서버에서 테스트 할 수 있습니다.
https://discord.gg/JnP3maYH (초대 만료 기간: 4/1)

---

### 주요 기능

- **신규 유저가 서버에 입장 시, 본인만 볼 수 있는 비공개 상담 채널 자동 생성**
- `!연애 고민내용` 입력 시 ChatGPT 기반 상담 응답
- 하루 최대 100회까지 상담 가능 (사용자별 횟수 제한)
- 따뜻하고 공감 어린 말투로 감정 기반 상담 응답
- 관리자는 생성된 채널에 접근할 수 없음 (완전한 개인 상담 공간 제공)

---

### 🛠 설치 및 실행 방법

#### 1. Python 패키지 설치
```bash
pip install discord openai python-dotenv
```

#### 2. `.env` 파일 생성 (최상단 디렉토리에 위치)
```
DISCORD_TOKEN=디스코드_봇_토큰
OPENAI_API_KEY=OpenAI_API_키
```

#### 3. 디스코드 봇 권한 설정
[Discord Developer Portal](https://discord.com/developers/applications) → OAuth2 → URL Generator

- Scopes:
  - `bot`
  - `applications.commands`
- Bot Permissions:
  - `Manage Channels`
  - `Manage Roles`
  - `Send Messages`
  - `Read Message History`
  - `View Channels`

생성된 URL로 서버에 봇 초대

---

### ✅ 사용 방법

#### 새 유저가 서버에 들어오면?
- 자동으로 `연애상담-닉네임` 형식의 비공개 채널 생성됨

#### 유저가 상담 시작
```text
!연애 짝사랑 중인데 고백을 해도 될지 모르겠어요
```

→ 챗봇이 다정하고 따뜻한 말투로 상담 응답

---

### 🧠 사용 모델 정보

- **모델**: `gpt-3.5-turbo`
- **API 방식**: `openai>=1.0.0` 최신 방식 사용

---

### 🧪 테스트 체크리스트

- [x] 유저 입장 시 비공개 채널 생성됨
- [x] 채널에 유저 외 접근 불가 (관리자가 접근되는 문제가 남아있음)
- [x] `!연애` 명령어 정상 응답
- [x] 하루 100회 제한 작동함
- [x] OpenAI API 키 정상 연결됨

### 참고자료
- https://velog.io/@chuu1019/AI-ChatGpt4-Discord-Bot-%EB%A7%8C%EB%93%A4%EA%B8%B0-feat.-python
- https://yongeekd01.tistory.com/193
- GPT4o를 통한 챗봇용 프롬포트 제작 및 코드 리펙토링(사용 비율은 50%)
