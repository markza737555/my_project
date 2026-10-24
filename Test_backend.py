# จำลองการทำงานของระบบ backend (รับข้อมูลผู้ใช้ แล้วประมวลผลส่งกลับเป็น JSON-like)
# def get_user_profile(...): นี่คือการสร้าง Function (ชุดคำสั่งย่อย) เปรียบเสมือน API หลังบ้านที่รอรับข้อมูลเข้ามาประมวลผล
def get_user_profile(username, role):
    #สมองกลหลังบ้าน: จัดรูปแบบข้อมูลที่จะส่งกลับไปแสดงที่หน้าเว็บ
#Dictionary { ... }: โครงสร้างข้อมูลแบบจับคู่ (Key-Value) ซึ่งนิยมใช้ส่งข้อมูลหากันระหว่าง Frontend และ Backend ในรูปแบบ JSON
    profile = {
        "status": "success",
        "user": username, 
        "target_role": role,
        "message": "ยินดีต้อนรับสู่เส้นทาง Full-Stack Deverloper!"
    }
    # return profile: คำสั่งส่งข้อมูลออกหลังจากประมวลผลเสร็จแล้ว
    return profile

#จำลองการส่ง Request เข้ามาที่ระบบ
print("--- กำลังเชื่อมต่อกับระบบ backend ---")
username = input("กรอกชื่อของคุณ: ")
role = input("กรอกตำแหน่งของคุณ: ")

# เรียกใช้งานฟังก์ชันหลังบ้าน
response_data = get_user_profile(username, role)

# แสดงผลลัพธ์ที่ตอบกลับมา (เปรียบเสมือนสิ่งส่งกลับไปแสดงที่ Frontend)
print("\n[Response จาก Backend]:")
print(response_data)