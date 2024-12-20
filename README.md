# 🚀 MRU Calculator (Uniform Rectilinear Motion)

Welcome to the MRU Calculator! This is a simple project built to calculate **Distance**, **Velocity**, and **Time** in Uniform Rectilinear Motion (MRU) using the [NiceGUI](https://nicegui.io/) library. The user interface is interactive and completely implemented in Python.

## 📄 Description

This application allows users to calculate **Distance**, **Velocity**, or **Time** in MRU. Simply enter two of the three parameters (Distance, Velocity, or Time), and the calculator will calculate the remaining value.

### 🧮 Formulas used:
- **Distance (d)** = Velocity (v) * Time (t)
- **Velocity (v)** = Distance (d) / Time (t)
- **Time (t)** = Distance (d) / Velocity (v)

## 🛠️ Technologies Used
- **Python 3.9**: The programming language used for the logic of the calculator.
- **NiceGUI**: Library for the user interface (UI).
- **Docker**: For creating containers and simplifying deployment.

## ⚡ Features

- Calculate **Distance**, **Velocity**, or **Time**.
- User interface based on NiceGUI, simple and easy to use.
- Docker support for easy deployment.

## 📝 Installation

Follow these steps to run the MRU Calculator on your local environment:

### 1. Clone the repository

```bash
git clone https://github.com/millanda29/calculadora-mru.git
cd calculadora-mru
```

### 2. Create a virtual environment (optional but recommended)

If you prefer to create a virtual environment in Python, run:

```bash
python -m venv .uce
source .uce/bin/activate  # On Linux/Mac
.uce\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The app will be available at [http://localhost:8080](http://localhost:8080).

## 🐳 Deploy with Docker

If you prefer to run the app using Docker, follow these steps:

### 1. Build the Docker image

```bash
docker build -t millanda29/calculadora-mru .
```

### 2. Run the Docker container

```bash
docker run -p 8080:8080 millanda29/calculadora-mru
```

Access the app at [http://localhost:8080](http://localhost:8080).

## 📁 Project Structure

```
calculadora-mru/
│
├── app.py              # Python code for the application
├── Dockerfile          # Dockerfile for container deployment
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .gitignore          # Files to be ignored by git
```

## 🤝 Contributing

Contributions are welcome! If you'd like to improve or fix anything, please follow these steps:

1. Fork this repository.
2. Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'feat: new feature'`).
4. Push to your branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🧑‍💻 Author

**Millanda29** - [Your GitHub Profile](https://github.com/millanda29)
