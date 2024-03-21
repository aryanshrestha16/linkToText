# linkToText
This python script utilizes OpenAI API and YouTubeTranscriptApi to summarize a YouTube video link into text.

## Programming Language used:
Python 3.12.1

## APIs used: 
OpenAI API & YouTubeTranscriptApi

## Directions:

### Install the OpenAI Python library
```
pip install --upgrade openai
```
### Set up your (OpenAI API key) [https://platform.openai.com/docs/quickstart?context=python]
#### MacOS
1. Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
2. Edit Bash Profile: Use the command nano ~/.bash_profile or nano ~/.zshrc (for newer MacOS versions) to open the profile file in a text editor.
3. Add Environment Variable: In the editor, add the line below, replacing your-api-key-here with your actual API key:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```
4. Save and Exit: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.
5. Load Your Profile: Use the command source ~/.bash_profile or source ~/.zshrc to load the updated profile.
6. Verification: Verify the setup by typing echo $OPENAI_API_KEY in the terminal. It should display your API key.

### Set up Youtube-transcript-API (Developed by @jdepoix) [https://github.com/jdepoix/youtube-transcript-api]
```
pip install youtube-transcript-api
```
