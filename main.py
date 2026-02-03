# 16-masala
def ozgartirish(roy):
    for i in range(len(roy)):
        if roy[i] < 0:
            roy[i] = 0
            print(roy)

ozgartirish([2, -5, 2, 5])
# 17-masala
def salomlashish(ism, yosh):
    print(f"Salom, {ism}! Siz {yosh} yoshdasiz.")

salomlashish("Sobir", 19)
# 18-masala
def split_text(text, symbol):
    parts = text.split(symbol)
    for p in parts:
        print(p)

split_text("2026-02-03", "-")
# 19-masala
def tortburchak_chizish(kenglik, balandlik):
    for _ in range(balandlik):
        print("*" * kenglik)

tortburchak_chizish(5, 5)
# 20-masala
def katta_harfga_otkzish(roy):
    for i in range(len(roy)):
        if isinstance(roy[i], str):
            roy[i] = roy[i].upper()
            print(roy)

katta_harfga_otkzish(["Hello world"])
