import time
import functools
import operator
import random
import math
print('เกมคณิตคิดเร็ว (　＾ω＾)')
time.sleep(2)
print('แน่จริงก็คิดเลขให้ได้ไวที่สุด ( *´・ω)/(；д； )')
time.sleep(3)
print('พร้อมแล้วก็ มาเริ่มกันเลย!!')
time.sleep(3)
type_solving=input('เลือกได้เลยว่าจะคำนวณเเบบไหน(พิมพ์ +,-,*):')
if type_solving not in ['+','-','*']:
    print('บอกให้พิมพ์เเค่ +, -, * เดี๋ยวตีเลยย!!!')
else:
    start_time=time.time()
    print('คุณมีเวลาในการตอบทั้งหมด3นาที')
    score=0
    while True:
        difficulty_base=2
        difficulty_increasing = math.floor(score/20)
        overall_difficulty=difficulty_base + difficulty_increasing
        numbers_list=[]
        for x in range(overall_difficulty):
            value=random.randint(1,9+(difficulty_increasing*2))
            numbers_list.append(value)
        if type_solving == '+':
            answer = functools.reduce(operator.add, numbers_list)
            print('บวกเลขที่กำหนดให้', numbers_list)
        elif type_solving == '-':
            answer = functools.reduce(operator.sub, numbers_list)
            print('ลบเลขที่กำหนดให้(คำตอบเป็นจำนวนเต็มลบ ให้ใส่เครื่องหมาย -หน้าคำตอบ)', numbers_list)
        elif type_solving == '*':
            answer = functools.reduce(operator.mul, numbers_list,)
            print('คูณตัวเลขที่กำหนดให้', numbers_list)
        else :
            print('บอกให้พิมพ์เเค่ +, -, * เดี๋ยวตีเลยย!!!')
        guess=int(input())
        time_out = time.time()-start_time
        if time_out > 180 :
            print('หมดเวลา เกมจบเเล้ว!!! (ノ-_-)ノ~┻━┻')
            elapsed_time=time.time() - start_time
            print('คะแนนของคุณคือ', score, 'ใช้เวลาไปทั้งหมด', (elapsed_time), 'วินาที')
            break
        if guess == answer:
            score = score +(1*overall_difficulty)
            continue
        else:
            print('เกมจบแล้ว!!! คำตอบที่ถูกคือ', answer,'(TдT )')
            elapsed_time=time.time() - start_time
            print('คะแนนของคุณคือ', score, 'ใช้เวลาไปทั้งหมด', (elapsed_time), 'วินาที')
            break
