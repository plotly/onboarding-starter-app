# Exploring Plotly Visualizations and Dash Applications

This repo includes a Jupyter Notebook called `explore_plotly_vis.ipynb` that demonstrates some ways to use Plotly visualizations and an `example_app.py` file to explore Dash Apps!

<div align="center">
  <a href="https://dash.plotly.com/project-maintenance">
    <img src="https://dash.plotly.com/assets/images/maintained-by-plotly.png" width="400px" alt="Maintained by Plotly">
  </a>
</div>


## Using this Repo

To use the this repo, just follow these steps:
1. Clone the repo to your local machine
    * For example, open your terminal and use these commands:
        * `cd Desktop`
        * `git clone https://github.com/plotly/onboarding-starter-app.git`
2. This will bring all of the files to your local machine
3. Navigate to the new directory 
    * `cd onboarding-starter-app`
4. Run the following command to check out the Jupyter Notebook
    * `jupyter notebook`
5. To see the dash app, run this command:
    * `pip install -r requirements.txt` (this will install all of the necessary dependencies for the dash app)
    * `python example_app.py`
    * You'll see a message that says `Dash is running on http://...`
    * Copy the `http://...` and paste it into your browser.

## The Jupyter Notebook

In the Jupyter Notebook, you will see the dependencies you need to gain the full flexibility of Plotly Visualizations. This will be a great place to start exploring the Plotly Graphing Library.

This notebook is thoroughly commented with explanations, and we **encourage you to explore reading in your own data and create visualizations**. The code in the notebook can serve as examples creating these visualzations. Simply use the Python libraries you commonly use to read your data and convert it to a Pandas dataframe.

For more information about the Plotly Graphing Library, check out the documentation!

[Plotly Express](https://plotly.com/python/plotly-express/)
[Plotly Graphing Library](https://plotly.com/python/)

## The Dash App

The Dash app is a simple, yet complete dash application that reads in sample data from Plotly Express and creates a basic line chart through a callback. Additionally, the Jupyter Notebook and the Dash App have some of the same code, which is one of the amazing aspects of Dash. We're coding interactive web applications in Python giving us the full flexibility that we've come to appreciate in data analysis.

This application is thoroughly commented. Please explore ways that you can read in your own data and edit the callback to visualize your data.

Here are some really helpful links to Dash documentation: 

[Dash App: The Layout](https://dash.plotly.com/layout)  
[Dash App: Callbacks](https://dash.plotly.com/basic-callbacks)

## Deploying the Dash App

Also, this repo has everything you need to explore deploying this application to your instance of Dash Enterprise! 

1. Initialize an App on Dash Enterprise 
2. Create a blank Workspace in the Workspace tab.
3. Either: 
    * Open the workspace and click and drag this repo's files to the file explorer in the Workpace.
    * Remove the `.git` file in the Workspace and clone this repo into the Workspace.
4. Then run the following `git` commands:
    * `git status`
    * `git add .`
    * `git commit -m "first deploy!"`
    * `git push plotly workspace:main`

