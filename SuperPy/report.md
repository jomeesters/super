Report

This assignment was very challenging. It took me a couple of weeks to manage and understand the assignment. Putting together a logical flow made it easier for me fulfill the requirements to make this program work

There are 3 technical elements of my implementation that are notable.

1. Class Stock
   Superpy contains the classes Product and Stock. The class Stock has a 'get_product' method which loads product data from the csv-files and creates a product instance for each bought product and updates it with information from the the sold-file.

The collection class Stock then loads all these Product instances into an instance list, or 'stock'. Each time a user needs a report, such as profit or product-sales, class methods specific to the type of report requested can be invoked on an up-to-date stock.

The advantage of structuring the code in this way, is that the class Stock provides a data structure which is better geared towards generating reports, than extracting the specific data directly from the two 'bought' and 'sold' csv-files everytime a report is queried.

2. CSV and Report files
   All csv files and report files are stored in the files/reports folder. If the files/reports folder has not been created, it will be created.

3. Uses of MatPlotLib
   When the inventory is reported, Matplotlib is used to display bar charts. It then displays a bar chart of products that have not expired and a bar chart of products that have expired.
