import os
import pandas as pd
import matplotlib.pyplot as plt

def analyze_trends(input_path, output_path):
    """
    Phân tích xu hướng dân số qua các năm.

    Args:
        input_path (str): Đường dẫn dữ liệu đã lọc.
        output_path (str): Đường dẫn lưu biểu đồ xu hướng.
    """
    try:
        # Đọc dữ liệu
        data = pd.read_csv(input_path, encoding='utf-8')
        print("\u0110\u1ecdc d\u1eef li\u1ec7u th\u00e0nh c\u00f4ng!")

        # Kiểm tra các cột cần thiết
        required_columns = ['Year', '15+ labor', 'Population grow ratio', 
                            'Region', 'Average population', 'Population density', 'Sex ratio']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Thiếu các cột sau: {missing_columns}")
            return

        # Tạo thư mục lưu trữ kết quả nếu chưa tồn tại
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Vẽ biểu đồ xu hướng tổng dân số
        trend_data = data[['Year', 'Average population']].dropna()
        plt.figure(figsize=(10, 6))
        plt.plot(
            trend_data['Year'], 
            trend_data['Average population'], 
            marker='o', linestyle='-', color='b'
        )
        plt.title("Xu hướng Dân số Việt Nam (2011-2016)")
        plt.xlabel("Năm")
        plt.ylabel("Tổng Dân số (Nghìn người)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(output_path)
        plt.show()
        plt.close()

        # Phân tích tỷ lệ tăng trưởng dân số
        trend_data['Growth Rate (%)'] = trend_data['Average population'].pct_change() * 100
        growth_rate_path = os.path.join(os.path.dirname(output_path), 'growth_rate_population.png')
        plt.figure(figsize=(10, 6))
        plt.plot(
            trend_data['Year'], 
            trend_data['Growth Rate (%)'], 
            marker='o', linestyle='-', color='g'
        )
        plt.title("Tỷ lệ Tăng trưởng Dân số Việt Nam (2011-2016)")
        plt.xlabel("Năm")
        plt.ylabel("Tỷ lệ Tăng trưởng (%)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(growth_rate_path)
        plt.show()
        plt.close()

        # Phân tích bổ sung: Mật độ dân số
        if 'Population density' in data.columns:
            density_data = data[['Year', 'Population density']].dropna()
            density_path = os.path.join(os.path.dirname(output_path), 'population_density.png')
            plt.figure(figsize=(10, 6))
            plt.plot(
                density_data['Year'], 
                density_data['Population density'], 
                marker='o', linestyle='-', color='r'
            )
            plt.title("Xu hướng Mật độ Dân số Việt Nam (2011-2016)")
            plt.xlabel("Năm")
            plt.ylabel("Mật độ Dân số (người/km²)")
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(density_path)
            plt.show()
            plt.close()

        # Phân tích bổ sung: Lực lượng lao động
        if '15+ labor' in data.columns:
            labor_data = data[['Year', '15+ labor']].dropna()
            labor_force_path = os.path.join(os.path.dirname(output_path), 'labor_force.png')
            plt.figure(figsize=(10, 6))
            plt.plot(
                labor_data['Year'], 
                labor_data['15+ labor'], 
                marker='o', linestyle='-', color='c'
            )
            plt.title("Xu hướng Lực lượng Lao động Việt Nam (2011-2016)")
            plt.xlabel("Năm")
            plt.ylabel("Lực lượng Lao động (Nghìn người)")
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(labor_force_path)
            plt.show()
            plt.close()

    except Exception as e:
        print(f"Lỗi trong quá trình phân tích: {e}")

if __name__ == "__main__":
    # Cập nhật đường dẫn đến file CSV của bạn
    input_csv = 'data/cleaned/cleaned_population.csv'  # Đảm bảo đường dẫn chính xác
    output_chart = 'outputs/visualizations/Trend Analysis/trend_analysis.png'
    analyze_trends(input_csv, output_chart)