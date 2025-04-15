# 의존성

---

## 1_dependency_origin_check

- pip 기반 프로젝트 준비

</br>

- pipdeptree

  - 설치:
    - pip install pipdeptree
  - 실행:
    - pipdeptree

</br>

- pip freeze

  - 실행:
    - pip freeze > `origin_requirements.txt`
  - 파일 이동:
    - `dependency(dukim)/1_dependency_origin_check/origin_requirements.txt`

---

## 2_dependency_recipes

- 실행:
  - create_recipe_files.py
- input:
  - `dependency(dukim)/1_dependency_origin_check/origin_requirements.txt`
- output:
  - `recipes`

---

## 3_dependency_forge

- 실행:
  - convert_to_forge.py
- input:
  - `dependency(dukim)/1_dependency_origin_check/origin_requirements.txt`
- output:
  - `터미널 문자열 확인`
- 실행
  - 터미널에서 `forge` 명령어 실행

---

## 4_dependency_dist_check

- 실행:
  - dependency_dist_check.py
- input:
  - `dist`
- output:
  - `dependency_dist_check.txt`

---

## 비교

- left: 1_dependency_origin_check/origin_requirements.txt
- right: 4_dependency_dist_check/dependency_dist_check.txt
