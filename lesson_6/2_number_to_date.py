seconds = int(input("Enter a number of seconds: "))

days = seconds // 86400
hrs = (seconds - days * 86400) // 3600
mins = (seconds - days * 86400 - hrs * 3600) // 60
secs = (seconds - days * 86400 - hrs * 3600 - mins * 60) % 60

day_word = None

if days == 0 or 11 <= days % 100 <= 19 :
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif days % 10 < 5:
    day_word = "дні"
elif days % 10 >= 5:
    day_word = "днів"

print(f"{days} {day_word}, {str(hrs).zfill(2)}:{str(mins).zfill(2)}:{str(secs).zfill(2)}")
