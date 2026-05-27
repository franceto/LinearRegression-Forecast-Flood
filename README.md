# Flood Prediction Linear Regression

<div align="center">

**Dự án dự đoán xác suất xảy ra lũ lụt bằng Linear Regression trên Flood Prediction Dataset từ Kaggle.**

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Linear%20Regression-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-AI%20Explanation-F55036?style=for-the-badge)

</div>

---

## 1. Project Title & Catchphrase

**Flood Prediction Linear Regression** là dự án dự đoán biến mục tiêu `FloodProbability` từ 20 đặc trưng số liên quan đến môi trường, hạ tầng, khí hậu và quản lý rủi ro.

Dự án sử dụng **Linear Regression** làm mô hình hồi quy cơ bản, kèm pipeline chuẩn gồm EDA, xử lý dữ liệu, chuẩn hóa, huấn luyện, đánh giá và demo bằng Streamlit.

---

## 2. Quick Demo & Visuals

Repository hiện chưa cung cấp ảnh demo trong README gốc, nên phần hình ảnh minh họa được bỏ qua.

Sau khi chạy ứng dụng Streamlit, người dùng có thể nhập thủ công 20 đặc trưng và nhận kết quả dự đoán `FloodProbability`.

---

## 3. Tính Năng Nổi Bật

- **Dự đoán xác suất lũ lụt:** dự đoán `FloodProbability` từ 20 biến đầu vào dạng số.
- **Pipeline hồi quy đầy đủ:** bao gồm đọc dữ liệu, EDA, xóa trùng, train/test split, chuẩn hóa và huấn luyện.
- **Đánh giá mô hình:** sử dụng MAE, MSE, R2 và Cross Validation.
- **Lưu artifacts:** lưu mô hình Linear Regression và scaler bằng `joblib`.
- **Demo Streamlit:** hỗ trợ nhập thủ công đặc trưng, hiển thị bảng tóm tắt input, biểu đồ đơn giản và giải thích bằng Groq AI bằng tiếng Việt.

---

## 4. Công Nghệ Sử Dụng

<div align="center">

![Python](https://img.shields.io/badge/Python-Core%20Pipeline-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Regression-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-EDA-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Processing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Artifacts-111827?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Vietnamese%20Explanation-F55036?style=for-the-badge)

</div>

### Thành phần kỹ thuật

| Nhóm | Công nghệ | Vai trò |
|---|---|---|
| Model | Linear Regression | Dự đoán `FloodProbability` |
| Data processing | Pandas, NumPy | Đọc dữ liệu, EDA và xử lý bảng |
| Preprocessing | StandardScaler | Chuẩn hóa 20 biến đầu vào |
| Evaluation | scikit-learn | Tính MAE, MSE, R2 và Cross Validation |
| Model persistence | joblib | Lưu model và scaler |
| Demo | Streamlit | Giao diện nhập dữ liệu và dự đoán |
| Explanation | Groq AI | Giải thích kết quả bằng tiếng Việt trong app |

---

## 5. Triển Khai Nhanh

**Prerequisites**

- Python 3.x
- Windows PowerShell hoặc terminal tương đương
- Dataset `data/flood.csv`
- File artifacts nếu chỉ muốn chạy demo: `models/linear_regression_model.pkl` và `models/scaler.pkl`

```bash
# Clone repository
git clone <YOUR_GITHUB_REPO_URL>
cd Flood_Prediction_LinearRegression

# Tạo và kích hoạt môi trường ảo trên Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Cài thư viện cho notebook và training
pip install -r requirements.txt

# Huấn luyện mô hình trong notebook
# Mở notebooks/flood.ipynb và chạy toàn bộ pipeline

# Cài thư viện cho Streamlit app
pip install -r streamlit_app/requirements_streamlit.txt

# Chạy Streamlit app
streamlit run streamlit_app/app.py
```

---

## 6. Tài Liệu Dự Án

### Bài toán

| Thành phần | Mô tả |
|---|---|
| Input | 20 biến số về môi trường, hạ tầng, khí hậu và quản lý |
| Output | `FloodProbability` |
| Task | Regression |
| Model | Linear Regression |
| Demo | Streamlit |
| AI explanation | Groq AI bằng tiếng Việt |

### Dataset

| Hạng mục | Thông tin |
|---|---:|
| File dữ liệu | `data/flood.csv` |
| Số dòng | 50.000 |
| Số cột | 21 |
| Số đặc trưng | 20 |
| Biến mục tiêu | `FloodProbability` |

### Danh sách đặc trưng

```text
MonsoonIntensity
TopographyDrainage
RiverManagement
Deforestation
Urbanization
ClimateChange
DamsQuality
Siltation
AgriculturalPractices
Encroachments
IneffectiveDisasterPreparedness
DrainageSystems
CoastalVulnerability
Landslides
Watersheds
DeterioratingInfrastructure
PopulationScore
WetlandLoss
InadequatePlanning
PoliticalFactors
```

### Pipeline huấn luyện

Notebook chính:

```text
notebooks/flood.ipynb
```

Các bước chính:

```text
1. Đọc dữ liệu từ data/flood.csv
2. Khám phá dữ liệu
3. Xóa dữ liệu trùng lặp
4. Chia train/test
5. Chuẩn hóa dữ liệu bằng scaler
6. Huấn luyện Linear Regression
7. Đánh giá bằng MAE, MSE, R2 và Cross Validation
8. Lưu model và scaler bằng joblib
```

### Streamlit App

Tính năng chính:

- Nhập thủ công 20 đặc trưng đầu vào.
- Dự đoán `FloodProbability`.
- Hiển thị bảng tóm tắt dữ liệu nhập.
- Hiển thị trực quan hóa đơn giản.
- Giải thích kết quả bằng Groq AI bằng tiếng Việt.

Chạy app:

```bash
pip install -r streamlit_app/requirements_streamlit.txt
streamlit run streamlit_app/app.py
```

### Model Artifacts

| File | Vai trò |
|---|---|
| `models/linear_regression_model.pkl` | Mô hình Linear Regression đã huấn luyện |
| `models/scaler.pkl` | Scaler dùng để chuẩn hóa dữ liệu đầu vào |

### Cấu trúc dự án

```text
Flood_Prediction_LinearRegression/
├── .venv/
├── data/
│   └── flood.csv
├── models/
│   ├── linear_regression_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── flood.ipynb
├── streamlit_app/
│   ├── app.py
│   ├── utils.py
│   ├── api_groq.txt
│   └── requirements_streamlit.txt
├── requirements.txt
└── README.md
```

### Git ignore khuyến nghị

```text
.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
streamlit_app/api_groq.txt
```

Nếu không muốn đưa dữ liệu hoặc model lên GitHub, có thể thêm:

```text
data/
models/
*.pkl
```

### Lưu ý sử dụng

- Không commit file `streamlit_app/api_groq.txt` nếu file này chứa API key thật.
- Khi chạy Streamlit app, cần đảm bảo đường dẫn tới model và scaler đúng.
- Mô hình Linear Regression là baseline dễ giải thích, chưa đại diện cho mô hình tối ưu nhất cho mọi trường hợp.
- Kết quả phụ thuộc cách chia dữ liệu, scaler và dữ liệu đầu vào.
- Dự án phục vụ học tập, thực hành hồi quy và demo AI.

### Tác giả

**To Anh Phap**

### Giấy phép

README gốc chưa nêu license cụ thể. Nếu public repository, nên bổ sung file `LICENSE` phù hợp với mục đích sử dụng.
