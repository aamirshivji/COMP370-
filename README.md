# COMP370 Final Project 

## Project Phases

### 1. Question definition
Our team has been hired by a media company that wants to understand the news reporting currently happening around the film **The Substance**. They have indicated that they are especially 
concerned with visibility and reception relative to other movies that have come out at a similar time. 
Specifically, they want to know:

*1.What aspect of the movie was the focus (topic) of the article*

*2.How much coverage the movie received relative to other movies that came out at a similar time*

You will conduct this analysis and submit a report discussing your findings.

### 2. Data collection (Set up News API’s one for each of us)

-Searching for Movies released between August 1st and October 31st (We may have to streamline this a little. I am going to test out different time ranges. The shorter the time line, the easier our job will be)

-Limit ourselves to English articles only
-Use unbiased keywords for the search such as Movie, Director names, Actors, box office etc. 

-Seeing as though we will be making comparisons with other movies, we should have some of these in mind: Smile 2, Joker 2, Anora, Alien Romulus etc. However, these are not keywords that 
will be included in the data collection 

*Collect articles on all selected movies, but ensure the specific movie has adequate representation. Aim for a balanced collection across all movies but with enough articles focused on your main movie to allow for deeper analysis.*

-save the 500+ articles to a csv or json. Fields may include: Article title, description, date, movie title referenced, maybe the most important paragraph from the article, source etc. 

#### AAMIR'S DATA COLLECTION
-I retrieved my api key and it is **fef5181e75ea4ee7a86fdb055f3f300b**

### 2. Data annotation (Open Coding)

-We have to randomly sample 200 of the articles from the dataset of 500+
-A headline, subheadline, and maybe the first paragraph? 

*During open coding, include articles about The Substance (may require us to be a little biased) as well as comparison movies.
This way, we’ll capture themes and topics that may be relevant across all movies, ensuring the main movie’s coverage can be compared effectively to others.*

**My understanding of 3-8 topics are simply what these 200 articles focus on when talking about the movies- plot, actors and their performance, cinematography and visuals, the box office,social 
issues or social commentary, the director and production style
I think we need to assign each article to one of these key topics, even if there is overlap in the topics**

**We then need to manually annotate all 500+ articles and assign the selected topics to each article**

When you annotate the full set of 500 articles, you’ll assign topics to articles for all movies, but your specific movie will be highlighted in your analysis.
Track the frequency and type of topics specific to your main movie compared to others, focusing on visibility, unique aspects of coverage, and any notable reception.

### 4. Data analysis (Topic Characterization Using TF-IDF Analysis)

### 5. Interpretation and communication 


## Toolset
NEWS API, Python requests, JSON, Pandas and CSV to manipulate our data set, matplotlib,  Jupyter notebooks for exploration and some visuals, python scriptig
 

## My thought process thus far 
-Since we do nat have any data collected, it is difficult to have a clear vision on the entire project as a whole - especially how we will interpret our findings. I suggest using th weekend to collect some data, and try to annotate it. 

-We can meet next week to work on the analysis together (and probably the annotation as well regarding what topics we each selected)
