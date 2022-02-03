print('Salam BSQ  hesablamasina xos gelmisiz')
bsq = float(input("BSQ-nin qiymeti: "))
numb = input("Nece KSQ yazmisiz: ")
if numb == "1":
    ksq = float(input("Birinci KSQ- nin qiymeti: "))
    final = ksq * 0.4
    final1 = bsq * 0.6
    finish = final + final1
    if finish < 31.0 and finish > 21.0:
        print("Yarim illik: ", finish, " bal qiymet 2-dir.Siz cox zeifsiz!!!")
    if finish < 61.0 and finish > 31.0:
        print("Yarim illik: ", finish, " bal qiymet 3-dir")
    if finish > 61.0 and finish < 81.0:
        print("Yaeim illik: ", finish, " bal qiymet 4-dir")
    if finish > 81.0:
        print("Yarim illik: ", finish, " bal qiymet 5-dir")
if numb == "2":
    ksq1 = float(input("Birinci KSQ- nin qiymeti: "))
    ksq2 = float(input("Ikinci KSQ- nin qiymeti: "))
    final2 = ksq1 + ksq2
    final3 = final2 / 2
    final4 = final3 * 0.4  #KSQ - ler hesablandi
    final5 = bsq * 0.6
    finish1 = final4 + final5
    if finish1 < 31.0 and finish1 > 21.0:
        print("Yarim illik: ", finish1, " bal qiymet 2-dir.Siz cox zeifsiz!!!")
    if finish1 < 61.0 and finish1 > 31.0:
        print("Yarim illik: ", finish1, " bal qiymet 3-dir")
    if finish1 > 61.0 and finish1 < 81.0:
        print("Yaeim illik: ", finish1, " bal qiymet 4-dir")
    if finish1 > 81.0:
        print("Yarim illik: ", finish1, " bal qiymet 5-dir")
if numb == "3":
    ksq1 = float(input("Birinci KSQ- nin qiymeti: "))
    ksq2 = float(input("Ikinci KSQ- nin qiymeti: "))
    ksq3 = float(input("Ucuncu KSQ- nin qiymeti: "))
    final6 = ksq1 + ksq2 + ksq3
    final7 = final6 / 3
    final8 = final7 * 0.4  #KSQ - ler hesablandi
    final9 = bsq * 0.6
    finish2 = final8 + final9
    if finish2 < 31.0 and finish2 > 21.0:
        print("Yarim illik: ", finish2, " bal qiymet 2-dir.Siz cox zeifsiz!!!")
    if finish2 < 61.0 and finish2 > 31.0:
        print("Yarim illik: ", finish2, " bal qiymet 3-dir")
    if finish2 > 61.0 and finish2 < 81.0:
        print("Yaeim illik: ", finish2, " bal qiymet 4-dir")
    if finish2 > 81.0:
        print("Yarim illik: ", finish2, " bal qiymet 5-dir")
