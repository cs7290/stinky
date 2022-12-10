# Stinky
### A project of the Roux Institute at Northeastern University
---

## Overview
Stinky maps smell complaints in the Portland, Maine metropolitan area in an attempt to identify pollutants, health hazards, and other quality of life impacts to Maine residents and visitors. It uses up-to-the-minute complaint data from [SmellMyCity](https://www.smellmycity.org), as well as other data, to seek and show patterns in Portland-area smells.

If you'd like to make a smell report, download the SmellMyCity app via the iOS App Store or the Google Play store. If you want to contribute code to Stinky, we welcome you to check the issues list associated with this repo. You should also feel free to suggest issues or submit pull requests directly.

The map and charts displayed on the site run from an [Observable](https://observablehq.com/d/e5057433bd482160) notebook and use MapLibre and D3.

## Data Sources


## Project Structure

In this version of the project, the entire data pipeline happens in linked Observable notebooks. The `docs` directory contains an html landing page and a basic CSS/SCSS setup that allows us to import and modify bootstrap for styling purposes.

## Observable Notebooks

- Main notebook: [Maplibre Heatmap with Compass](https://observablehq.com/d/e5057433bd482160). This is the notebook that is imported into the HTML page. It contains all the visible UI elements plus the code necessary to generate the map and apply various filters to the data.
- Compass direction selector: [Simple Compass Selector](https://observablehq.com/@cs7290/simple-compass-selector). This is a UI element that allows selection by wind direction. It outputs a JavaScript object that maps wind direction to a boolean indicating whether it should be visible.
- Histogram brush: [Click to Recenter Brush II (Histogram Version with Animation)](https://observablehq.com/d/f95fd9c234b88717). This is a 1-dimensional brush showing a histogram in the background. It functions similar to a traditional scatterplot brush but is easier to interpret with a large number of datapoints.
- Natural language processing: [What does it smell like?](https://observablehq.com/d/bc17b13892793ae). This contains the code necessary to develop word frequency metrics from the smell reports.
- Data API calls: [Fresh Stink](https://observablehq.com/d/c16cbf71c8623c43). This retrieves smell reports from the SmellMyCity API, queries a NOAA API for weather data, and uses the latter to add wind direction to the former.

## `docs/`

For the most part, everything in `docs/` should be easy to understand if you have a working knowledge of HTML/CSS and Bootstrap. For details on compiling SCSS to CSS, see the [separate README.md in `docs/`](docs/README.md).

### `index.html`

Most of the actual HTML code is fairly straightforward. A great resource for refreshing your memory regarding Bootstrap classes is the [Bootstrap 5 Cheatsheet from Theme Selection](https://bootstrap-cheatsheet.themeselection.com/).

Most of the real "business" happens in the section of script at the bottom of the file. First, we import the Observable runtime and inspector, as well as our actual notebook.

```html
<script type="module">
    import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@5/dist/runtime.js";
    import notebook from "https://api.observablehq.com/d/e5057433bd482160@1396.js?v=3";
```
Note the use of @ followed by a number to pin a specific version of the notebook.

Next, we make an object that maps names of cells in the Observable notebook to the id of the `<div>` where we want to insert them in the page.
```js
    const renders = {
        "container": "#observablehq-container",
        "compass": "#observablehq-compass",
        "brush": "#observablehq-brush",
        "selectAllBtn": "#observablehq-selectAllBtn",
        "animateBtn": "#observablehq-animateBtn",
        "whatSmellChart": "#observable-wordFrequencyChart",
        "flyToHtmlSelect": "#observablehq-flyToHtmlSelect",
        "testSmellBtn": "#observablehq-smellBtn1",
        "loading": "#observablehq-loading"
    };
```

Finally, we create a `Runtime` instance and pass the notebook to the runtime. We also pass a function that instructs the runtime to evaluate each notebook cell against the `renders`
object. If present, it creates an Inspector to inject the cell at the corresponding `<div>`; else, it returns `true` which ensures that cells that are not visible on the page still run in the background.

```js
    const runtime = new Runtime();
    const main = runtime.module(notebook, name => {
        const selector = renders[name];
        return selector ? new Inspector(document.querySelector(selector)) : true;
    });
</script>
```

The best documentation available at the moment for this process is from Observable's [Advanced Embedding and Downloading notebook](https://observablehq.com/@observablehq/advanced-embeds).

## Acknowledgements

This project builds on previous work from students in Philip Bogden's DS5110 class.