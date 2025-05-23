from SinhVien import SinhVien  # Đảm bảo file SinhVien.py tồn tại và đúng

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []  # Khởi tạo là instance attribute

    def generateID(self):
        max_id_val = 0
        if self.listSinhVien: # Kiểm tra list có rỗng không
            for sv in self.listSinhVien:
                if sv._id > max_id_val:
                    max_id_val = sv._id
        return max_id_val + 1

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyên ngành của sinh vien: ") # Giả sử major là string
        while True:
            try:
                diemTB = float(input("Nhap diem cua sinh vien: "))
                if 0 <= diemTB <= 10: # Kiểm tra điểm hợp lệ
                    break
                else:
                    print("Điểm trung bình phải từ 0 đến 10. Vui lòng nhập lại.")
            except ValueError:
                print("Điểm trung bình phải là một số. Vui lòng nhập lại.")

        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        print("Thêm sinh viên thành công!")

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if sv is not None:
            print(f"Cập nhật thông tin cho sinh viên có ID: {ID}")
            sv._name = input(f"Nhap ten sinh vien moi (hiện tại: {sv._name}): ") or sv._name
            sv._sex = input(f"Nhap gioi tinh sinh vien moi (hiện tại: {sv._sex}): ") or sv._sex
            sv._major = input(f"Nhap chuyen nganh của sinh vien moi (hiện tại: {sv._major}): ") or sv._major # Giả sử major là string
            
            while True:
                try:
                    diemTB_str = input(f"Nhap diem cua sinh vien moi (hiện tại: {sv._diemTB}): ")
                    if not diemTB_str: # Nếu người dùng không nhập gì, giữ giá trị cũ
                        break 
                    diemTB = float(diemTB_str)
                    if 0 <= diemTB <= 10:
                        sv._diemTB = diemTB
                        break
                    else:
                        print("Điểm trung bình phải từ 0 đến 10. Vui lòng nhập lại.")
                except ValueError:
                    print("Điểm trung bình phải là một số. Vui lòng nhập lại.")
            
            self.xepLoaiHocLuc(sv)
            print("Cập nhật sinh viên thành công!")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.") # Sửa lỗi chính tả

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        print("Đã sắp xếp danh sách sinh viên theo ID.")

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        print("Đã sắp xếp danh sách sinh viên theo Tên.")

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False) # Giả sử là _diemTB
        print("Đã sắp xếp danh sách sinh viên theo Điểm TB.")

    def findByID(self, ID):
        # searchResult = None # Không cần thiết nếu dùng return trực tiếp
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv._id == ID:
                    return sv # Trả về ngay khi tìm thấy
        return None # Trả về None nếu không tìm thấy

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                # Kiểm tra _name có tồn tại và là string không trước khi upper()
                if hasattr(sv, '_name') and isinstance(sv._name, str) and \
                   keyword.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            isDeleted = True
            print(f"Đã xóa sinh viên có ID = {ID}.")
        else:
            print(f"Không tìm thấy sinh viên có ID = {ID} để xóa.")
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5: # Giả sử là _diemTB
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        print("-" * 70) # Dòng kẻ cho đẹp
        print("{:<8} {:<18} {:<8} {:<15} {:<10} {:<10}".format(
            "ID", "Name", "Sex", "Major", "Điểm TB", "Học Lực"))
        print("=" * 70) # Dòng kẻ

        if len(listSV) > 0:
            for sv_item in listSV: # Đổi tên biến để không trùng với sv trong các hàm khác
                print("{:<8} {:<18} {:<8} {:<15} {:<10.2f} {:<10}".format(
                    sv_item._id, sv_item._name, sv_item._sex, sv_item._major, sv_item._diemTB, sv_item._hocLuc))
        else:
            print("Danh sách sinh viên rỗng.")
        print("-" * 70) # Dòng kẻ
        # print("\n") # Thường không cần thêm \n ở cuối print, tự nó xuống dòng rồi

    def getListSinhVien(self):
        return self.listSinhVien