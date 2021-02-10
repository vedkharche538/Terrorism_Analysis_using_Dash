# Terrorism_Analysis_using_Dash
### Analysis terrorism in India and predict how it will in near future 
Introduction:-
1.	About the project 
         For this project we using a Python with Dash framework which use many other laybaries  like pandas,plotly,webbrowser and displaying data visualization of global terrorism using a dataset of approximately 1,90,000 records.In project we use Two types of visualization,first is Map tool  which given the World Map and India Specific Map and second is Chart tool which given Area chart for world data and also for only India data which shown the number of incident happend to every year.In world Map UI ,There are seven dropdown UI each of which plays the function of a filter for the world map so Dropdown UIs are:
1.	Month
2.	Date
3.	Region
4.	Country
5.	Province/State
6.	City
7.	Attack-Type 
After creating  this seven UI we use filtering on that UI using the callbacks concept like without select the month can not show the data of date and same for region and country,first you have to select Region then countries of that particular selected region.similarly for state and city.create the range slider for year so when we change in the slider according that map also change .now we create the legend of attack type which showen side of map and given different color to the attack type.
For the India Specific Map we have disable value of region and country so, The Region is South Asia and the country is India. For other UI like month,date apply filtering same as in world  map. The legend is the same as the World Map.
Next we have Chart Tool which  has two type,first is  world chart tool and second is India chart tool.Chart Tool UI contain 
1.	Incidents Grouped By- Region(by default)
2.	Search Box Filter
3.	Area Chart
For the world chart tool we have one dropdown which contains multiple group regions,attack type,weapon type,nationality ,organization, country attack and using search tool searches for the selected dropdown filter's content, whether it is contained in it or not. If it yields results then they are shown, if not the original legend is shown that has been selected from the dropdown.
India Area Chart has two decibel values region  and country as region  'South Asia' selected and for country 'India'. If the user searches for something then it is shown that graph otherwise it shows the region's graph.


My  project work and Implementation
Before starting the project I read the user expectations for project and then started my work on it..First step is i need to convert text file to csv file,for that write the code in spyder and using pandas library,which is used for data analysis convert text file into csv file.
After creating csv file now I starting the coding other expectations for project and for that use the dash framework which is building web application and  import all the necessary libraries in code which require for complete the project.UI Expectation for taking input from the user and UI Expectation for the output,so for that import dash_html_component as html for use html in python  and import dash_core_component as dcc for create dropdowns,graphs,range slider and Tabs.use the define function as def for different functionality.
Create a define function(def) for loading the data which is required for making a webpage. then create another def for html at which i make tabs, dropdowns,graphs,range slider and search buttons the same for others also.in fig you show that i use global which is used for globalize the data
 In project code first in def define data and than make the seven dropdown for different datas like month,days,region,country,state,attack type.in next step filter the all the data using callbacks for that use library from dependencies import Input,Output which is help to filter data when we select the month than date is shown in dropdown other wise no data found for date  same for region and country.next we want to select multiple value in dropdown so we just use multi=True in dropdown.upload the world map using data we again use the callbacks method.than create legend for attack type.then create the two tabs map tool and chart tool which have two subtabs world map tool and indian map tool.
 For map tool UI first we create world map tool which connected with dropdown when i change 
The value according to that my world map also change and in India map tool we have two disebal value for region is South Asia and for country  is India which change also shown in world map when i selected india map tool this is fulfill by using callbacks and when i change year slider according to that world map also given changes.
or chart too UI we create world data graph with all year in data file.for that create dropdown which have different group like region,attack type,organization,country attack,weapon attack,type of nationality and for selected group we search particular data from search input which given particular graph of that search data and also change the year from slider which given changeable graph of  year. When selecting India tool the region and country have default value which is south asia and India and it is only given the India graph and south asia graph as output here also we change year using year slider which gives implementation on graph.
And lastly, using css  makes the web page more attractive.for all this implementation without forsk coding school not possible i done my project because of their daily encouragement and support. 

Results
1.	Dropdown and range slider created
 
2.	Select the value from dropdown for Month,Date,Region,Country,State,Attack type after filter the data

3.Upload world map with attack type legend.
 
4. World Map change with selected data with multiple values or only India data map with disble value of region and country India.
  
5.  Upload the world graph and than graph with search value 

6. India graph with default region and country value 
 
7. Different group type graphs and changes in slider year show according to that graph also change.

Conclusion 
Finally I complete my project with the coding and necessary thinking which requirements for completing the project like when I run my code from command it opens itself in a web browser and I am also able to select multiple values from drop down and show the change in map.also get the india map.next i also shown the world graph with different group like country attack,weapon type ect.and also search for the selected group.also able to only south asia and India particular graph  and change in slider give also that change in graph. 
