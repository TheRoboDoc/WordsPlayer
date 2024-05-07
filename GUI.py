import tkinter as tk
import wordsfinder
from tkinter import font as tkfont
import darkdetect

theme = darkdetect.isDark() and 'dark' or 'light'


def run_window() -> None:
    def run_action() -> None:
        try:
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)

            feedback_label.config(fg='green')

            user_input: str = letters_entry.get()

            length: int = int(length_entry.get())

            _found_words: set[str] = wordsfinder.find_words(user_input, length)

            if not _found_words:
                raise Exception("No words found matching the criteria.")

            found_words_sorted: list[str] = sorted(_found_words, key=len)

            for _word in found_words_sorted:
                output_text.insert(tk.END, _word + "\n")

            output_text.config(state=tk.DISABLED)

            feedback_label.config(text=f"{len(found_words_sorted)} words found successfully!", fg='green')

        except ValueError:
            feedback_label.config(text="Please enter a valid number for length.", fg='red')

            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.config(state=tk.DISABLED)

        except Exception as e:
            feedback_label.config(text=str(e), fg='red')

            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.config(state=tk.DISABLED)

    def quit_action() -> None:
        root.destroy()

    def toggle_theme() -> None:
        global theme

        theme = 'dark' if theme == 'light' else 'light'

        set_theme()

    def set_theme() -> None:
        global theme

        colors: dict[theme] = {
            'dark': {
                "background": "#333333",
                "foreground": "#ffffff",
                "button_background": "#555555",
                "button_foreground": "#ffffff",
                "text_bg": "#555555",
                "text_fg": "#ffffff"
            },
            'light': {
                "background": "#ffffff",
                "foreground": "#000000",
                "button_background": "#eeeeee",
                "button_foreground": "#000000",
                "text_bg": "#ffffff",
                "text_fg": "#000000"
            }
        }[theme]

        root.configure(background=colors['background'])

        top_frame.config(background=colors['background'])
        toggle_button.config(background=colors['button_background'], foreground=colors['button_foreground'])
        banner_label.config(background=colors['background'], foreground=colors['foreground'])

        input_frame.config(background=colors['background'])
        letters_label.config(background=colors['background'], foreground=colors['foreground'])
        letters_entry.config(background=colors['text_bg'], foreground=colors['text_fg'],
                             insertbackground=colors['foreground'])

        length_label.config(background=colors['background'], foreground=colors['foreground'])
        length_entry.config(background=colors['text_bg'], foreground=colors['text_fg'],
                            insertbackground=colors['foreground'])

        output_frame.config(background=colors['background'])
        output_text.config(background=colors['text_bg'], foreground=colors['text_fg'])
        feedback_label.config(background=colors['background'], foreground=colors['foreground'])

        button_frame.config(background=colors['background'])
        run_button.config(background=colors['button_background'], foreground=colors['button_foreground'])
        quit_button.config(background=colors['button_background'], foreground=colors['button_foreground'])

    root: tk = tk.Tk()
    root.title("Words Processor")
    root.geometry("440x600")
    root.minsize(220, 580)
    root.maxsize(440, 600)

    # Define custom font
    headerFont: tkfont = tkfont.Font(family="Helvetica", size=28)
    customFont: tkfont = tkfont.Font(family="Helvetica", size=14)
    smallFont: tkfont = tkfont.Font(family="Helvetica", size=10)

    top_frame: tk.Frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    toggle_button: tk.Button = tk.Button(top_frame, text="Toggle Theme", font=smallFont, command=toggle_theme, width=12)
    toggle_button.pack(side=tk.LEFT, padx=10, pady=10)

    banner_label: tk.Label = tk.Label(top_frame, text="Words Processor", font=headerFont)
    banner_label.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

    input_frame: tk.Frame = tk.Frame(root, padx=20, pady=20)
    input_frame.pack()

    letters_label: tk.Label = tk.Label(input_frame, text="Letters:", font=customFont)
    letters_label.pack()
    letters_entry: tk.Entry = tk.Entry(input_frame, font=customFont, width=30)
    letters_entry.pack()

    length_label: tk.Label = tk.Label(input_frame, text="Length:", font=customFont)
    length_label.pack()
    length_entry: tk.Entry = tk.Entry(input_frame, font=customFont, width=30)
    length_entry.pack()

    feedback_label: tk.Label = tk.Label(root, text="", font=customFont)
    feedback_label.pack()

    output_frame: tk.Frame = tk.Frame(root, padx=20, pady=20)
    output_frame.pack(fill=tk.BOTH, expand=True)

    output_text: tk.Text = tk.Text(output_frame, height=10, width=50, font=customFont)
    output_text.config(state=tk.DISABLED)

    scrollbar: tk.Scrollbar = tk.Scrollbar(output_frame, command=output_text.yview)

    output_text.configure(yscrollcommand=scrollbar.set)
    output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    button_frame: tk.Frame = tk.Frame(root, padx=20, pady=20)
    button_frame.pack()

    run_button: tk.Button = tk.Button(button_frame, text="Run", font=customFont, command=run_action, width=10)
    run_button.pack(side=tk.LEFT, padx=10)

    quit_button: tk.Button = tk.Button(button_frame, text="Quit", font=customFont, command=quit_action, width=10)
    quit_button.pack(side=tk.RIGHT, padx=10)

    set_theme()

    root.mainloop()
