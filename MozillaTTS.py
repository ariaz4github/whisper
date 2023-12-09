import requests

def synthesize_text(text, host="localhost", port=5002):
    url = f"http://{host}:{port}/api/tts"
    response = requests.post(url, json={"text": text})

    if response.status_code == 200:
        with open("output.wav", "wb") as file:
            file.write(response.content)
        print("Audio saved as output.wav")
    else:
        print("Error:", response.status_code, response.text)

# Example usage
text_to_synthesize = "Ah, the classic IT team being called back to the office scenario! It sounds like the CEO finally found the one bug they couldn't fix remotely: office chairs that were too comfy at home. But honestly, the real reason they're being called back is because the CEO heard that the servers were feeling lonely without all the IT folks around to talk tech with them. I mean, can you imagine the servers trying to make small talk with the coffee machine? And let''s not forget, they probably just ran out of virtual high-fives and needed to restock on the real thing. "'High-five, you just rebooted the server!'" just doesn''t have the same ring through a webcam, does it? But hey, on the bright side, at least the Wi-Fi will be better in the office... right?"
synthesize_text(text_to_synthesize)
