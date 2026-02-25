import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def get_playlist(mood):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a music expert and mood analyst. 
                Based on this mood: '{mood}'
                
                Please suggest a playlist with:
                1. 5 song recommendations with artist names
                2. The genre that fits this mood
                3. A short explanation of why this playlist fits the mood
                
                Format it nicely and clearly."""
            }
        ]
    )
    return message.content[0].text

def main():
    print("🎵 AI Mood Playlist Curator 🎵")
    print("--------------------------------")
    mood = input("How are you feeling right now? ")
    print("\nGenerating your perfect playlist...\n")
    playlist = get_playlist(mood)
    print(playlist)

if __name__ == "__main__":
    main()
