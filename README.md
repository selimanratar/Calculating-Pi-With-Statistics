# Calculating-Pi-With-Statistics

This hour-project calculates Pi with the help of Statistics in a form of a darts game.

In the program, there is a target for the user to throw darts at, which is in shape of a circle inside a square (with 2 times radius being equal to a side of the square). 

For each dart we throw, statistically we would expect (Area_Of_Circle/Area_Of_Square) times total_darts to land on the circle and the rest to the areas on square that are out of circle's area. 

The program prompts the user for the amount of darts that user wants to throw, then places the darts randomly on a target 

Since (Area_Of_Circle/Area_Of_Square) is equal to Pi/4 (from this equation: 4r^2 / (r^2 * Pi));
It divides the amount of darts landed on circle to the amount of darts landed on the square (including those landed on circle). Then multiplies it by 4, which would eventually get closer and closer to Pi as we throw more and more darts to the target.

The user can also determine the radius of the circle and observe the change in the pace of convergence to Pi.

