import machine
import utime

# LED pin tanımı (örnek olarak GPIO pin 25)
led_pin = machine.Pin(25, machine.Pin.OUT)

# Mors alfabesi
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

# LED için Mors fonksiyonu
def mors_led(text):
    for char in text.upper():
        if char in morse_code:
            morse = morse_code[char]
            for symbol in morse:
                if symbol == '.':
                    led_pin.on()
                    utime.sleep(0.2)  # Nokta (kısa sinyal) için LED'i 0.2 saniye açık tut
                    led_pin.off()
                    utime.sleep(0.2)  # Nokta (kısa sinyal) arasında 0.2 saniye bekle
                elif symbol == '-':
                    led_pin.on()
                    utime.sleep(0.6)  # Çizgi (uzun sinyal) için LED'i 0.6 saniye açık tut
                    led_pin.off()
                    utime.sleep(0.2)  # Çizgi (uzun sinyal) arasında 0.2 saniye bekle
            utime.sleep(0.4)  # Her harf arasında 0.4 saniye bekle
        else:
            # Bilinmeyen karakterleri yok say
            pass

# Klavyeden metin girişi al
def get_input():
    try:
        text = input("Lütfen bir metin girin: ")
        return text
    except KeyboardInterrupt:
        return None

# Ana döngü
while True:
    user_input = get_input()
    if user_input is not None:
        mors_led(user_input)
    else:
        print("\nProgram sonlandırılıyor.")
        break
