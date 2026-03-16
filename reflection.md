# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It didn't work when guessing the number 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The hints were incorrect.
  - The Number of attempts were incorrect

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  - I used CoPilot Agent Mode.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  - The AI suggested the code to correct the two selected bugs of the incorrect hints and attempt counter.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  
  - When running the test the we had an error when running the test was written with the wrong directory while reviewing the code I was able to resolve the directory issue.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  - I played the game by running the app and wrote tests that passed as well.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

    - Tested by using up all my attempts and seeing we had 7 attempts and the attempt counter was fixed.

- Did AI help you design or understand any tests? How?

  - AI was helpful designing the tests and showed me the purpose of the tests and the design as well.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  - The Secret number didn't change with my testing.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  - Its a simple game which allows you to play a guessing game with hints and 7 attempts.

- What change did you make that finally gave the game a stable secret number?

  - The secret number didn't change with my testing.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

    - Giving the AI context makes work much simpler it understands the issues and fixes are much faster.

- What is one thing you would do differently next time you work with AI on a coding task?

  - Be more specific of the outcome I want whether I want it to code or just explain the issue being specific is necessary.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  - AI is a helpful tool, if you understand where to go AI is the horse that gets you there faster.