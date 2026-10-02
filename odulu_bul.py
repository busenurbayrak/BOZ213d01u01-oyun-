import tkinter as tk
import random
# değişkenler
prize_location = random.randint(0,9)
attempts_left = 3
# fonksiyonlar
def play_game():
    global attempts_left
    user_guess = entry_guess.get()
    entry_guess.delete(0, tk.END)
    if not user_guess.isdigit():
        lbl_result.config(text="HATA: Tam sayı girin!", fg="red")
        return
    guess = int(user_guess)
    if guess < 0 or guess > 9:
        lbl_result.config(text="HATA: 0 ile 9 arasında tam sayı girin!", fg="red")
        return
    attempts_left = attempts_left - 1
    # kazanma durumu
    if guess == prize_location:
        lbl_result.config(text="tebrikler, ödülü buldun!", fg="lime green")
        lbl_status.config(text="kazandınız!", fg="lime green")
        btn_submit.config(state=tk.DISABLED)
    # kaybetme durumu
    elif attempts_left == 0:
        lbl_result.config(text=f"kaybettin, Ödül {prize_location} numaradaydı.", fg="red")
        btn_submit.config(state=tk.DISABLED)
    # yanlış tahmin
    else:
        lbl_result.config(text="Boş kutu!", fg="red")
        lbl_status.config(text=f"Kalan Deneme: {attempts_left}")
def reset_game():
    global attempts_left, prize_location
    attempts_left = 3
    prize_location = random.randint(0, 9)
    lbl_status.config(text="Kalan Deneme: 3", fg="#2ecc71")
    lbl_result.config(text="Oyun sıfırlandı! Bol şans.", fg="white")
    btn_submit.config(state=tk.NORMAL)
# --- ARAYÜZ (GUI) TASARIMI ---
root = tk.Tk()
root.title("Ödül Avı")
root.geometry("350x350") 
root.configure(bg="#2c3e50")
tk.Label(root, text=" ÖDÜLÜ BUL!", font=("Arial", 11, "bold"), fg="#f1c40f", bg="#2c3e50").pack(pady=20)
tk.Label(root, text="Hangi kutuyu açmak istiyorsun? (0-9)", font=("Arial", 10), fg="white", bg="#2c3e50").pack()
entry_guess = tk.Entry(root, font=("Arial", 16), width=5, justify="center")
entry_guess.pack(pady=10)
btn_submit = tk.Button(root, text="KUTUYU AÇ", command=play_game, bg="#e74c3c", fg="white", font=("Arial", 12, "bold"))
btn_submit.pack(pady=10)
lbl_status = tk.Label(root, text="Kalan Deneme: 3", font=("Arial", 12), fg="#2ecc71", bg="#2c3e50")
lbl_status.pack(pady=5)
lbl_result = tk.Label(root, text="Bol şans!", font=("Arial", 11), fg="white", bg="#2c3e50")
lbl_result.pack(pady=5)
btn_reset = tk.Button(root, text="YENİDEN OYNA", command=reset_game, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
btn_reset.pack(pady=10)
root.mainloop()
