# 베이스 이미지
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# 필수 패키지 복사
COPY requirements.txt .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 앱 복사
COPY . .

# 장고 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
