import anthropic
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint

console = Console()
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
    console.print(Panel.fit(
        "[bold magenta]🎵 AI Mood Playlist Curator 🎵[/bold magenta]\n"
        "[cyan]Powered by Claude AI[/cyan]",
        border_style="magenta"
    ))
    
    console.print("\n[yellow]How are you feeling right now?[/yellow] ", end="")
    mood = input()
    
    console.print("\n[cyan]✨ Generating your perfect playlist...[/cyan]\n")
    
    playlist = get_playlist(mood)
    
    console.print(Panel(
        f"[green]{playlist}[/green]",
        title="[bold magenta]🎵 Your Playlist[/bold magenta]",
        border_style="cyan"
    ))

if __name__ == "__main__":
    main()
