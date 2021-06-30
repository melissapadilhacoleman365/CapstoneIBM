# CapstoneIBM
Capstone Projekt_ 
As part of the Coursera Capstone, I was involved in multiple sprints. 
The last sprint I used the opportunity to take on the challenge of opening a vegan restaurant in Berlin. 
Please follow the final week sprint to find out more. 


1. Introduction: Final Sprint 


Berlin is a hub for culture, politics, science, and start ups. The city is made of diverse population of around 3 million inhabitants. Berlin is also known in the vegan community as a capital for pushing the culinary boundaries. From vegan curry wurst to donuts, the city provides a lot to offer for vegan tourists and residents. Berlin is even home to high end vegan food with some of the first vegan fine dinning. The city has numerous examples of creativity in the vegan space, including Germany's first zero waste vegan restaurant. It's now estimated that over 800,000 vegans live in the city!
Due to my person connection to Berlin and veganism, I have this topic as a lens for the 'IBM Data Science Professional' certificate. 


2. Problem Description


Question: Where to set-up a new vegan restaurant in Berlin?
Within a city with many hubs, it is important to understand locations that are of interest. Especially for niche clients, such as vegans, the location is important to be located in a high density area where the population resides. At the same time, one wants to avoid being too close to large competitors. Within this research, we will focus on the following areas of importance: 


Demographics; the density of the population within each neighborhood 
Visibility; we are interested in having the location close to other vegan hubs in order to infuse the business int he vegan culture of a neighborhood. 


3. Data Sources
The two main data sources of this project is Wikipedia and Foursquare API. Wikipedia data was included to understand the neighborhoods and populations. This was combined with the Foursquare API to look at the restaurants in the area, including their rating. 


4. Getting and Cleaning the Data
In order to understand these two data sets, the following data was used in two different methods: 
Getting the neighborhood information using Web Scraping (BeautifulSoup)
Getting neighborhood restaurant venues using the Foursquare API
Top Venues per neighbood was retrived and then filtered to include only restaurants 
Top restaurant types per neighborhood
- Alt-Treptow (3rd most popular restaurant type in neighborhood)
- Friedrichshain (2nd most popular restaurant type in neighborhood)
- Fennpfuhl (3rd most popular restaurant type in neighborhood)
-  Mitte (4th Most Common Venue)


5. Visualizing and Understanding the Data


5.1 Berlin map 
The data that was fetched from the Wikipedia page and the Four Square API in order to compare the two sets of data to one another. 
Generate a map of Berlin 
Plot the different neighborhoods on a map
5.2 Chart Population and Density 
The population and density of neighborhood are of biggest interest in order to have a restaurant with high foot traffic and visibility. 


Population of Berlin neighborhoods in 2010
Density of Berlin neighborhoods in 2010


5.3.  Competitor location 
The neighborhoods of the most interest were examined for their top vegan and vegetarian restaurants in the neighborhood. These were then visualized on a map based on location. 


6. Selecting a Location
1. Boroughs that we should consider, based on population count:
Pankow, Tempelhof-Schöneberg, and Mitte.
2. Boroughs that we should consider, based on population density:
Friedrichshain-Kreuzberg, Mitte, and Tempelhof-Schöneberg.
3. Neighborhoods with the highest competiton based on the top 10 results: 
Friedrichshain-Kreuzberg, Moabit, Mitte 



7. Discussion 
When we examine the possibilities based on population and density, Tempelhof-Schöneberg, and Mitte standout as being great locations. Friedrichshain-Kreuzberg is at the top of the list of the poplulation is additionally of interest due to high population density. However, due to the high competition of other vegan restaurants in the area, it could be a risk choice. 
As a result, Tempelhof-Schöneberg, and Mitte are seen as being great choices with lower competiton and high population densities.
