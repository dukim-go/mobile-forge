#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
origin_requirements.txt 파일을 처리하는 스크립트
- 각 라인 문자열을 하나의 라인의 문자열로 치환
- 대문자 > 소문자
- (-) 문자 -> (_) 문자로 치환
- 정렬
"""

import re
import os

def process_requirements(input_file, output_file):
    """
    requirements.txt 파일을 처리하여 새로운 형식으로 변환합니다.
    
    Args:
        input_file (str): 입력 파일 경로
        output_file (str): 출력 파일 경로
    """
    # 입력 파일 읽기
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # 처리된 패키지 목록
    processed_packages = []
    
    # 각 라인 처리
    for line in lines:
        line = line.strip()
        if not line:  # 빈 라인 건너뛰기
            continue
            
        # 패키지 이름과 버전 분리
        parts = line.split('==')
        if len(parts) != 2:
            continue  # 형식이 맞지 않는 라인 건너뛰기
            
        package_name = parts[0]
        version = parts[1]
        
        # 패키지 이름 처리
        # 대문자를 소문자로 변환
        package_name = package_name.lower()
        # 하이픈을 언더스코어로 변환
        package_name = package_name.replace('-', '_')
        
        # 처리된 패키지 추가
        processed_packages.append(f"{package_name}=={version}")
    
    # 알파벳 순으로 정렬
    processed_packages.sort()
    
    # 결과를 파일에 쓰기
    with open(output_file, 'w') as f:
        for package in processed_packages:
            f.write(f"{package}\n")
    
    print(f"처리 완료: {len(processed_packages)}개의 패키지가 {output_file}에 저장되었습니다.")

if __name__ == "__main__":
    # 현재 스크립트의 디렉토리
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 입력 및 출력 파일 경로
    input_file = os.path.join(current_dir, "origin_requirements.txt")
    output_file = os.path.join(current_dir, "sort_origin_requirements.txt")
    
    # 파일 처리
    process_requirements(input_file, output_file) 