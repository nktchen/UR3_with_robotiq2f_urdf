from setuptools import setup
import os

package_name = 'skoltech'

# соберём data_files: package.xml + рекурсивно все файлы из meshes, rviz и urdf
data_files = [
    ('share/' + package_name, ['package.xml']),
]

def add_dir_to_data_files(base_dir):
    """Добавляет все файлы из base_dir в data_files в виде
       ('share/skoltech/<rel_dir>', [list_of_files])"""
    if not os.path.isdir(base_dir):
        return
    for root, dirs, files in os.walk(base_dir):
        files = [f for f in files if not f.startswith('.')]
        if not files:
            continue
        rel_dir = os.path.relpath(root, '.')  # 'meshes/...' или 'rviz' и т.д.
        target_dir = os.path.join('share', package_name, rel_dir)
        file_paths = [os.path.join(root, f) for f in files]
        data_files.append((target_dir, file_paths))

# добавить папки, если они есть
add_dir_to_data_files('meshes')
add_dir_to_data_files('rviz')
add_dir_to_data_files('urdf')

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nktchen',
    maintainer_email='nktchen@todo.todo',
    description='skoltech package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
