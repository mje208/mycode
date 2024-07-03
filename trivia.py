#!/usr/bin/env/python3 

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }



a = trivia.get('question')
b = trivia.get('correct_answer')
c = html.unescape(b)

d = trivia.get('incorrect_answers')[0]
e = trivia.get('incorrect_answers')[1]
f = trivia.get('incorrect_answers')[2]
ia = html.unescape(d) 
ia = html.unescape(e) 
ia = html.unescape(f)







print(f'{a} \n {c} \n {ia}')







