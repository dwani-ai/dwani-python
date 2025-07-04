import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")


def run_asr():
    try:
        result = dwani.ASR.transcribe(file_path="kannada_sample.wav", language="kannada")
        print("ASR Response:", result)

        result = dwani.ASR.transcribe(file_path="english_sample.wav", language="english")
        print("ASR Response:", result)
    except Exception as e:
        print(f"Error in ASR module: {e}")


def display_menu():
    print("\ndwani.ai ASR API Module Selector")
    print("1. ASR")
    print("0. Exit")
    return input("Enter your choice (0-9, default is 1): ").strip()

def main():
    while True:
        choice = display_menu()

        # Default to Chat if no input or invalid input
        if not choice or choice not in {"0", "1"}:
            choice = "1"

        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            run_asr()

if __name__ == "__main__":
    main()