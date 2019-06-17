# Completed DataCamp Data science courses Python<br>
Python notebooks from DataCamp data science tutorials:v
1. Intermediate Python Data structures <br>
99_Python_DataCamp_01_intermediate.ipynb<br>

2. Intermediate Python Pandas, DataFrames<br>
99_Python_Datacamp_02_intermediate_pandas_dataframe.ipynb<br>
3. Toolbox for data scientist Part 1<br>
99_Python_Datacamp_03_toolbox1_functions_lambda.ipynb<br>
Functions, lambda(),map(),filter(),reduce()<br>
4. Toolbox for data scientist Part 2<br>
99_Python_Datacamp_04_toolbox2_iterators_generators_chunks<br>
iterators,enumerate(),zip(),chunks for big data,generators, nested loops,<br>
5. Statistical thinking in Python part 1<br>
99_Python_Datacamp_05_statistical_thinking_part1<br>
Plotting  a histogram, adjusting number of bins, sns(seaborne),bee swarm plot, boxplot<br>
computing and plotting ECDF(Empirical cumilative distribution function)<br>
means and medians,covariance and pearson correlation coefficient, scatter plots<br>
Np.random and bernoulli trials, binomial distribution, Normal PDFs and CDFs,exponential distribution<br>
6. Statistical thinking in Python part 2<br>
99_Python_Datacamp_06_statistical_thinking_part2.ipynb<br>
Exploratory data analysis(EDA) (bee swarm plots), ECDF plots, bootstrap confidence intervals, hypothesis testing, p-values, linear regressions, pearson correlation coefficients.
7. Importing data in Python part 1
99_Python_Datacamp_07_importing_data_in_Python_part1.ipynb <br>
Importing entire text files,<br>
Importing text files line by line,<br>
Importing flat files using NumPy,<br>
Working with mixed data types,<br>
Importing flat files using pandas,<br>
Pickled files - serialized,<br>
Excel Spreadsheets,<br>
MATLAB files,<br>
SAS files,<br>
Strata files,<br>
HDF5 files<br>
Relational databases: PostGreSQL, MySQL, SQLite, SQL <br>

8. Importing data in Python part 2<br>
99_Python_Datacamp_08_importing_data_in_Python_part2.ipynb<br>
import and locally save datasets from the web, load datasets into pandas DF, make HTTP requests(GET requests), Scrape web data such as HTML, parse HTML into useful data (BeautifulSoup), use urlllib and requests packages<br>
loading and exploring JSON<br>
loading data from twitter and exploring json<br>
9. Manipulating time series data in Python<br>
99_Python_Datacamp_09_manipulating_time_series_in_python <br>
indexing and resampling time series, converting to_datetime
basic time series calculations shift(),diff(),mul(),div()
frequency resampling to monthly, yearly,upsampling(bfill,ffill),reindex(),upsamping with resample(),
.add_suffix('_fill'), interpolate(),pd.concat([series_1, series_2), axis=1)
resample('M').median(), moving average,expanding windows (average up to date),
cumsum(), expanding().sum(), running return, correlation, heat map of correlation.

10. 99_Python_Datacamp_09_manipulating_time_series_in_python.ipynb <br>
Exploring data:
Loading, Exploratory data analysis, summary stats,frequency counts, visual exploratory, single vas in histogram, multiple vars with boxplots, multiple vars with scatter plots
Tidying data for analysis:
recognizing tidy data,reshaping data using melt (swapping columns and rows), customizing melted data, pivoting data (opposite of melt),resetting index of DataFrame, pivoting duplicate values,splitting column with .str, .split(), .get()
Combining data for analysis:
concatenating data, combining rows of data, combining columns of data, finding and concatenating files, finding file that match a pattern, iterating and concatenating matches, merge data, 1 to 1 merge, many to 1 merge, many to many merge
Cleaning data for analysis:
data types, converting data types, working with numerical data,using regular expressions to clean strings, string parsing with regular expressions, extracting numerical values from strings, pattern matching, using functions to clean data,custom functions to clean data,lambda fnctions, duplicate and missing data, dropping duplicate data, filling missing data, testing with asserts
Case study:
exploratory analysis, visualizing data, assembling data, reshaping data, checking data types, mor cleaning and processing

