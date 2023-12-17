from gtts import gTTS
from pathlib import Path
from art import tprint

import pdfplumber


def pdf_to_mp3(file_path="test.pdf", language="en"):

    print(f"[+] Original file: {Path(file_path).name}")
    print("[+] Processing...")

    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = "".join(pages)
        text = text.replace('\n', '')
        
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")
        return f'[+] {file_name}.mp3 saved successfully'
    else:
        return "File nooooot good!"
    

def main():
    tprint("PDF>TO>MP3", font="bulbhead")
    file_path = input("\nEnter a file's path: ")
    language = input("Change language ru/en: ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == "__main__":
    main()
