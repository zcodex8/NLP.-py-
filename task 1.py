from nltk.chat.util import Chat, reflections

pairs = [
    # 1. Greetings
    [r".*\b(hello|hi|hey)\b.*", 
        ["Hello there! Ready to talk football?", 
         "Hey! How can I help you with football today?", 
         "Hi! Ask me anything about soccer."]],
    [r".*\bgood (morning|afternoon|evening)\b.*", 
        ["Good %1! What football topic are you interested in?", 
         "%1! How can I assist with your football question?"]],
    # 2. Football rules: Offside
    [r".*\boffside\b.*", 
        ["Offside means a player is in the opponent’s half and closer to the goal than both the ball and the second-last defender when the ball is played:contentReference[oaicite:1]{index=1}. If such a player then gets involved in play, the referee will stop the match and award an indirect free kick to the defenders.",
         "Being offside is not a foul by itself, but if an offside player touches the ball or interferes with an opponent, the referee will call offside. In short: don’t stand behind the last defender when a teammate plays the ball:contentReference[oaicite:2]{index=2}."]],
    # 2. Football rules: Fouls
    [r".*\bfoul\b.*", 
        ["A foul is an unfair act by a player that violates the laws and interferes with active play:contentReference[oaicite:3]{index=3}. When a foul occurs, the referee blows the whistle and usually awards a free kick or penalty to the other team:contentReference[oaicite:4]{index=4}.",
         "Fouls include things like kicking, tripping, or pushing an opponent. If a player commits a foul, the game is stopped and a free kick (or penalty if in the box) is given to the other side."]],
    # 2. Football rules: Match time
    [r".*\b(90 minutes|duration|length of (a )?match|half-time)\b.*", 
        ["A standard soccer match lasts 90 minutes, split into two 45-minute halves:contentReference[oaicite:5]{index=5}, with about 15 minutes for half-time. The referee may add a few minutes of stoppage time at the end of each half for injuries or delays.",
         "Professional matches are 90 minutes long (2×45). There is a halftime break in between, and the referee can add extra (injury) time after each half:contentReference[oaicite:6]{index=6}."]],
    # 3. Player info: Lionel Messi
    [r".*\bMessi\b.*", 
        ["Lionel Messi is an Argentine forward widely regarded as one of the greatest ever.  He won the FIFA World Cup with Argentina in 2022:contentReference[oaicite:7]{index=7} and scored record goals for Barcelona.",
         "Messi is a star at PSG (and formerly Barcelona). He has won many Ballon d'Or awards and was a key player in Argentina’s 2022 World Cup victory:contentReference[oaicite:8]{index=8}." ]],
    # 3. Player info: Cristiano Ronaldo
    [r".*\bRonaldo\b.*", 
        ["Cristiano Ronaldo is a Portuguese striker known for his scoring ability. He holds the men’s international goals record (136 for Portugal):contentReference[oaicite:9]{index=9} and has won multiple Champions Leagues and a Euro title.",
         "Ronaldo is a superstar who has played for Sporting Lisbon, Manchester United, Real Madrid, Juventus, and now Al-Nassr.  He’s scored over 800 goals in his career and has the world record 136 international goals:contentReference[oaicite:10]{index=10}." ]],
    # 3. Player info: Top scorers
    [r".*\b(top goal|top scorer|highest scorer)\b.*", 
        ["The leading international goal scorers are Cristiano Ronaldo (136 goals) and Lionel Messi (112 goals) as of 2025:contentReference[oaicite:11]{index=11}.  Ali Daei (Iran) has 109.",
         "As of now, Ronaldo (136) and Messi (112) are the top two all-time international scorers:contentReference[oaicite:12]{index=12}. Others like Pele (77 goals) are legendary but below those marks."]],
    # 4. Tournaments: World Cup
    [r".*\bWorld Cup\b.*", 
        ["The FIFA World Cup is the top tournament for national teams, held every 4 years:contentReference[oaicite:13]{index=13}. Brazil has won it a record five times:contentReference[oaicite:14]{index=14}, and Argentina is the current champion (2022):contentReference[oaicite:15]{index=15}.",
         "World Cup finals take place every four years. For example, Argentina won in 2022:contentReference[oaicite:16]{index=16}.  Only teams from Europe and South America have ever won it:contentReference[oaicite:17]{index=17}." ]],
    # 4. Tournaments: Champions League
    [r".*\bChampions League\b.*", 
        ["The UEFA Champions League is an annual club tournament among top European teams. Real Madrid has won it 14 times (a record):contentReference[oaicite:18]{index=18}, more than any other club.",
         "Champions League final is held in late May/early June each year.  In 2023 Manchester City won the title:contentReference[oaicite:19]{index=19}." ]],
    # 4. Tournaments: Premier League
    [r".*\bPremier League\b.*", 
        ["The Premier League is England’s top professional league (20 teams):contentReference[oaicite:20]{index=20}. It runs from August to May.  Manchester United has won it 13 times (more than any other club):contentReference[oaicite:21]{index=21}.",
         "Since 1992, seven different clubs have won the Premier League:contentReference[oaicite:22]{index=22}.  The current champions (2024) are Manchester City, but Man U has the most titles (13):contentReference[oaicite:23]{index=23}." ]],
    # 5. Stadiums (insert relevant team names for context)
    [r".*\b(Wembley|England national stadium)\b.*", 
        ["Wembley Stadium in London is England’s national football stadium, with a capacity of 90,000 spectators:contentReference[oaicite:24]{index=24}. It hosts the FA Cup final and England internationals.",
         "Wembley is famous for its giant arch and 90k capacity:contentReference[oaicite:25]{index=25}. Major finals (like the Champions League or Euro final) are often played there." ]],
    [r".*\b(Camp Nou|Barcelona stadium)\b.*", 
        ["Camp Nou is FC Barcelona’s home ground, and with a capacity around 105,000 it is the largest stadium in Europe:contentReference[oaicite:26]{index=26}. Its record attendance was 120,000 in 1986.",
         "Barcelona’s Camp Nou holds over 100,000 fans:contentReference[oaicite:27]{index=27}. It’s undergoing renovation to expand even more, which would make it Europe’s biggest stadium." ]],
    [r".*\bOld Trafford\b.*", 
        ["Old Trafford in Manchester is the home of Manchester United. It seats about 74,000 (making it the largest club stadium in the UK):contentReference[oaicite:28]{index=28}.",
         "Known as 'The Theatre of Dreams', Old Trafford holds ~74,000 fans:contentReference[oaicite:29]{index=29}. It opened in 1910 and is Manchester United’s historic home." ]],
    [r".*\bstadium\b.*", 
        ["Famous football stadiums include Wembley (London, 90k):contentReference[oaicite:30]{index=30}, Camp Nou (Barcelona, 105k):contentReference[oaicite:31]{index=31}, and Old Trafford (Manchester, 74k):contentReference[oaicite:32]{index=32}.",
         "Some iconic stadiums: Wembley (England, 90k):contentReference[oaicite:33]{index=33}, Maracanã (Brazil, ~78k), Camp Nou (Spain, 105k):contentReference[oaicite:34]{index=34}, and Old Trafford (England, 74k):contentReference[oaicite:35]{index=35}."]],
    # 6. Fun facts about football
    [r".*\b(fun fact|did you know|interesting)\b.*", 
        ["Fun fact: The 2022 World Cup final was watched by over 5 billion people globally:contentReference[oaicite:36]{index=36}, making soccer the most popular sport worldwide.",
         "Did you know? Real Madrid has won 14 Champions League titles (more than any other club):contentReference[oaicite:37]{index=37}.  Another cool stat: Ronaldo has scored 136 international goals (a record):contentReference[oaicite:38]{index=38}." ]],
    # 7. Club information: Barcelona
    [r".*\bBarcelona\b.*", 
        ["FC Barcelona is one of Spain’s most successful clubs. They have won La Liga 27 times:contentReference[oaicite:39]{index=39} and five Champions League titles. They play at Camp Nou (~105k seats):contentReference[oaicite:40]{index=40}.",
         "Barcelona, based in Catalonia, is famous for its 'tiki-taka' style.  Players like Messi and Xavi starred there. They’ve won the Champions League five times and the domestic league 27 times:contentReference[oaicite:41]{index=41}." ]],
    # 7. Club information: Manchester United
    [r".*\b(Manchester United|Man United)\b.*", 
        ["Manchester United is a top English club. They’ve won 20 English league titles in total (13 of those were since 1992 in the Premier League):contentReference[oaicite:42]{index=42}.",
         "Man U plays at Old Trafford (74k seats):contentReference[oaicite:43]{index=43}. They won the Champions League in 1968, 1999 (treble year), and 2008." ]],
    # 8. Equipment: Ball and goal
    [r".*\b(ball size|size (5 )?ball|football circumference)\b.*", 
        ["A standard size-5 football (used by adults) has a circumference of about 68–70 cm and weighs 410–450 grams.  It must be spherical and follow FIFA Law 2.",
         "Soccer balls are roughly 70 cm around (size 5).  They weigh around 425 g when inflated to regulations."]],
    [r".*\b(goalpost|goal size)\b.*", 
        ["The regulation goal is 7.32 meters wide (distance between posts) and 2.44 meters high (bottom to crossbar).  This is the standard for all full-size matches.",
         "Soccer goalposts are 7.32 m apart and 2.44 m high.  The net is attached behind them to catch the ball."]],
    # 9. Match schedules or results (static answers)
    [r".*\bChampions League final\b.*", 
        ["The next UEFA Champions League final is scheduled for June 1, 2025 in London:contentReference[oaicite:44]{index=44}.", 
         "Champions League finals are usually at the end of May or early June; for example, the 2025 final is on June 1, 2025:contentReference[oaicite:45]{index=45}." ]],
    [r".*\b2026 World Cup\b.*", 
        ["The 2026 FIFA World Cup will be held in USA/Canada/Mexico from June 11 to July 19, 2026:contentReference[oaicite:46]{index=46}.", 
         "The 2026 World Cup runs from June 11 to July 19, 2026:contentReference[oaicite:47]{index=47}, with 48 teams (expanded format)."]],
    [r".*\bWorld Cup 2022\b.*", 
        ["In 2022, Argentina won the World Cup by beating France on penalties:contentReference[oaicite:48]{index=48}.  It was Argentina’s third title and Messi’s first World Cup victory:contentReference[oaicite:49]{index=49}.",
         "Argentina defeated France in the 2022 World Cup final (3-3, 4-2 on penalties):contentReference[oaicite:50]{index=50}, earning their third World Cup." ]],
    # 10. Farewells
    [r".*\b(bye|goodbye|see you|cya|later)\b.*", 
        ["Goodbye! Feel free to ask more about football anytime.", 
         "See you! Come back if you have more soccer questions.", 
         "Bye! Hope I was able to help with your football queries."]]
]

# Initialize the chatbot with these pairs and default reflections
chatbot = Chat(pairs, reflections)
