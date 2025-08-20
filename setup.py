from setuptools import setup, find_packages
import os

package_name = 'skoltech'
this_dir = os.path.abspath(os.path.dirname(__file__))

# always install package.xml
data_files = [
    (os.path.join('share', package_name), [os.path.join(this_dir, 'package.xml')]),
]

# папки которые хотим рекурсивно установить
dirs_to_install = ['launch', 'rviz', 'urdf', 'meshes', 'resource']

def add_dir(base_dir):
    path = os.path.join(this_dir, base_dir)
    if not os.path.isdir(path):
        return
    for root, _, files in os.walk(path):
        files = [f for f in files if not f.startswith('.')]
        if not files:
            continue
        # относительный путь внутри пакета, например 'meshes/ur3/visual'
        rel_dir = os.path.relpath(root, this_dir)
        target_dir = os.path.join('share', package_name, rel_dir)
        file_paths = [os.path.join(root, f) for f in files]
        data_files.append((target_dir, file_paths))

for d in dirs_to_install:
    add_dir(d)

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nktchen',
    maintainer_email='nktchen@todo.todo',
    description='skoltech: URDF + meshes + launch + rviz',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
