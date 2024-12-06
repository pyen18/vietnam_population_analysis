import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_economic_impact(input_path, output_dir):
    """
    Phân tích tác động kinh tế liên quan đến xu hướng dân số.
    
    Args:
        input_path (str): Đường dẫn dữ liệu đã lọc.
        output_dir (str): Thư mục lưu các biểu đồ.
    """
    try:
        # Đọc dữ liệu
        data = pd.read_csv(input_path, encoding='utf-8')
        print("Đọc dữ liệu thành công cho phân tích tác động kinh tế.")
        
        # Kiểm tra các cột cần thiết
        required_columns = ['Year', '15+ labor', 'Population grow ratio', 'Region', 'Average population']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Các cột sau bị thiếu: {missing_columns}. Không thể phân tích.")
            return
        
        # Tạo thư mục lưu trữ kết quả nếu chưa tồn tại
        os.makedirs(output_dir, exist_ok=True)
        
        # Phân tích: Xu hướng lực lượng lao động qua các năm
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Year', y='15+ labor', data=data, marker='o')
        plt.title("Xu hướng lực lượng lao động 15+ qua các năm")
        plt.xlabel("Năm")
        plt.ylabel("Lực lượng lao động 15+")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "labor_trend.png"))
        plt.close()
        print("Biểu đồ xu hướng lực lượng lao động đã được lưu.")
        
        # Phân tích: Mối liên hệ giữa lực lượng lao động và tăng trưởng dân số
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='15+ labor', y='Population grow ratio', data=data)
        sns.regplot(x='15+ labor', y='Population grow ratio', data=data, scatter=False, color='red')
        plt.title("Mối liên hệ giữa lực lượng lao động và tăng trưởng dân số")
        plt.xlabel("Lực lượng lao động 15+")
        plt.ylabel("Tăng trưởng dân số (%)")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "labor_vs_population_growth.png"))
        plt.close()
        print("Biểu đồ mối liên hệ giữa lực lượng lao động và tăng trưởng dân số đã được lưu.")
        
        # Phân tích: Dân số trung bình theo khu vực
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Region', y='Average population', data=data, ci=None, palette='viridis')
        plt.title("Dân số trung bình theo khu vực")
        plt.xlabel("Khu vực")
        plt.ylabel("Dân số trung bình")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "average_population_by_region.png"))
        plt.close()
        print("Biểu đồ dân số trung bình theo khu vực đã được lưu.")
        
    except Exception as e:
        print(f"Lỗi trong quá trình phân tích tác động kinh tế: {e}")

if __name__ == "__main__":
    input_csv = "data/cleaned/cleaned_population.csv"  # Đường dẫn đến file CSV đã làm sạch
    output_directory = "outputs/visualizations/Economic Impact"
    analyze_economic_impact(input_csv, output_directory)
