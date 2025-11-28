
# Triangle classifier and drawer (TDD)

프로젝트 목표: 세 개의 숫자를 입력받아 삼각형 종류를 판별하고, 해당 삼각형의 모양을 그래픽으로 출력한다. 모든 개발은 TDD로 진행됩니다.

설치:

```bash
python -m pip install -r requirements.txt
```

유닛 테스트 실행:

```bash
python -m pytest -q
```

커버리지 실행 및 리포트:

```bash
python -m coverage run -m pytest
python -m coverage report -m
```

간단한 사용 예시 (인터프리터에서):

```python
>>> from triangle import classify_triangle, draw_triangle
>>> classify_triangle(3,4,5)
"scalene"
>>> fig = draw_triangle(3,4,5)
>>> fig.savefig('example_triangle.png')
```

또는 커맨드라인에서 빠르게 확인하려면:

```bash
python - <<'PY'
from triangle import classify_triangle, draw_triangle
print(classify_triangle(5,5,5))
draw_triangle(3,4,5, output_path='triangle.png')
PY
```

CI: `.github/workflows/ci.yml` 파일이 포함되어 있어 GitHub Actions에서 테스트와 커버리지를 실행합니다.

---

## 프로젝트 구조

- `triangle/` - 패키지 소스 코드
	- `triangle/triangle.py` - 삼각형 분류기 (`classify_triangle`)
	- `triangle/draw.py` - 삼각형 그림 생성기 (`draw_triangle`)
- `tests/` - 단위 테스트
- `requirements.txt` - 개발 및 테스트 의존성
- `.github/workflows/ci.yml` - GitHub Actions 워크플로

## 함수 시그니처
- `classify_triangle(a, b, c)`
	- 반환값: `'equilateral'`, `'isosceles'`, `'scalene'`
	- 예외: `ValueError` (영 또는 음수, 삼각형이 아닌 경우, 숫자가 아닌 입력)

- `draw_triangle(a, b, c, output_path=None)`
	- 반환값: `matplotlib.figure.Figure`
	- 동작: `output_path`가 주어지면 PNG 형식으로 파일 저장
	- 예외: `ValueError` (유효하지 않은 변 길이)

## 개발 가이드라인
- 모든 변경은 TDD로 진행하였습니다: 먼저 실패하는 테스트를 작성하고 구현을 추가해 통과시켰습니다.
- 공개 함수의 라인 수 및 순환 복잡도 제한을 지켰습니다(함수당 50행 이하, 복잡도 10 이하).

## 로컬에서 빠르게 실행하기

의존성 설치:

```bash
python -m pip install -r requirements.txt
```

테스트와 커버리지 실행:

```bash
python -m coverage run -m pytest
python -m coverage report -m
```

간단한 사용 예시(스크립트):

```bash
python - <<'PY'
from triangle import classify_triangle, draw_triangle
print('Triangle type:', classify_triangle(3,4,5))
draw_triangle(3,4,5, output_path='triangle.png')
print('Saved triangle.png')
PY
```

---
