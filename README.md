# 🦅 Python Interfaces via ABC (Bird Simulation)
A professional implementation of **Interface-based Programming** using Python's `abc.ABC`. This project demonstrates how to enforce behaviors across diverse bird species using multiple inheritance and Abstract Base Classes.

**Version:** 3.0

**Date:** April 22, 2026

**Authors**: Joseph Adogeri ([@jadogeri](https://github.com))

## 🛠 Technology Stack
* **Language:** Python 3.10+
* **Testing:** [Unittest](https://python.org)
* **Design Pattern:** Interface Segregation Principle (ISP)
* **Typing:** Static Type Hinting & ABC (PEP 3119)

## 📂 Project Structure

```text
python_interfaces_via_ABC/
├── .github/workflows/      # 🚀 CI/CD pipeline configurations
└── app/
    ├── src/
    │   ├── interfaces/
    │   │   ├── bird.py      # 📜 Base Bird ABC
    │   │   ├── flyable.py   # ☁️ Flyable Interface
    │   │   └── swimmable.py # 🌊 Swimmable Interface
    │   ├── eagle.py        # 🦅 Eagle implementation
    │   ├── penguin.py      # 🐧 Penguin implementation
    │   └── ostrich.py      # 🏜️ Ostrich implementation
    ├── tests.py            # 🧪 Unit tests for bird behaviors
    ├── main.py             # 🏃 Entry point
    ├── pyproject.toml      # ⚙️ Configuration
    └── requirements.txt    # 📦 Dependencies
```

## 📄 File Details



| File | Author | Version | Since | Description |
|---|---|---|---|---|
| bird.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | Base abstract class for all birds. |
| flyable.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | Interface for birds that can fly. |
| swimmable.py| Joseph Adogeri | 1.0.0 | 2023-10-27 | Interface for birds that can swim. |
| eagle.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 🦅 Logic for Eagles (Flyable). |
| penguin.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 🐧 Logic for Penguins (Swimmable). |
| ostrich.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 🏜️ Logic for Ostriches (Flightless). |
| tests.py | Joseph Adogeri | 1.1.0 | 2024-05-20 | 🧪 Unit tests with interface compliance checks. |
| main.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 🎮 Orchestration of bird behaviors. |

## 🚀 Getting Started

### 1. Installation

#### Clone the repository
```bash
git clone https://github.com
cd python_interfaces_via_ABC
```

#### Install dependencies
```bash
pip install -r app/requirements.txt
```

### 2. Running the Application (PyCharm)

1. **Open Project**: Open the root folder `python_interfaces_via_ABC` in PyCharm.
2. **Set Sources Root**: Right-click the **app** folder in the Project sidebar → **Mark Directory as** → **Sources Root**.
3. **Run**: Navigate to `app/main.py`, right-click, and select **Run 'main'**.

### 3. Running the Application (Command Line)

#### Navigate to the app directory and run
```bash
cd app
python main.py
```

## 🧪 Running Tests

##### Run all tests from the app directory
```bash
cd app
python tests.py
```

##### Troubleshooting Imports
If you encounter a `ModuleNotFoundError` or `AssertionError` during `isinstance` checks, ensure your `PYTHONPATH` is set to the `app` directory:
```bash
# Windows
set PYTHONPATH=%PYTHONPATH%;%CD\(\%\app\)
python app/tests.py

# Mac/Linux
export PYTHONPATH=\(PYTHONPATH:\)(pwd)/app
python app/tests.py
```

## 📜 License

[LICENSE](/LICENSE)
