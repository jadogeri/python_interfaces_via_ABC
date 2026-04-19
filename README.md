
# 💳 Python Interfaces via Protocol
A professional implementation of the **Strategy Design Pattern** using Python's `typing.Protocol`. This project demonstrates how to create a decoupled, type-safe payment processing system.

**Version:** 2.0

**Date:** April 18, 2026

**Authors**: Joseph Adogeri ([@jadogeri](https://www.github.com/jadogeri))

## 🛠 Technology Stack
* **Language:** Python 3.10+
* **Testing:** [Pytest](https://pytest.org), [Unittest](https://python.org)
* **CI/CD:** GitHub Actions
* **Package Management:** Pip
* **Typing:** Static Type Hinting & Protocols (PEP 544)

## 📂 Project Structure

```text
python_interfaces_via_protocol/
├── .github/workflows/      # 🚀 CI/CD pipeline configurations
└── app/
    ├── src/
    │   ├── interfaces/
    │   │   └── payment.py   # 📜 Payment Protocol (Interface)
    │   ├── bitcoin.py       # ₿ Bitcoin implementation
    │   ├── credit_card.py   # 💳 Credit Card implementation
    │   └── debit_card.py    # 🏧 Debit Card implementation
    ├── tests.py            # 🧪 Unit tests for all payment methods
    ├── main.py              # 🏃 Entry point (Moved)
    ├── pyproject.toml       # ⚙️ Configuration (Moved)
    └── requirements.txt     # 📦 Dependencies (Moved)

```
## 📄 File Details

| File | Author | Version | Since | Description |
|---|---|---|---|---|
| payment.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | Defines the Payment Protocol (Interface). |
| bitcoin.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | ₿ Concrete logic for Bitcoin payments. |
| credit_card.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 💳 Concrete logic for Credit Card payments. |
| debit_card.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 🏧 Concrete logic for Debit Card payments. |
| tests.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 🧪 Comprehensive test suite with parameterization. |
| main.py | Joseph Adogeri | 1.0.0 | 2023-10-27 | 🎮 Orchestration of the payment implementations. |

Here is the updated Getting Started section. I have corrected the paths to reflect that your requirements.txt is now inside the app folder and added the essential "Sources Root" step for PyCharm.

## 🚀 Getting Started

### 1. Installation

#### Clone the repository
git clone https://github.com/jadogeri/python_interfaces_via_protocol.git
cd python_interfaces_via_protocol

#### Install dependencies from the app directory
```bash
pip install -r app/requirements.txt
```

### 2. Running the Application (PyCharm)

   1. Open Project: Open the root folder python_interfaces_via_protocol in PyCharm.
   2. Set Sources Root: Right-click the app folder in the Project sidebar → Mark Directory as → Sources Root (this turns the folder blue).
   3. Run: Navigate to app/main.py, right-click the file, and select Run 'main'.

### 3. Running the Application (Command Line)

#### Navigate to the app directory and run
```bash
cd app
python main.py
```

## 🧪 Running Tests

##### Ensure you are in the app directory
```bash
cd app
pytest tests.py
```
or

##### Ensure you are outside the app directory

```bash
python -m unittest app/tests.py

```

Note: This might require you to have your imports perfectly aligned or use PYTHONPATH if you get a ModuleNotFoundError.

### Run using the pytest configuration
PYTHONPATH=app pytest app/tests.py

------------------------------
## 📜 License

[LICENSE](/LICENSE)


