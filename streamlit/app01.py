import streamlit as st

# สร้างเว็ปแอป
st.sidebar.subheader(':red[เลขฐานยอดนิยม📐]')

# สร้างเมนูแถบข้าง
menu_option = st.sidebar.radio("คำนวณเลขฐาน", ['เลขฐาน2', 'เลขฐาน3', 'เลขฐาน8', 'เลขฐาน16'])

# setbackground
def set_background(image_url):
    image_url_str = f'url("{image_url}")'
    css = f"""
    <style>
    .stApp {{
        background-image: {image_url_str};
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

##ใช้งานตรงนี้
set_background("https://png.pngtree.com/thumb_back/fh260/background/20220524/pngtree-linen-plain-clothing-material-map-image_1366872.jpg")

# รูปภาพ
st.image('https://www.teachernu.com/wp-content/uploads/2018/12/%E0%B8%9A%E0%B8%A7%E0%B8%81%E0%B8%A5%E0%B8%9A%E0%B9%80%E0%B8%A5%E0%B8%82%E0%B8%90%E0%B8%B2%E0%B8%99.png')

# สร้างเว็ปแอป ของ การคำนวณเลขฐานสอง
def decimal_to_binary(n):
    if n == 0:
        return '0'
    ternary = ''
    while n:
        n, r = divmod(n, 2)
        ternary = str(r) + ternary
    return ternary

def binary_to_decimal(n):
    decimal = 0
    for i, digit in enumerate(reversed(str(n))):
        decimal += int(digit) * (2 ** i)
    return decimal

# สร้างเว็ปแอป ของ การคำนวณเลขฐานสาม
def decimal_to_ternary(n):
    if n == 0:
        return '0'
    ternary = ''
    while n:
        n, r = divmod(n, 3)
        ternary = str(r) + ternary
    return ternary

def ternary_to_decimal(n):
    decimal = 0
    for i, digit in enumerate(reversed(str(n))):
        decimal += int(digit) * (3 ** i)
    return decimal

# สร้างเว็ปแอป ของ การคำนวณเลขฐานแปด
def decimal_to_octal(n):
    if n == 0:
        return '0'
    ternary = ''
    while n:
        n, r = divmod(n, 8)
        ternary = str(r) + ternary
    return ternary

def decimal_to_octall(n):
    decimal = 0
    for i, digit in enumerate(reversed(str(n))):
        decimal += int(digit) * (8 ** i)
    return decimal

# สร้างเว็ปแอป ของ การคำนวณเลขฐานสิบหก
def decimal_to_hexadecimal(n):
    if n == 0:
        return '0'
    ternary = ''
    while n:
        n, r = divmod(n, 16)
        ternary = str(r) + ternary
    return ternary

def hexadecimal_to_decimal(n):
    decimal = 0
    for i, digit in enumerate(reversed(str(n))):
        decimal += int(digit) * (16 ** i)
    return decimal

def main():
    if menu_option == 'เลขฐาน2':
        st.title(":red[แปลงเลขฐานสอง]")

        # สร้างช่องข้อมูลให้ผู้ใช้ป้อน
        option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นเลขฐานสอง", "ฐานสองเป็นทศนิยม"])

        # รับข้อมูลเลขทศนิยม
        if option == "ทศนิยมเป็นเลขฐานสอง":
         decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
         if st.button('แปลงเลข'):
           binary_num = decimal_to_binary(decimal_num)
           st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {binary_num}")

        # รับข้อมูลเลขฐาน
        elif option == "ฐานสองเป็นทศนิยม":
         binary_num = st.text_input("ป้อนเลขทศนิยม:")
         if st.button('แปลงเลข'):
            decimal_num = binary_to_decimal(binary_num)
            st.write(f"การแสดงทศนิยมของ {binary_num} คือ: {decimal_num}")
            

    if menu_option == 'เลขฐาน3':
        st.title(":red[แปลงเลขฐานสาม]")

        # สร้างช่องข้อมูลให้ผู้ใช้ป้อน
        option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นฐานสาม", "ฐานสามเป็นทศนิยม"])

        # รับข้อมูลเลขทศนิยม
        if option == "ทศนิยมเป็นฐานสาม":
         decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
         if st.button('แปลงเลข'):
            ternary_num = decimal_to_ternary(decimal_num)
            st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {ternary_num}")

        # รับข้อมูลเลขฐาน
        elif option == "ฐานสามเป็นทศนิยม":
         ternary_num = st.text_input("ป้อนเลขฐานสาม:")
         if st.button('แปลงเลข'):
            decimal_num = ternary_to_decimal(ternary_num)
            st.write(f"การแสดงทศนิยมของ {ternary_num} คือ: {decimal_num}")
 
    if menu_option == 'เลขฐาน8':
         st.title(":red[แปลงเลขฐานแปด]")

         # สร้างช่องข้อมูลให้ผู้ใช้ป้อน
         option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นฐานแปด", "ฐานแปดเป็นทศนิยม"])

         # รับข้อมูลเลขทศนิยม
         if option == "ทศนิยมเป็นฐานแปด":
           decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
           if st.button('แปลงเลข'):
                octal_num = decimal_to_octal(decimal_num)
                st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {octal_num}")

         # รับข้อมูลเลขฐาน      
         elif option == "ฐานแปดเป็นทศนิยม":
            octal_num = st.text_input("ป้อนเลขฐานแปด:")
            if st.button('แปลงเลข'):
                decimal_num =decimal_to_octall(octal_num)
                st.write(f"การแสดงทศนิยมของ {octal_num} คือ: {decimal_num}")
 
    if menu_option == 'เลขฐาน16':
        st.title(":red[แปลงเลขฐานสิบหก]") 

        # สร้างช่องข้อมูลให้ผู้ใช้ป้อน
        option = st.selectbox("เลือกตัวเลือก:", ["ทศนิยมเป็นฐานสิบหก", "ฐานสิบหกเป็นทศนิยม"])

        # รับข้อมูลเลขทศนิยม
        if option == "ทศนิยมเป็นฐานสิบหก":
         decimal_num = st.number_input("ป้อนเลขทศนิยม:", value=0, step=1)
         if st.button('แปลงเลข'):
            hexadecimal_num = decimal_to_hexadecimal(decimal_num)
            st.write(f"การแสดงทศนิยมของ {decimal_num} คือ: {hexadecimal_num}")

        # รับข้อมูลเลขฐาน
        elif option == "ฐานสิบหกเป็นทศนิยม":
         hexadecimal_num = st.text_input("ป้อนเลขฐานสิบหก:")
         if st.button('แปลงเลข'):
            decimal_num = hexadecimal_to_decimal(hexadecimal_num)
            st.write(f"การแสดงทศนิยมของ {hexadecimal_num} คือ: {decimal_num}")
if __name__ == "__main__":
    main()
