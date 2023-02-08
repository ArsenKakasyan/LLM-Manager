'''
The GUI is changed, now it's divided into two blocks in the middle with each text area's on the side. Here's the tasks that I want you to do:

1)Divide GUI into 3 blocks: left (1st) block should be narrow (25% of screen) and contain text area for user input and send to gpt button below (not thick). middle (2nd) block should be wide (50% of screen) and contain 3 main parts: text area for json display on top, text area for user feedback and save feedback button on the bottom (not thick). right (3rd) block should be narrow (25% of screen) and just display response from gpt.

Okay, GUI done. Second task:

2) User also shouldn't be able to save one response multiple times and flood JSON file. Let's add additional identity attribute (hash) to the JSON object structure and check if there was the object with the exact code (maybe we should write another function for this). Here's the new structure of JSON:

"response_id": n,
"initial_prompt": "",
"response_text": "",
"response_hash": "",
"response_edit": "",
"updated_prompt": ""

The current state of code (mention only those places in code in your response that require changes):

3) Finally, as you've seen there's It should also now save initial prompt into separate new line. Primarily, it should concatenate response edit with response text in order to make updated_prompt. Here's the current code you need to refactor:

Plan:
Part 1: API Connection and Input/Output

    Connect to OpenAI API using the text-davinci-003 model [done]
    Receive user input and send it to the API [done]
    Receive the API response and save it into JSON file [done]

Part 2: Memory and User Interaction

    Store API responses in JSON [done]
    Show API response to the user and ask for feedback [done]
    Receive user feedback and add it to the API response [done]
    Pass the edited API response back to Module 1
    Maintain a history of all API responses and user feedback
'''
import hashlib
import json
import openai
import os
import tkinter as tk
from tkinter import filedialog, Menu

class OPENAI_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("OPENAI GUI")
        self.master.geometry("1600x900")
        self.master.resizable(True, True)
        self.master.configure(bg="black")

        # Create menu bar
        menu = Menu(master)
        master.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="JSON", command=self.select_json)
        
        key_menu = Menu(menu)
        menu.add_cascade(label="Key", menu=key_menu)
        key_menu.add_command(label="ENV", command=self.set_api_key)

        # Left frame
        self.left_frame = tk.Frame(self.master, bg="black", width=320)
        self.left_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        self.user_input = tk.Text(self.left_frame, height=10, width=40, bg="black", fg="white", font=("Courier", 12, "bold"))
        self.user_input.pack(expand=True, fill="both")
        self.user_input.insert("1.0", "Enter your query here...")

        def clear_user_input_placeholder(event):
            if self.user_input.get("1.0", "end-1c") == "Enter your query here...":
                self.user_input.delete("1.0", "end")

        self.user_input.bind("<FocusIn>", clear_user_input_placeholder)


        self.send_to_gpt_button = tk.Button(self.left_frame, text="Send to GPT-3", bg="#1565C0", fg="#FBFBFB", font=("Helvetica", 20, "bold"), command=self.send_to_gpt)
        self.send_to_gpt_button.pack(side="bottom", pady=10)

        # Right frame
        self.right_frame = tk.Frame(self.master, bg="black", width=320)
        self.right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        self.response_from_gpt = tk.Text(self.right_frame, height=10, width=40, bg="black", fg="white", font=("Courier", 12, "bold"))
        self.response_from_gpt.pack(expand=True, fill="both")
        self.response_from_gpt.insert("1.0", "Response from GPT-3 will appear here...")

        # Middle frame
        self.middle_frame = tk.Frame(self.master, bg="black", width=640, height=500)
        self.middle_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        # Text area for JSON display
        self.json_display = tk.Text(self.middle_frame, height=10, width=40, bg="black", fg="white", font=("Courier", 12, "bold"))
        self.json_display.pack(side="top", expand=True, fill="both")
        self.json_display.insert("1.0", "JSON data will be displayed here...")

        # Text area for user feedback and save feedback button
        self.feedback_input_frame = tk.Frame(self.middle_frame, bg="black")
        self.feedback_input_frame.pack(side="bottom", expand=True, fill="both", pady=10)


        self.feedback_input = tk.Entry(self.feedback_input_frame, width=50, bg="black", fg="white", font=("Courier", 12, "bold"))
        self.feedback_input.pack(side="top", expand=True, fill="both")
        self.feedback_input.insert(0, "Enter your feedback here...")

        def clear_feedback_input_placeholder(event):
            if self.feedback_input.get() == "Enter your feedback here...":
                self.feedback_input.delete(0, tk.END)

        self.feedback_input.bind("<FocusIn>", clear_feedback_input_placeholder)

        self.save_feedback_button = tk.Button(self.feedback_input_frame, text="Save Feedback", bg="#1565C0", fg="#FBFBFB", font=("Helvetica", 20, "bold"), command=self.save_feedback)
        self.save_feedback_button.pack(side="left", pady=10)

        self.clear_json_repetitive_hashes_button = tk.Button(self.feedback_input_frame, text="Clear JSON", bg="#FF0000", fg="#FBFBFB", font=("Helvetica", 20, "bold"), command=self.clear_json_repetitive_hashes)
        self.clear_json_repetitive_hashes_button.pack(side="right", pady=10)

    def send_to_gpt(self):
        user_input = self.user_input.get("1.0", "end-1c")
        openai.api_key = os.getenv("KEY") 

        if user_input:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{user_input}",
                temperature=0.5,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            response_text = response["choices"][0]["text"]
            self.response_from_gpt.delete("1.0", tk.END)
            self.response_from_gpt.insert(tk.END, f"Model used: text-davinci-003\n\n{response_text}")

    def save_feedback(self):
        feedback = self.feedback_input.get()
        response_processor = ResponseProcessor((self.response_from_gpt.get("1.0", "end-1c"), feedback))
        response_processor.process_response_from_gpt()

    def clear_json_repetitive_hashes(self):
        response_processor = ResponseProcessor((None, None))
        response_processor.clear_repetitive_hashes()

    def set_api_key(self):
        api_key = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        # Add the selected file as an environment variable here
    
    def select_json(self):
        json_file = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("JSON files", "*.json"), ("all files", "*.*")))
        # Open and process the selected JSON file here



