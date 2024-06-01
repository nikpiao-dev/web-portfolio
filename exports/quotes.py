import json

# Quotes from brainyquote.com

quotes_dict = [
    {
     'id': '1',
     'author': 'Confucius', 
     'quotes': 'It does not matter how slowly you go as long as you do not stop.',
     'type': 'Motivational'
    },
    {
     'id': '2',
     'author': 'Nelson Mandela', 
     'quotes': 'It always seems impossible until it\'s done.',
     'type': 'Motivational'
    },
    {
     'id': '3',
     'author': 'Winston Churchill', 
     'quotes': 'If you\'re going through hell, keep going.',
     'type': 'Motivational'
    },
    {
     'id': '4',
     'author': 'Aristotle', 
     'quotes': 'Quality is not an act, it is a habit.',
     'type': 'Motivational'
    },
    {
     'id': '5',
     'author': 'Mark Twain', 
     'quotes': 'The secret of getting ahead is getting started.',
     'type': 'Motivational'
    },
    {
     'id': '6',
     'author': 'Alan Kay', 
     'quotes': 'People who are really serious about software should make their own hardware.',
     'type': 'Technology'
    },
    {
     'id': '7',
     'author': 'Tim Berners-Lee', 
     'quotes': 'You affect the world by what you browse.',
     'type': 'Technology'
    },
    {
     'id': '8',
     'author': 'Oren Etzioni', 
     'quotes': 'AI is neither good nor evil. It\'s a tool. It\'s a technology for us to use.',
     'type': 'Technology'
    },
    {
     'id': '9',
     'author': 'Scott Cook', 
     'quotes': 'We\'re still in the first minutes of the first data of the Internet revolution.',
     'type': 'Technology'
    },
    {
     'id': '10',
     'author': 'Gertrude Stein', 
     'quotes': 'Everybody gets so much information all day long that they lose their common sense.',
     'type': 'Technology'
    },
    {
     'id': '11',
     'author': 'Theodore Roosevelt', 
     'quotes': 'Believe you can and you\'re halfway there.',
     'type': 'Inspirational'
    },
    {
     'id': '12',
     'author': 'Robin Williams', 
     'quotes': 'No matter what people tell you, words and ideas can change the world.',
     'type': 'Inspirational'
    },
    {
     'id': '13',
     'author': 'Lao Tzu', 
     'quotes': 'To the mind that is still, the whole universe surrenders.',
     'type': 'Inspirational'
    },
    {
     'id': '14',
     'author': 'Aesop', 
     'quotes': 'No act of kindness, no matter how small, is ever wasted.',
     'type': 'Inspirational'
    },
    {
     'id': '15',
     'author': 'Rainer Maria Rilke', 
     'quotes': 'The only journey is the one within.',
     'type': 'Inspirational'
    },
    {
     'id': '16',
     'author': 'Oscar Wilde', 
     'quotes': 'Experience is simply the name we give our mistakes.',
     'type': 'Experience'
    },
    {
     'id': '17',
     'author': 'Albert Einstein', 
     'quotes': 'The only source of knowledge is experience',
     'type': 'Experience'
    },
    {
     'id': '18',
     'author': 'Albert Camus', 
     'quotes': 'You can create experience. You must undergo it.',
     'type': 'Experience'
    },
    {
     'id': '19',
     'author': 'Frank McCourt', 
     'quotes': 'The sky is the limit. You never have the same experience twice.',
     'type': 'Experience'
    },
    {
     'id': '20',
     'author': 'Sally Ride', 
     'quotes': 'All adventures, especially into new territory, are scary.',
     'type': 'Experience'
    },
    {
     'id': '21',
     'author': 'Cesare Pavese', 
     'quotes': 'We do not remember days, we remember moments.',
     'type': 'Life'
    },
    {
     'id': '22',
     'author': 'Confucius', 
     'quotes': 'Life is really simple, but we insist on making it complicated.',
     'type': 'Life'
    },
    {
     'id': '23',
     'author': 'Buddha', 
     'quotes': 'Do no dwell in the past, do not dream of the future, concentrate the mind on the present moment.',
     'type': 'Life'
    },
    {
     'id': '24',
     'author': 'Charles Darwin', 
     'quotes': 'A man who dares to waste one hour of time has not discovered the value of life.',
     'type': 'Life'
    },
    {
     'id': '25',
     'author': 'Emily Dickinson', 
     'quotes': 'Find ecstasy in life; the mere sense of living is joy enough.',
     'type': 'Life'
    },
    {
     'id': '26',
     'author': 'John Muir', 
     'quotes': 'In every walk with nature one receives far more than he seeks.',
     'type': 'Wisdom'
    },
    {
     'id': '27',
     'author': 'George Bernard Shaw', 
     'quotes': 'Beware of false knowledge; it is more dangerous than ignorance.',
     'type': 'Wisdom'
    },
    {
     'id': '28',
     'author': 'Franz Kafka', 
     'quotes': 'Start with what is right rather than what is acceptable.',
     'type': 'Wisdom'
    },
    {
     'id': '29',
     'author': 'Sigmund Freud', 
     'quotes': 'Being entirely honest with oneself is a good exercise.',
     'type': 'Wisdom'
    },
    {
     'id': '30',
     'author': 'Joan Rivers', 
     'quotes': 'Yesterday is history, tomorrow is a mystery, today is God\'s gift, that\'s why we call it the present.',
     'type': 'Wisdom'
    },
    {
     'id': '31',
     'author': 'Saint Augustine', 
     'quotes': 'The world is book, and those who do not travel read only a page.',
     'type': 'Travel'
    },
    {
     'id': '32',
     'author': 'Matsuo Basho', 
     'quotes': 'Every day is a journey, and the journey itself is home.',
     'type': 'Travel'
    },
    {
     'id': '33',
     'author': 'Frank Borman', 
     'quotes': 'Exploration is really the essence of the human spirit.',
     'type': 'Travel'
    },
    {
     'id': '34',
     'author': 'Danny Kaye', 
     'quotes': 'To travel is to take a journey into yourself.',
     'type': 'Travel'
    },
    {
     'id': '35',
     'author': 'R. Buckminster Fuller', 
     'quotes': 'How often I found where I should be going only by setting out for somewhere else.',
     'type': 'Travel'
    },
    {
     'id': '36',
     'author': 'Robert Collier', 
     'quotes': 'Success is the sum of small efforts - repeated day in and day out.',
     'type': 'Success'
    },
    {
     'id': '37',
     'author': 'Stephen Hawking', 
     'quotes': 'However difficult life may seem, there is always something you can do and succeed at.',
     'type': 'Success'
    },
    {
     'id': '38',
     'author': 'John F. Kennedy', 
     'quotes': 'Victory has a thousand fathers, but defeat is an orphan.',
     'type': 'Success'
    },
    {
     'id': '39',
     'author': 'John Ruskin', 
     'quotes': 'When love and skill work together, expect a masterpiece.',
     'type': 'Success'
    },
    {
     'id': '40',
     'author': 'Billie Jean King', 
     'quotes': 'A champion is afraid of losing. Everyone else is afraid of winning.',
     'type': 'Success'
    },
    {
     'id': '41',
     'author': 'Paul Klee', 
     'quotes': 'One eye sees, the other feels.',
     'type': 'Art'
    },
    {
     'id': '42',
     'author': 'Henry David Thoreau', 
     'quotes': 'This world is but a canvas to our imagination.',
     'type': 'Art'
    },
    {
     'id': '43',
     'author': 'Stella Adler', 
     'quotes': 'Life beats down and crushes the soul and art reminds you that you have one.',
     'type': 'Art'
    },
    {
     'id': '44',
     'author': 'Unknown', 
     'quotes': 'A picture is worth a thousand words.',
     'type': 'Art'
    },
    {
     'id': '45',
     'author': 'Marcel Proust', 
     'quotes': 'Only through art can we emerge from ourselves and know what another person sees.',
     'type': 'Art'
    },
    {
     'id': '46',
     'author': 'Jim Carrey', 
     'quotes': 'Behind every great man is a woman rolling her eyes.',
     'type': 'Funny'
    },
    {
     'id': '47',
     'author': 'Arthur C. Clarke', 
     'quotes': 'It has yet to be proven that intelligence has any survival value.',
     'type': 'Funny'
    },
    {
     'id': '48',
     'author': 'Karl Barth', 
     'quotes': 'Joy is the simplest form of gratitude.',
     'type': 'Thankful'
    },
    {
     'id': '49',
     'author': 'Martha Graham', 
     'quotes': 'THe body is a sacred garment.',
     'type': 'Health'
    },
    {
     'id': '50',
     'author': 'Carl Sandburg', 
     'quotes': 'Nothing happens unless first we dream.',
     'type': 'Dreams'
    },
]


# Convert and save data to json

json_obj = json.dumps(quotes_dict, indent=4)

# Save quotes data to JSON
with open('quotes.json', 'w') as quote_file:
    quote_file.write(json_obj)

# Print the quotes data
print("Quotes Data: ")
with open('quotes.json', 'r') as doc_file:
    print(doc_file.read())
    