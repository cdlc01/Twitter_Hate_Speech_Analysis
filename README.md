# Twitter Hate Speech Analysis in 2021

Author: Christopher de la Cruz

Overview
Our analysis currently reflects what types of renovations (based on a home's grade and condition) are most worth the increase in selling price. We take a deep dive into the specific relationship that grade and price share with sales price. Our project currently shows that there are specific grade and condition relationships that do make the renovations worth the cost and about how much you can expect to save. We also found that the square footage of living spaces is one of the best indicators of price when doing a very general modeling of factors that affect home prices. This analysis can be used by any real estate agency or prospective home seller to guide them on what kinds of renovations they should be making.

Business Problem
We are a Seattle-based real estate agency that specializes in helping prospective real estate sellers make the best possible choices to increase the value of their homes before putting them on the market. Among the homes in Seattle, Washington, homes are graded by both their grade (1 - 10; 10 being the highest possible condition) and condition (1 - 5; 5 being the highest quality condition). Our project aims to look at what types of renovations are worth the improvement in price (for example if a home has a grade of 1, is the change in selling price worth it to renovate to a 3 or does it have to renovate to a 5 in order to be worth the renovation?). We chose to focus on renovations because there are the most straight-forward changes that you can make to a home (for example, you cannot simply add a waterfront view to a home).

Data
Our dataset contains house sale prices for King County. It includes homes sold and the characteristics of those homes. For the sake of our grade & condition regression model, we limited our houses specifically to Seattle and specifically looked closely at:

Price
Grade
Condition
We do also include further columns when modeling what homes might sell for in general in Seattle as well as a a very general model of what a home might sell for even outside of Seattle

Methods
We mainly observed the distributions of sales prices, grades and conditions and explored their relationships to one another. We also utitilzied two sample T-Tests in order to determine whether different groups were statistically significant from one another and whether the significance was large enough to justify the renovation.

Result 1
Our model shows that not all renovations generate enough savings to necessarily be worth the price and labor (we showcase the relationships in our conclusion). Here are the results of our grade & condition model.

Visual 1
gradeconmodel

Conclusions
These are our business recommendations regarding renovations done to a house before selling it on the market:

Our analysis shows that square footage of the living space is strongly correlated with the price of a house. While we realize that increasing an already-built house's footage may not always be realistic, we've discovered that there is statistical differences in the price of homes depending on it's Grade or Condition rating.

For Grade, we're 95% confident of the following:

Upgrading homes with a grade of 6 to a 7 can generate a 53K - 77K savings amount.
Upgrading homes with a grade of 7 to an 8 can generate a 52K - 78K savings amount.
Upgrading homes with a grade of 8 to a 9 can generate a 38K - 65K savings amount.
For Condition, we're 95% confident of the following:

Upgrading homes with a condition of 2 to a 3 can generate a 41K - 55K savings amount.
Upgrading homes with a condition of 2 to a 4 can generate a 57K - 71K savings amount.
Upgrading homes with a condition of 2 to a 5 can generate a 75K - 90K savings amount.
Upgrading homes with a condition of 3 to a 4 can generate a 8K - 23K savings amount.
Upgrading homes with a condition of 3 to a 5 can generate a 27K - 42K savings amount.
Upgrading homes with a condition of 4 to a 5 can generate a 11K - 26K savings amount.
For More Information
Please review our full analysis in our Jupyter Notebook or our presentation: https://docs.google.com/presentation/d/1SX5UJGmCgV2di-Wo5SZsfECan8wcSG7Y7HiPm24aCQs/edit#slide=id.gd0341dc497_0_842

For any additional questions, please contact Christopher de la Cruz at cdelacruz2013@gmail.com, David Tian at dt1086@stern.nyu.edu

Repository Structure
├── README.md                                         <- The top-level README for reviewers of this project
├── Nan.pdf                                           <- PDF version of project presentation
├── EDA.ipynb                                         <- Narrative documentation of analysis in Jupyter notebook 
├── data                                              <- Both sourced externally and generated from code     
└── images                                            <- Both sourced externally and generated from code

