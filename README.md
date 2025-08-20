# ROS2 Launch Files

Этот репозиторий содержит launch-файлы для запуска различных компонентов в ROS2.

## Использование

1. Создайте рабочее пространство ROS2 и склонируйте в него репозиторий:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone <repo_url> skoltech
    ```
2. Соберите рабочее пространство:
    ```bash
    cd ~/ros2_ws
    colcon build
    source ~/ros2_ws/install/setup.bash
    ```
3. Запустите нужный launch-файл:
    ```bash
    ros2 launch skoltech display.launch.py
    ```

## Требования

- ROS2 Humble или новее
- Python 3.8+

## Контакты

[chennikita70@gmail.com]
