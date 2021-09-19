from GPTJ.gptj_api import Completion
context = "This emulates a text message conversation."
examples = {
    "What do you think I should do?": "Mmm… I’d just try to forget about it if I were you",
    "Can I bring anything?": "Oh, don’t worry about it. I have everything covered.",
    "Oh hey, I didn’t see you there. Did you already get a table?": "Yeah, right over here.",
    "Me too. So, what’s going on?": "Oh, not much. You?"}
context_setting = Completion(context, examples)
prompt ="How has your week been?"
User = "Student"
Bot = "Calculator"
max_tokens = 50
temperature = 0.9
top_probability = 1.0

while(True):
    past_response = ""
    prompt = past_response + input();
    response = context_setting.completion(prompt,
              user=User,
              bot=Bot,
              max_tokens=max_tokens,
              temperature=temperature,
              top_p=top_probability)
    past_response = response
    print(response)
