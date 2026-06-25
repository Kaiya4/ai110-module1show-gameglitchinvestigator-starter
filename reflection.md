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


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