11. 99_Python_Datacamp_11_pandas_foundations.ipynb <br>
Data ingestion and inspection:
import export in various formats
Exploratory data analysis:
pandas line plots, scatter plots, box plots, hist,pdf,cdf, statistical exploratory analysis, median vs mean, quantiles, standard deviation, separating populations with boolean indexing, filtering and counting, separate and summarize, separate and plot
Time series in pandas:
indexing pandas time series, reading and slicing times, creating DatetimeIndex, partial string indexing and slicing, reindexing the index, resampling pandas time series, resampling and frequency, separating and resampling, rolling mean,resamle and roll with it, manipulating time series, method chaining and filtering, missing values interpolation, time zones and conversion, visualizaing time series, plotting time series, datetime indexing,plotting data ranges, partial indexing

12. 99_Python_Datacamp_12_manipulating_DataFrames_withPandas.ipynb
01 Extracting and transforming data:<br>
indexing dataframes, index ordering, positional and labeled indexing, indexing and column rearrangment, slicing dataframes, slicing rows, slicing columns, subselecting dataframes with lists,
filtering data frames, thresholding data, filtering columns using other columns, filtering using NaNs, transforming dataframes,using apply() to transform a column, using .map() with dictionary, using vectorized functions
02 advanced indexing:<br>
index objects and label data, index values and names,changing index of a dataframe, changing index name labels, building an index then a dataframe, hierarchical indexing, extracting data with a multiindex, setting and sorting a multiindex, using .loc[] with nonunique indexes, indexing multipe levels of multiindex
03 rearranging and reshaping data:
pivoting DataFrames, pivoting and the index, pivoting a single variable, pivoting all variables, stacking and unstacking DataFrames, restoring data index, melting DataFrames, adding names for readability, going from wide to long, obtaining key-value pairs with melt(), pivot tables,  setting up a pivot table, using other aggregations in pivot tables, using margins in pivot tables
04 grouping data:<br>
categoricals and groupby,grouping multiple columns, grouping by another series,groupby and aggregations, computing multiple aggregates of multiple columns,agregating on index levels/fields, grouping on a function of the index, groupby and transformations,detecting outliers with z-scores, filling missing data(imputations by group),other transformations with .apply(), groupby and filtering, grouping and filtering with .apply, .filter(),.map()
05 putting it all together:<br>
grouping and aggregating, using .value_counts() for ranking, using pivot_table() to count medals by type, understanding column labels, applying .drop_duplicates(), finding possible errors with groupby(), locating suspecious data, using .nunique() to rank distinct sports,reshaping data for visualization, line plot, area plot,
Extracting and transforming data:<br>
extracting, filtering,transforming data from dataframes, advanced indexing with multiple levels, tidying, rearranging, restructuring data, pivoting, melting, stacking, identifying and splitting by groups

13. Introduction to DataBases in Python, SQLAlchemy

1 <b> Intro to databases </b>, relational model, connecting to database, engines and connection strings, autoloading tables from database, viewing table details, intro to SQL, selecting data from table(raw SQL), selecting data from table with SQLAlchemy
<br>
2 <b>Applying Filtering</b>, Ordering and Grouping to Queries
filtering and targeting data, connecting to PostreSQL DB, filter data selected from table, ordering by single column, descending order, ordering bt multiple columns, counting, summing, grouping,counting distinct data,use pandas and matplotlib to visialize our data, SQLAlchemy ResultsProxy and Pandas DataFrame, From SQLAlchemu results to a Graph
<br>
3 <b>ADVANCED SQLAlchemy</b> querries
calculing values  in query, connecting to MySQL DataBase, calculating difference between two columns, determening percentage, SQL relationships, automatic joins, joins,hierarchical tables, leveraging functions and Group_bys
<br>
4 <b>Creating and Manipulating your own database</b>
creating databases and tables, creating tables with SQLAlchemy, Inserting data to table, inserting a single row with an insert() statement, inserting multiple records at once, Loading CSV into Table,
Updating data in dataBase, updating individual records, updating multiple records, correlated updates, removing data from database, deleting all records from table, deleting specific records, deleting table completely
<br>
5 <b>Putting it all together - Census Case Study</b> <br>
Setup the engine and MetaData, create the table to the database, populating the database,
reading the data from csv, load data from list into the table, example querries,
build a query to determine  the average age by population, determine percentage of population by gender and state, determine the difference by state from the 2000 and 2008 censuses
In separate file:
99_Python_Datacamp_13_intro_to_databases_casestudy_census.ipynb
All other exercises in:
99_Python_Datacamp_13_intro_to_databases_exercises_sqlalchemy.ipynb
