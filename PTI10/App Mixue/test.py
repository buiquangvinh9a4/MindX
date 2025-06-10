import json
from datetime import datetime
from fpdf import FPDF

def xuat_hoa_don(username, danh_sach_mua):
    hoa_don = {
        "username": username,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "purchase": danh_sach_mua
    }
    
    with open("hoa_don.json", "w", encoding="utf-8") as file:
        json.dump(hoa_don, file, indent=4, ensure_ascii=False)
    
    return hoa_don

def tao_pdf(hoa_don):
    pdf = FPDF()
    pdf.add_font("DejaVu", "", "/Users/macos/Documents/HNUE/Programming/MindX/PTI10/App Mixue/scripts/DejaVuSans.ttf", uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Thêm font Unicode
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)
    
    pdf.cell(200, 10, "HÓA ĐƠN BÁN HÀNG", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, f"Khách hàng: {hoa_don['username']}", ln=True)
    pdf.cell(200, 10, f"Thời gian: {hoa_don['time']}", ln=True)
    pdf.ln(10)
    
    pdf.cell(80, 10, "Tên mặt hàng", border=1)
    pdf.cell(30, 10, "Số lượng", border=1, align='C')
    pdf.cell(40, 10, "Giá tiền", border=1, align='C')
    pdf.cell(40, 10, "Thành tiền", border=1, align='C')
    pdf.ln()
    
    tong_tien = 0
    for item in hoa_don["purchase"]:
        thanh_tien = item["soLuong"] * item["giaTien"]
        tong_tien += thanh_tien
        pdf.cell(80, 10, item["tenMatHang"], border=1)
        pdf.cell(30, 10, str(item["soLuong"]), border=1, align='C')
        pdf.cell(40, 10, f"{item['giaTien']:,} VND", border=1, align='C')
        pdf.cell(40, 10, f"{thanh_tien:,} VND", border=1, align='C')
        pdf.ln()
    
    pdf.ln(10)
    pdf.cell(200, 10, f"Tổng tiền: {tong_tien:,} VND", ln=True, align='R')
    
    pdf.output("hoa_don.pdf")
    print("Hóa đơn PDF đã được tạo thành công!")

# Danh sách các mặt hàng
mat_hang = [
   
            {
                "tenMatHang": "Trà sữa Phương Tuấn",
                "soLuong": 6,
                "giaTien": 90000,
                "hinhAnh": "images/trasua.jpg"
            },
            {
                "tenMatHang": "Trà sữa Bạc Hà",
                "soLuong": 4,
                "giaTien": 120000,
                "hinhAnh": "images/trasua.jpg"
            },
            {
                "tenMatHang": "Hồng trà sữa",
                "soLuong": 5,
                "giaTien": 125000,
                "hinhAnh": "images/trasua.jpg"
            },
            {
                "tenMatHang": "Trà sữa hạt dẻ",
                "soLuong": 4,
                "giaTien": 80000,
                "hinhAnh": "images/trasua.jpg"
            }
        
]

# Xuất hóa đơn
hoa_don = xuat_hoa_don("user1", mat_hang)
print(json.dumps(hoa_don, indent=4, ensure_ascii=False))

# Tạo file PDF
tao_pdf(hoa_don)