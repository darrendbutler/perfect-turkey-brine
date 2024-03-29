_Summary: Created a python serverless function to calculate ingredients for a Turkey Brine recipe_

# Challenge 1: The Perfect Holiday Turkey
 
## Your Chefs: Jen Looper, Cloud Advocate (Microsoft) and Darren Butler, Microsoft Student Ambassador
 
## This week's featured region: North America

[Watch Solution: Seasons of Serverless 2020- A Turkey Teaser!](https://youtu.be/BCbG50Zhw0Y)
 
In North America, the holidays are simply not complete without a proper turkey on the table! The only problem is, these birds can be hard to cook so that they are not dry and tough. The secret? A proper brine! 
 
Here's a [sample recipe](img.https://www.aspicyperspective.com/best-turkey-brine-recipe/) for that important process in the production of a perfect turkey.
 
There's a science to a great turkey brine, but we, as software engineers, are both absent-minded and need an automated way to remind ourselves each year of the proper percentages of ingredients of a good brine, based on the weight of the turkey.
 
According to Chef Darren's calculations, the brine equation and roast recommendation looks like this:
 
Brine time (in hours) = 2.4 * lbs of turkey
 
Salt (in cups) = 0.05 * lbs of turkey
 
Water (gallons) = 0.66 * lbs of turkey
 
Brown sugar (cups) = 0.13 * lbs of turkey
 
Shallots = 0.2 * lbs of turkey
 
Cloves of garlic = 0.4 * lbs of turkey
 
Whole peppercorns (tablespoons) = 0.13 * lbs of turkey
 
Dried juniper berries (tablespoons) = 0.13 * lbs of turkey
 
Fresh rosemary (tablespoons) = 0.13 * lbs of turkey
 
Thyme (tablespoons) = 0.06 * lbs of turkey
 
Roast time (in minutes) = 15 * lbs of turkey
 
Your challenge: convert this brine equation and cook time to an automated process so that when you input a turkey's weight, you will be given the amount of water, sugar, salt, and spices to add and a recommendation on how long to cook it.
 
Let's assume you have available a large cooler for your turkey and its brine and that it's defrosted.
