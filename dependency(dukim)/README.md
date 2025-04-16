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

- 정렬
  - 실행:
    - `sort_origin_requirements.py`
  - input:
    - `dependency(dukim)/1_dependency_origin_check/origin_requirements.txt`
  - output:
    - `dependency(dukim)/1_dependency_origin_check/sort_origin_requirements.txt`

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

- left: dependency(dukim)/1_dependency_origin_check/sort_origin_requirements.txt
- right: dependency(dukim)/4_dependency_dist_check/dependency_dist_check.txt

## maturin 문제

- maturin (Rust로 작성된 Python 바인딩을 빌드하는데 사용되는 도구)
- [pyproject.toml](../pyproject.toml) 의존성 수정

  - 의존성 추가

    ```pyproject.toml
    ...
    "jsonschema == 4.23.0",
    "maturin >= 1.0.0, < 2.0.0",
    "packaging == 24.2",
    ...
    ```

- maturin 직접빌드

  - [src/forge/cross.py](../src/forge/cross.py) 수정
  - 코드영역 삭제 or 주석처리

    ```py
    # If we're doing a host build, require binary packages.
    # build environment can use non-binary packages.
    + (
        []
        if build
        else [
            "--only-binary",
            ":all:",
        ]
    )
    ```

- Rust Compiler 설치 & 환경설정

  ```bash
  # 설치
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

  # 환경설정 (or 터미널 재시작)
  source "$HOME/.cargo/env"

  # Rust가 올바르게 설치되었는지 확인
  rustc --version
  ```

## ⚠️ 아직

```text
aiohttp

package:
  name: aiohttp
  version: 3.11.14
===>
package:
  name: aiohttp
  version: 3.10.5

--------------------
h11
- patch 작성

--------------------
frozenlist

requirements:
  build:
    - cython>=3.0.0b3

--------------------
idna

package:
  name: idna
  version: 3.10
===>
package:
  name: idna
  version: "3.10"


--------------------
jiter

일단 포기 (maturin)

--------------------
jsonpatch

package:
  name: jsonpatch
  version: 1.33
===>
package:
  name: jsonpatch
  version: "1.33"

--------------------
orjson

일단 포기 (maturin)

--------------------
pydantic

일단 포기 (maturin)

--------------------
propcache

requirements:
  build:
    - cython>=3.0.12

--------------------
pydantic==2.10.6

일단 포기 (maturin)


--------------------
requests

일단 포기

--------------------
yarl

requirements:
  build:
    - cython>=3.0.12

--------------------
zstandard

일단 포기
```
