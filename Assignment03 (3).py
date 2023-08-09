print ("โปรแกรมคำนวณการทาสี:")
width = int(input ("ใส่ขนาดความกว้างของบ้าน(เมตร) : "))
long = int(input ("ใส่ขนาดความยาวของบ้าน(เมตร) : "))
height = int(input ("ใส่ขนาดความสูงของบ้าน(เมตร) : "))

OSarea = width*long*height
Hp = OSarea/2.5
paintcan = Hp/4
totalprice = paintcan*200

print ("จำนวนพื้นที่บ้านภายนอกในการทาสีทั้งหมด : ",OSarea,"ตารางเมตร")
print ("จำนวนสีที่ใช้ในการทาสีทั้งหมด : ",Hp,"ลิตร")
print ("จำนวนกระป๋องสีที่ใช้ในการทาสี : ",int(paintcan),"กระป๋อง")
print ("จำนวนเงินที๋่เป็นค่าใช้จ่ายในการซื้อสี : ",totalprice,"บาท")
