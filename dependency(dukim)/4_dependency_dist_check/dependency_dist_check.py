import os
import re

def convert_filename_to_requirement(filename):
    # .whl 확장자 제거
    name = filename.replace('.whl', '')
    
    # 패턴: 패키지명-버전-나머지
    pattern = r'^([a-zA-Z0-9_-]+)-([0-9.]+)'
    match = re.match(pattern, name)
    
    if match:
        package_name = match.group(1)
        version = match.group(2)
        
        # 하이픈을 언더스코어로 변환
        package_name = package_name.replace('-', '_')
        
        return f"{package_name}=={version}"
    return None

def main():
    dist_dir = 'dist'
    output_file = 'dependency(dukim)/4_dependency_dist_check/dependency_dist_check.txt'
    
    requirements = []
    
    # dist 폴더의 모든 파일 순회
    for filename in os.listdir(dist_dir):
        if filename.endswith('.whl'):
            requirement = convert_filename_to_requirement(filename)
            if requirement:
                requirements.append(requirement)
    
    # 중복 제거 및 정렬
    requirements = sorted(list(set(requirements)))
    
    # requirements.txt 파일에 쓰기
    with open(output_file, 'w') as f:
        for req in requirements:
            f.write(f"{req}\n")

if __name__ == '__main__':
    main() 