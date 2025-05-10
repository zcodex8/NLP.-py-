# app.py

from flask import Flask, request, jsonify, render_template
from nltk.chat.util import Chat, reflections

# Define your pattern-response pairs here (pairs = [...])
# main.py

pairs = [
    [r"(?i).hello.|.hi.|.hey.",
     ["Hello! Ready to talk football?",
      "Hi there! Ask me anything about football — grounds, players, or rules.",
      "Hey! Want to talk World Cup, leagues, or history?"]],

    [r"(?i).who is the best football player?",
     ["The title of the best football player is often debated, but many consider Lionel Messi and Cristiano Ronaldo as two of the greatest players in football history."]],

    [r"(?i).how many players.*football.",
     ["A football team has 11 players on the field, including one goalkeeper."]],

    [r"(?i).what is offside.*",
     ["Offside is a rule where an attacker is nearer to the opponent's goal line than both the ball and the second-last defender when the ball is played to them."]],

    [r"(?i).what is a penalty kick?",
     ["A penalty kick is awarded when a player commits a foul inside their own penalty area. It’s taken from the penalty spot and only the goalkeeper can defend it."]],

    [r"(?i).who won the 2022 world cup?",
     ["Argentina won the 2022 FIFA World Cup, defeating France in a thrilling final."]],

    [r"(?i).who is messi?",
     ["Lionel Messi is an Argentine footballer widely regarded as one of the greatest players of all time. He played for Barcelona for most of his career before joining Paris Saint-Germain."]],

    [r"(?i).who is cristiano ronaldo?",
     ["Cristiano Ronaldo is a Portuguese footballer known for his incredible athleticism and goal-scoring ability. He has played for top clubs like Manchester United, Real Madrid, and Juventus."]],

    [r"(?i).famous football grounds.",
     ["Famous football grounds include Old Trafford (Manchester United), Camp Nou (Barcelona), Santiago Bernabéu (Real Madrid), and Wembley Stadium (London)."]],

    [r"(?i).where is the fifa world cup held?",
     ["The FIFA World Cup is held every four years and hosted by different countries. The 2022 World Cup was held in Qatar, and the 2026 World Cup will be in the USA, Canada, and Mexico."]],

    [r"(?i).who has the most world cup wins?",
     ["Brazil holds the record for the most FIFA World Cup titles, with five victories (1958, 1962, 1970, 1994, and 2002)."]],

    [r"(?i).who is the most expensive football player?",
     ["As of now, Neymar holds the record for the most expensive football transfer, with a €222 million move from Barcelona to Paris Saint-Germain in 2017."]],

    [r"(?i).what is the premier league?",
     ["The Premier League is the top tier of English football. It features 20 teams, including Manchester United, Liverpool, Arsenal, Chelsea, and more."]],

    [r"(?i).who is the captain of england football team?",
     ["The current captain of the England football team is Harry Kane, who plays for Tottenham Hotspur."]],

    [r"(?i).how long is a football match?",
     ["A standard football match lasts 90 minutes, divided into two 45-minute halves. Additional time (stoppage time) can be added at the end of each half."]],

    [r"(?i).what is a free kick?",
     ["A free kick is awarded when a player commits a foul outside the penalty area. It can either be direct (where a goal can be scored directly) or indirect (where the ball must touch another player before a goal can be scored)."]],

    [r"(?i).who has won the most champions league titles?",
     ["Real Madrid holds the record for the most UEFA Champions League titles, with 14 victories as of 2023."]],

    [r"(?i).who is the top scorer in premier league history?",
     ["As of 2023, the top scorer in Premier League history is]() "]]
    
]
 # (Your full list from earlier)

# Initialize chatbot
chatbot = Chat(pairs, reflections)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message", "")
    bot_reply = chatbot.respond(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
