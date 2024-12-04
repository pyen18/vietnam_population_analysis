# scripts/preprocess.py
import pandas as pd
import os

def clean_data(input_path, output_path):
    """
    Làm sạch dữ liệu: xử lý giá trị thiếu, loại bỏ ngoại lệ, chuẩn hóa dữ liệu.
    
    Args:
        input_path (str): Đường dẫn dữ liệu thô.
        output_path (str): Đường dẫn lưu dữ liệu đã làm sạch.
    """
    try:
        # Đọc dữ liệu thô
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công.")

        # Kiểm tra các giá trị bị thiếu
        missing = data.isnull().sum()
        print("Các giá trị bị thiếu:\n", missing)

        # Xử lý giá trị thiếu (ví dụ: điền giá trị trung bình hoặc loại bỏ)
        data = data.fillna(method='ffill')  # Dùng forward fill
        data = data.fillna(method='bfill')  # Dùng backward fill nếu còn thiếu

        # Loại bỏ các giá trị ngoại lệ (ví dụ: dân số âm hoặc không hợp lý)
        if 'population' in data.columns:
            data = data[data['population'] > 0]

        # Chuẩn hóa dữ liệu (ví dụ: chuyển đổi kiểu dữ liệu)
        data['year'] = data['year'].astype(int)
        if 'population' in data.columns:
            data['population'] = data['population'].astype(int)
        if 'growth_rate' in data.columns:
            data['growth_rate'] = data['growth_rate'].astype(float)

        # Lưu dữ liệu đã làm sạch
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_csv(output_path, index=False, encoding='utf-8')
        print(f"Dữ liệu đã làm sạch và lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi trong quá trình làm sạch dữ liệu: {e}")

if __name__ == "__main__":
    input_csv = "data/raw/population_en_v2.csv"
    output_csv = "data/cleaned/cleaned_population.csv"
    clean_data(input_csv, output_csv)
