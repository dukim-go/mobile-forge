import os
import re

def create_recipe_file(package_name, version):
    # recipes 디렉토리가 없으면 생성
    if not os.path.exists('recipes'):
        os.makedirs('recipes')
    
    # 패키지 디렉토리 생성
    package_dir = os.path.join('recipes', package_name)
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)
    
    # meta.yaml 파일 생성
    meta_yaml_path = os.path.join(package_dir, 'meta.yaml')
    with open(meta_yaml_path, 'w') as f:
        f.write(f'''package:
  name: {package_name}
  version: {version}
''')

def process_requirements():
    with open('dependency(dukim)/1_dependency_origin_check/origin_requirements.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # 패키지 이름과 버전 분리
                match = re.match(r'([^=]+)==(.+)', line)
                if match:
                    package_name, version = match.groups()
                    create_recipe_file(package_name, version)
                    print(f'Created recipe for {package_name}=={version}')

if __name__ == '__main__':
    process_requirements() 