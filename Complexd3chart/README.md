# Complexd3Chart

**Purpose**:
- This is HTML structure of your visualization. It establishes a visual canvas for oyur bar chart and links to both the D3.js library and our custom JavaScript file.

**Key Parts** :
1. `<svg width="800" height="600"></svg>`: This  create an SVG canvas with specified and heigh where the bar chart will be drawn.
2. `<script src="https://d3js.org/d3.v5.min.js"></script>`: This links to the D3.js library. You need this to use D3 functions and methods.
3. `<script src="chart.js"></script>`: This links to our custom JS file which contains the logic for rendering the bar chart.

**Key parts Code** :
1. **Data Declaration** :
   - `const data = [30, 86, 168, 281, 303, 365];` : This is the data array that will represented in the bar chart
2. **SVG and Dimensions Setup**:
   - We first select the SVG element from the HTML and define margins, width, and height for our chart.
   - We also define the x and y scales. '`x`' is a band scale used for discrete data(like categories) and 'y' is a linear scale used for continuous data.
3. **Axis Creation**:
   - `g.append("g)`:Appends a new group ('<g>') element which will containr x-render the y-axis on the left.
   - `.call(d3.axisBottom(x))`: This renders the x-axis on the bottom.
   - Similiarly, another groupis appended to contain the y-axis elements. This will render the y-axis on the left.
4. **Bar Creation**:
   - `g.selectAll(".bar")`: Selects all elements with the class "bar". initially, no such elements exist.
   - `.data(data)`: Bind the provided data to the selected elements.
   - `.enter()`: This method returns a placeholder for each data point that doesn't yet have a corresponding DOM element.
   - `.append("rect)`: For each placeholder, appends a rectangle("<rect>") to the SVG. This rectangle will represent a bar.
   - The subsequent '.attr()' calls set various attributes for each bar:
      - `x` and `y` : These determine the position
      - `width` : This determines the width of the bar based on the x scale's bandwith.
      - `height`: This determines the height of the bar based on the difference between the tota; height and the y position
    
In summary, this script reads a data array and uses it to draw a bar chart on an SVG canvas. That bars positions and sizes are determined by D3 scales, and the x and y axes help contextualize the data points.
 
# Example view
![chart](https://github.com/rifqanzalbina/DifferentButSame/assets/124742008/5fc0bed0-69b8-4c1d-b421-304def428ffc)

