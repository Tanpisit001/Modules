"""
main.py
โปรแกรมสาธิตการเรียกใช้งาน 10 modules
"""

import math_utils
import string_utils
import file_utils
import date_utils
import validator
import converter
import logger
import random_utils
import stats_utils
import greeting


def main():
    # 0. ข้อความต้อนรับ (Module 10: greeting)
    print(greeting.welcome_message())

    # 1. Module: math_utils
    print(greeting.section_title("1. Math Utils"))
    print("5 + 3 =", math_utils.add(5, 3))
    print("5 - 3 =", math_utils.subtract(5, 3))
    print("5 * 3 =", math_utils.multiply(5, 3))
    print("5 / 3 =", round(math_utils.divide(5, 3), 2))
    print("5! =", math_utils.factorial(5))

    # 2. Module: string_utils
    print(greeting.section_title("2. String Utils"))
    text = "Level"
    print(f"reverse('{text}') =", string_utils.reverse_string(text))
    print(f"is_palindrome('{text}') =", string_utils.is_palindrome(text))
    print("count_vowels('hello world') =", string_utils.count_vowels("hello world"))
    print("to_title_case('python program') =", string_utils.to_title_case("python program"))

    # 3. Module: file_utils
    print(greeting.section_title("3. File Utils"))
    demo_path = "demo_output.txt"
    print(file_utils.write_text_file(demo_path, "สวัสดี นี่คือไฟล์ทดสอบ"))
    print("อ่านไฟล์กลับมา:", file_utils.read_text_file(demo_path))
    print("ไฟล์มีอยู่จริงหรือไม่:", file_utils.file_exists(demo_path))
    print("ขนาดไฟล์ (bytes):", file_utils.get_file_size(demo_path))

    # 4. Module: date_utils
    print(greeting.section_title("4. Date Utils"))
    print("วันเวลาปัจจุบัน:", date_utils.get_current_datetime())
    print("2026-01-01 + 30 วัน =", date_utils.add_days("2026-01-01", 30))
    print("ระยะห่างวัน 2026-01-01 ถึง 2026-03-01:",
          date_utils.days_between("2026-01-01", "2026-03-01"), "วัน")

    # 5. Module: validator
    print(greeting.section_title("5. Validator"))
    print("test@example.com ถูกต้องหรือไม่:", validator.is_valid_email("test@example.com"))
    print("0812345678 เป็นเบอร์โทรที่ถูกต้องหรือไม่:", validator.is_valid_phone("0812345678"))
    print("'123.45' เป็นตัวเลขหรือไม่:", validator.is_numeric("123.45"))

    # 6. Module: converter
    print(greeting.section_title("6. Converter"))
    print("30°C =", round(converter.celsius_to_fahrenheit(30), 2), "°F")
    print("86°F =", round(converter.fahrenheit_to_celsius(86), 2), "°C")
    print("10 กม. =", round(converter.km_to_miles(10), 2), "ไมล์")
    print("70 กก. =", round(converter.kg_to_pounds(70), 2), "ปอนด์")

    # 7. Module: logger
    print(greeting.section_title("7. Logger"))
    logger.log_info("โปรแกรมทำงานปกติ")
    logger.log_warning("นี่คือตัวอย่างคำเตือน")
    logger.log_error("นี่คือตัวอย่างข้อผิดพลาด (จำลอง)")

    # 8. Module: random_utils
    print(greeting.section_title("8. Random Utils"))
    print("สุ่มตัวเลข 1-100:", random_utils.random_number(1, 100))
    print("สุ่มสตริง 8 ตัวอักษร:", random_utils.random_string(8))
    fruits = ["แอปเปิ้ล", "กล้วย", "ส้ม", "มะม่วง"]
    print("สลับลิสต์:", random_utils.shuffle_list(fruits))
    print("สุ่มเลือกผลไม้:", random_utils.pick_random_item(fruits))

    # 9. Module: stats_utils
    print(greeting.section_title("9. Stats Utils"))
    numbers = [10, 20, 30, 40, 50]
    print("ข้อมูล:", numbers)
    print("ค่าเฉลี่ย (mean):", stats_utils.mean(numbers))
    print("ค่ามัธยฐาน (median):", stats_utils.median(numbers))
    print("ความแปรปรวน (variance):", stats_utils.variance(numbers))
    print("ส่วนเบี่ยงเบนมาตรฐาน (std dev):", round(stats_utils.std_deviation(numbers), 2))

    # 10. ข้อความจบ (Module 10: greeting)
    print(greeting.goodbye_message())


if __name__ == "__main__":
    main()
