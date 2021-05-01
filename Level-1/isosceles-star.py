'''       A program to draw an isosceles triangle with * like below
          * 
         * * 
        * * * 
       * * * * 
      * * * * * 
     * * * * * * 
    * * * * * * * 
   * * * * * * * * 
  * * * * * * * * * 
 * * * * * * * * * * 
 '''

# The Magic of Logic here is in the point where we are considering both the star and the adjacent space as one charecter,
# Where I have struggled hours to figure out.
# Also notice the rule of deploying n spaces before we deploy the star and space as a single charecter.
# Yes.! That was the logic. Simple it may seem but crazy it does to one.

n = 10
for i in range(1, 11):
    print(' '*n, end = '')
    print('* '*(i))
    n-=1
