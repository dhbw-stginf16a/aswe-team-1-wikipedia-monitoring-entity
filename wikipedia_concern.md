# Concern Definition (wikipedia)

**Concern-Tag :** `wikipedia`

This is all about wikipedia on this day.

## General Parameters

* **event** (dictionary) A specific event
    - deaths
    - births
    - events
    - holidays

## Request Types

### Events for a given date

**Type-Tag:** `event_on_this_day`

#### Request

- **type**: type of information the user wants (can be: all, deaths, births, events, holidays)

#### Response

- **event**: Array as listed in general parameters

#### Example

Request

```json
{
    'type': 'event_on_this_day',
    'payload': {
        'type': 'all',
        'day': 'today'
    }
}
```

Response

```json
[
  {
    "births": [
      [
        "Steven Tyler, American singer-songwriter and actor",
        "Steven Tyler is an American singer, songwriter, musician, actor, and former television music competition judge. He is best known as the lead singer of the Boston-based rock band Aerosmith, in which he also plays the harmonica, piano, and percussion. He is known as the \"Demon of Screamin'\" due to his high screams and his wide vocal range. He is also known for his on-stage acrobatics. During his high-energy performances, Tyler usually dresses in bright, colorful outfits with his trademark scarves hanging from his microphone stand."
      ],
      [
        "Paul Morley, English journalist, producer, and author",
        "Paul Robert Morley is an English music journalist. He wrote for the New Musical Express from 1977 to 1983 and has since written for a wide range of publications. He was a co-founder of the record label ZTT Records and was a member of the synthpop group Art of Noise. He has also been a band manager, promoter and television presenter."
      ],
      [
        "Roger Leger, Canadian ice hockey player (d. 1965)",
        "Joseph Ernest Roger Leger was a professional ice hockey player who played 187 games in the National Hockey League. He was born in L'Annonciation, Quebec. He played with the Montreal Canadiens and New York Rangers."
      ]
    ],
    "deaths": [
      [
        "Sisto Averno, American football player (b. 1925)",
        "Sisto Joseph Averno was an American football guard and linebacker who played in the National Football League for the original Baltimore Colts (1950), the New York Yanks (1951), Dallas Texans (1952) and the Baltimore Colts (1953–1954). He was the final pick of the 1951 NFL Draft, serving as that draft's Mr. Irrelevant. Sisto's college football career also earned him recognition as a member of the Muhlenberg College Athletic Hall of Fame."
      ],
      [
        "Uriah P. Levy, American commander (b. 1792)",
        "Uriah Phillips Levy was a naval officer, real estate investor, and philanthropist. He was a veteran of the War of 1812 and the first Jewish Commodore of the United States Navy. He was instrumental in helping to end the Navy's practice of flogging, and during his half-century-long service prevailed against the antisemitism he faced among some of his fellow naval officers."
      ],
      [
        "Fabrizio Frizzi, Italian television presenter (b. 1958)",
        "Fabrizio Frizzi was an Italian television presenter, voice actor and philanthropist. He often presented a mixture of variety shows, talent shows and game shows across Italy and he was also known as the Italian voice of Woody from the Toy Story franchise."
      ]
    ],
    "events": [
      [
        "Guru Amar Das becomes the Third Sikh guru.",
        "Guru Amar Das was the third of the Ten Gurus of Sikhism and became Sikh Guru on 26 March 1552 at age 73.",
        "The Sikh gurus  established Sikhism over the centuries, beginning in the year 1469. Guru Nanak was the first Guru, and subsequently, each Guru, in succession, was referred to as \"Nanak\", and as \"Light\". All the Gurus themselves also used the name \"Nanak\" while penning down their spiritual verses."
      ],
      [
        "Saudi Arabia begins its military intervention in Yemen , which led to deaths of thousands of people, many of whom were civilians.",
        "Saudi Arabia, officially the Kingdom of Saudi Arabia, is a country in Western Asia constituting the bulk of the Arabian Peninsula. With a land area of approximately 2,150,000 km2 (830,000 sq mi), Saudi Arabia is geographically the largest sovereign state in the Middle East, the second-largest in the Arab world, the fifth-largest in Asia, and the 12th-largest in the world. Saudi Arabia is bordered by Jordan and Iraq to the north, Kuwait to the northeast, Qatar, Bahrain, and the United Arab Emirates to the east, Oman to the southeast and Yemen to the south; it is separated from Israel and Egypt by the Gulf of Aqaba. It is the only nation with both a Red Sea coast and a Persian Gulf coast, and most of its terrain consists of arid desert, lowland and mountains. As of October 2018, the Saudi economy was the largest in the Middle East and the 18th largest in the world. Saudi Arabia also enjoys one of the world's youngest populations; 50% of its 33.4 million people are under 25 years old.",
        "A military intervention was launched by Saudi Arabia in 2015, leading a coalition of nine countries from the Middle East and Africa, in response to calls from the internationally recognized pro-Saudi president of Yemen Abdrabbuh Mansur Hadi for military support after he was ousted by the Houthi movement due to economic and political grievances, and fled to Saudi Arabia. Code-named Operation Decisive Storm, the intervention is said to be in compliance with Article 2(4) of the UN Charter by the international community; this has been contested by some academics. The intervention initially consisted of a bombing campaign on Houthi rebels and later saw a naval blockade and the deployment of ground forces into Yemen. The Saudi-led coalition has attacked the positions of the Houthi militia, and loyalists of the former President of Yemen, Ali Abdullah Saleh, allegedly supported by Iran. The Houthis who had pressured Mansur Hadi for reforms, say that they took power through a popular revolution and are defending Yemen from a western backed invasion. The Saudi-led bombings soon expanded to most of Western Yemen including civilian targets and was followed by UAE-led deployment of ground forces in the South."
      ],
      [
        "The United Kingdom driving test is introduced.",
        "The United Kingdom driving test is a test of competence that UK residents take in order to obtain a full Great Britain or Northern Ireland (car) driving licence or to add additional full entitlements to an existing one. Tests vary depending on the class of vehicle to be driven. In Great Britain it is administered by the Driver and Vehicle Standards Agency (DVSA) and in Northern Ireland by the Driver & Vehicle Agency (DVA)."
      ]
    ],
    "holidays": [
      [
        "Prince Kūhiō Day (Hawaii, United States)",
        "Prince Kūhiō Day is an official holiday in the state of Hawaiʻi in the United States. It is celebrated annually on March 26, to mark the birth of Prince Jonah Kūhiō Kalanianaʻole — heir to the throne of the Kingdom of Hawaiʻi, prince of the House of Kalākaua, and later territorial delegate to the United States Congress. It was established in 1949 by the legislature of the Territory of Hawaii.",
        "Hawaii is the 50th and most recent state to have joined the United States, having received statehood on August 21, 1959. Hawaii is the only U.S. state located in Oceania, the only U.S. state located outside North America, and the only one composed entirely of islands. It is the northernmost island group in Polynesia, occupying most of an archipelago in the central Pacific Ocean.",
        "The United States of America (USA), commonly known as the United States or America, is a country composed of 50 states, a federal district, five major self-governing territories, and various possessions. At 3.8 million square miles, the United States is the world's third or fourth largest country by total area and is slightly smaller than the entire continent of Europe's 3.9 million square miles. With a population of over 327 million people, the U.S. is the third most populous country. The capital is Washington, D.C., and the largest city by population is New York City. Forty-eight states and the capital's federal district are contiguous in North America between Canada and Mexico. The State of Alaska is in the northwest corner of North America, bordered by Canada to the east and across the Bering Strait from Russia to the west. The State of Hawaii is an archipelago in the mid-Pacific Ocean. The U.S. territories are scattered about the Pacific Ocean and the Caribbean Sea, stretching across nine official time zones. The extremely diverse geography, climate, and wildlife of the United States make it one of the world's 17 megadiverse countries."
      ],
      [
        "Independence Day and National Day (Bangladesh), celebrates the declaration of independence from Pakistan in 1971.",
        "The Independence Day of Bangladesh, taking place on 26 March, is a national holiday. It commemorates the country's declaration of independence from Pakistan in the late hours of 25 March 1971,by the undisputed leader of the Nation Sheikh Mujibur Rahman.",
        "Bangladesh, officially the People's Republic of Bangladesh, is a sovereign country in South Asia. It shares land borders with India and Myanmar (Burma). The country's maritime territory in the Bay of Bengal is roughly equal to the size of its land area. Bangladesh is the world's eighth most populous country as well as its most densely-populated, to the exclusion of small island nations and city-states. Dhaka is its capital and largest city, followed by Chittagong, which has the country's largest port. Bangladesh forms the largest and easternmost part of the Bengal region. Bangladeshis include people from a range of ethnic groups and religions. Bengalis, who speak the official Bengali language, make up 98% of the population. The politically dominant Bengali Muslims make the nation the world's third largest Muslim-majority country. Islam is the official religion of Bangladesh.",
        "Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. It is the world’s sixth-most populous country with a population exceeding 212,742,631 people. In area, it is the 33rd-largest country, spanning 881,913 square kilometres. Pakistan has a 1,046-kilometre (650-mile) coastline along the Arabian Sea and Gulf of Oman in the south and is bordered by India to the east, Afghanistan to the west, Iran to the southwest, and China in the far northeast. It is separated narrowly from Tajikistan by Afghanistan's Wakhan Corridor in the northwest, and also shares a maritime border with Oman."
      ],
      [
        "Christian feast days:\nEmmanuel and companions",
        "Saint Emmanuel, was arrested and executed with 42 other martyrs, including Quadratus (Codratus) and Theodocius, in 304 as part of Diocletian's persecution of the Christians. Their feast day is 26 March."
      ]
    ]
  }
]
```

## Subscription Types

### [Type Name]

**Type-Tag:** `[Type Tag]`

#### Message

- **[Parameter1 Name]** ([Parameter1 Type]): [Description]
  - _[Possible Value]_: [Value Description]
- **[Parameter2 Name]**: ([Parameter2 Type]): [Description]

#### Example

```json
[Example for message]
```