class ResponseProcessor:

    def __init__(self, response_and_feedback, file_path = "response.json"):
        self.response_and_feedback = response_and_feedback
        self.file_path = file_path
        self.responses = []

    def _get_max_response_id(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.responses = data
        except json.decoder.JSONDecodeError:
            data = []
            with open(self.file_path, 'w') as f:
                json.dump(data, f)
        if not data:
            return 0
        return max(data, key=lambda x: x['response_id'])['response_id']

    def _save_response_to_file(self):
        with open("response.json", "w") as f:
            json.dump(self.responses, f, indent=4)

    def process_response_from_gpt(self):
        response_hash = hashlib.sha256(str(self.response_and_feedback).encode()).hexdigest()
        
        for response in self.responses:
            if response["response_hash"] == response_hash:
                return
                
        response_id = self._get_max_response_id() + 1
        data = {
            "response_id": response_id,
            "response_text": self.response_and_feedback[0],
            "response_hash": response_hash,
            "response_edit": self.response_and_feedback[1]
        }
        self.responses.append(data)
        self._save_response_to_file()

    def clear_repetitive_hashes(self):
        try:
            with open(self.file_path, 'r') as f:
                self.responses = json.load(f)
        except json.decoder.JSONDecodeError:
            self.responses = []

        hashes = []
        filtered_responses = []
        response_id = 0
        for response in self.responses:
            response_hash = response["response_hash"]
            if response_hash not in hashes:
                hashes.append(response_hash)
                response["response_id"] = response_id
                filtered_responses.append(response)
                response_id += 1

        self.responses = filtered_responses
        self._save_response_to_file()



def run_module_1():
    root = tk.Tk()
    app = OPENAI_GUI(root)
    # mainmenu = Menu(root) 
    # root.config(menu=mainmenu)
    # mainmenu.add_command(label='Файл')
    # mainmenu.add_command(label='Справка')
    root.mainloop()
    


if __name__ == '__main__':
    run_module_1()