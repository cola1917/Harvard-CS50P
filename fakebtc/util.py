import sqlite3
import os
from fpdf import FPDF

class simpleToolSql():
    """
    simpleToolSql for sqlite3
    """

    def __init__(self,filename="fakebtc"):
        self.filename = filename + ".db"
        self.db = sqlite3.connect(self.filename)
        self.c = self.db.cursor()

    def close(self):
        self.c.close()
        self.db.close()

    def execute(self,sql,param=None):
        try:
            if param is None:
                self.c.execute(sql)
            else:
                if type(param) is list:
                    self.c.executemany(sql,param)
                else :
                    self.c.execute(sql,param)
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print(e)
            return False,e
        if count > 0 :
            return True
        else :
            return False

    def query(self,sql,param=None):
        if param is None:
            self.c.execute(sql)
        else:
            self.c.execute(sql,param)
        return self.c.fetchall()

class PDF(FPDF):
    def header(self):
        self.image("./CS50P-DUCK.png", 5, 40, 200)
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'FAKEBTC', 0, 0, 'L')
        self.cell(0, 10, 'FOR CS50P', 0, 1, 'R')

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
        self.line(10, 285, 200, 285)

# pdf = PDF()
# pdf.add_page()
# pdf.set_font('Times', '', 12)
# lorem_ipsum = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
#                "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
#                "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
#                "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
#                "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
# lines = lorem_ipsum.split('. ')
# for line in lines:
#     pdf.cell(0, 10, line, 0, 1)

# # Output the PDF to a file
# pdf.output('example.pdf')
# from PIL import Image

# # 打开图像
# image = Image.open("CS50P-DUCK.png")

# # 将图像转换为RGBA模式（如果尚未处于此模式）
# image = image.convert("RGBA")

# # 获取图像数据
# data = image.getdata()

# # 新的图像数据列表，其中包括透明度调整
# new_data = []
# for item in data:
#     # 如果背景颜色为白色（这里的判断可以根据您的需求修改）
#     if item[0] > 200 and item[1] > 200 and item[2] > 200:
#         new_data.append((255, 255, 255, 0))  # 设置为完全透明
#     else:
#         new_data.append(item)  # 保持原始颜色和透明度

# # 更新图像数据
# image.putdata(new_data)

# # 保存新图像
# image.save("output_image.png")

