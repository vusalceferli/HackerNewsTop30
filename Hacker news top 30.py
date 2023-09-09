import requests
import tkinter as tk
from tkinter import scrolledtext


def get_top_news():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

    try:
        response = requests.get(url)
        response.raise_for_status()
        top_story_ids = response.json()[:30]

        news_text = ""
        for story_id in top_story_ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
            story_response = requests.get(story_url)
            story_data = story_response.json()

            title = story_data.get("title")
            url = story_data.get("url")
            score = story_data.get("score")

            news_text += f"Başlık: {title}\nURL: {url}\nSkor: {score}\n\n"

        news_window = tk.Toplevel(window)
        news_window.title("En Üstte Çıkan 30 Haber")
        news_textbox = scrolledtext.ScrolledText(news_window, wrap=tk.WORD)
        news_textbox.insert(tk.END, news_text)
        news_textbox.pack(expand=True, fill='both')

    except Exception as e:
        error_message = f"Haberleri alma sırasında bir hata oluştu: {str(e)}"
        messagebox.showerror("Hata", error_message)


window = tk.Tk()
window.title("Hacker News En Üstte Çıkan 30 Haber")
window.config(padx=30,pady=30)

get_news_button = tk.Button(window, text="Haberleri Getir", command=get_top_news)
get_news_button.pack(pady=10)

window.mainloop()