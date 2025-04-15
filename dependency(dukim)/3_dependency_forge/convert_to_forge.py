import re

def convert_to_forge_command():
    with open('dependency(dukim)/1_dependency_origin_check/origin_requirements.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # 패키지 이름 추출
                match = re.match(r'([^=]+)==(.+)', line)
                if match:
                    package_name = match.group(1)
                    print(f'forge iOS {package_name}')

if __name__ == '__main__':
    convert_to_forge_command() 