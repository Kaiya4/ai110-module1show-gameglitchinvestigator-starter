# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked normal, the UI was normal, but the game logic was broken.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were not working correctly since it wanted me to go lower despite putting 1. The guess counter also does not count correctly. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess 50 when secret is 25 | "Too High, 📉 Go LOWER!"|"Too High, 📈 Go HIGHER!" | Logic |
|Guess 12 (on attempt #2) when secret is 5 | "Too High" (since 12 > 5)|"Too Low" (since "12" < "5" alphabetically) | Caught internally by except TypeError, leading to bad logic.|
| Click "New Game" while on "Easy" mode|Secret resets between 1 and 20 | Secret resets between 1 and 100| None|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Gemini
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Hints being backwards was correct. I verified by putting different numbers below and above the secret to see the output.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). 
The attempt counter is wrong, it showed I had 1 more attempt, but it said I was out of attempt.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
By testing it and using pytests as well. Also, handling edge cases like negative numbers.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest named test_guess_too_high_hint_direction to check if a guess of 60 (when the secret is 50) correctly outputs the '📉 Go LOWER!' hint. It showed me that my function returns a tuple (outcome, message), meaning my test needed to unpack both variables rather than just checking a single string.

- Did AI help you design or understand any tests? How?
Yes, it also helped me debug a ModuleNotFoundError in the terminal by explaining how Python's folder paths work and showing me how to use python -m pytest to successfully run the test suite.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain that Streamlit updates when the code is updated, reflecting the new updated code in real time. Kind of like a visual test.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Asking the AI to give clarifying questions and be more brief in its responses before continuing.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I would use multiple AIs to give me different opinions and see what other AIs catch that the first one didn't. Also to see if there's better ways to make the code more readable.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I don't think it changed how I think of AI generated code because I know it can be good, but it can also cause mistakes, and we are the ones to guide it so it doesn't create mistakes.
