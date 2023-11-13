import turtle

gravity_factors = {
    'Mercury': -0.5 * 3.7 / 2,  # Adjusted for simulation
    'Venus': -0.5 * 8.87 / 2,
    'Earth': -0.5 * 9.81 / 2,
    'Mars': -0.5 * 3.71 / 2,
    'Jupiter': -0.5 * 24.79 / 2,
    'Saturn': -0.5 * 10.44 / 2,
    'Uranus': -0.5 * 8.69 / 2,
    'Neptune': -0.5 * 11.15 / 2
}
gravity = 0
velocity = 0  # pixels/(time of iteration) instead of m/s^2
energy_loss = float(input('Enter Energy loss (between 0 and 1): '))
mass_factor = float(input('Enter the mass factor: '))
initial_height = float(input('Enter the initial height in pixels: '))
planet = input('Enter the planet (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, or Neptune): ')

if planet not in gravity_factors:
    print("Invalid planet name. Please enter a valid planet.")
else:
    gravity = gravity_factors[planet]

width = 600
height = 800
scale_factor = 10 # Range of 10 units per pixel

window = turtle.Screen()
window.setup(width, height)

ball = turtle.Turtle()
axis = turtle.Turtle()  # New turtle for drawing the y-axis

ball.penup()
ball.color("green")
ball.shape("circle")

axis.penup()
axis.goto(-width / 2, -height / 2)
axis.pendown()
axis.color("black")
axis.pensize(2)

# Draw y-axis with scale
for i in range(0, height + 1, scale_factor):
    axis.penup()
    axis.goto(-width / 2, -height / 2 + i)
    axis.pendown()
    axis.forward(5)  # Adjust the tick length as needed

axis.setheading(90)
axis.forward(height)

while True:
    ball.sety(ball.ycor() + velocity)
    velocity += gravity

    if ball.ycor() < -height / 2:
        velocity = -velocity * energy_loss

    # Adjust gravity based on mass factor
    gravity = -0.5 * (mass_factor / 2)

    window.update()
