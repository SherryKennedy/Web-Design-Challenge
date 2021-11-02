# Web-Design-Challenge -Web Visualization Dashboard (Latitude)
HTML, CSS, Bootstrap media queries, CSV

## Background 
Data analysed previously with ***WeatherVacationAnalysis_api** repository. 
Created a dashboard to show the findings and showing visualizations.
Plotting weather data from [weather data](data/cities.csv).

Built a datshboard. Created individual pages for each plot and a means by which one can navigate between them (navigation menu). The pages contain visualizations and their corresponding explanations. Created a landing page, a comparison page (to compare all of the plots), and a data page showing the data used to build the plots. Seven HTML pages in total. 

Bootstrap was used to create responsive pages, to show the results on various screen sizes.
Use of media queries.

Note: The code files csv_to_html are the same code. Just noted the differences in using Jupyter Notebook and a python file within VSCode. 
The csv_to_html code allows the easy generation of an HTML table of results from a CSV file. 

### Setup
Used the following ***directory*** / - file setup:

***root***
    ***code*** 
            - csv_to_html.ipynb
            - csv_to_html.py
    ***data***
            - cities.csv
    ***plots***
            - Cloudiness.html
            - Humidity.html
            - MaxTemperature.html 
            - WindSpeed.html
    ***static***
                ***css***
                        - main.css
                ***images***
                        - Fig1.png
                        - Fig2.png
                        - Fig3.png
                        - Fig4.png
   - index.html
   - data.html
   - comparison.html
   
  ### Landing page:
  Explanation of the project.
  Links to each visulaization page. 
  Sidebar showing preview of images of each clickable plot image.
  
  ### Four Visualization pages:
  A descriptive heading.
  Plot/Visualization for selected comparison.
  Paragraph describing the plot and its significance.
  
  ### Comparison page:
  All the visualizations for comparison.
  
  ### Data page:
  Displays table of loaded data used for the visualizations.
    
  ### Navigation menu:
  - Has the name of the sit on the left of the nav which allow user to return to the landing page from any page. 
  - Contains a dropdown menu on the right of the navbar named "Plots" that provides a link to each individual visualization page. 
  - Provides two more text links on the right: "Comparisons" , which links ot the comparisons page, and "Data", which links to the data page.
  - Is responsive (using media queries).
  
        
    

- - -

## References

OpenWeatherMap.org. (2012). Сurrent weather and forecast. Retrieved from [https://openweathermap.org/](https://openweathermap.org/)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

