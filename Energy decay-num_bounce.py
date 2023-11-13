import matplotlib.pyplot as plt

def calculate_bounces_and_distance(coefficient_of_restitution, initial_height, planet_gravity):
    # Constants for different planets' gravitational accelerations (in m/s^2)
    planet_gravities = {
        'Mercury': 3.7,
        'Venus': 8.87,
        'Earth': 9.81,
        'Mars': 3.71,
        'Jupiter': 24.79,
        'Saturn': 10.44,
        'Uranus': 8.69,
        'Neptune': 11.15
    }

    # Dictionary to map coefficients to ball names
    ball_coefficients = {
        0.7: "Tennis Ball",
        0.75: "Basketball",
        0.9: "Super Ball",
        0.3: "Softball"
    }

    # Use the get method to retrieve the ball name or set it to "Unknown Ball" if not found
    ball_name = ball_coefficients.get(coefficient_of_restitution, "Unknown Ball")

    # Initialize variables
    height = initial_height
    bounces = 0
    velocities = []  # To store velocities for plotting
    time = 0

    # Simulation loop
    while height >= 0.1:  # Until the height is less than 10 centimeters
        # Calculate the new height after the bounce
        height *= coefficient_of_restitution
        # Calculate velocity with adjusted gravitational acceleration and append to the list
        velocity = (2 * planet_gravities[planet_gravity] * height)**0.5
        velocities.append(velocity)
        # Increment time
        time += (2 * height / planet_gravities[planet_gravity])**0.5
        # Increment bounce count
        bounces += 1

    # Report results
    print(f"\nFor {ball_name} dropped from {initial_height} meters on {planet_gravity}:")
    print(f"Number of bounces: {bounces}")

    # Plot velocity decay
    plt.plot(range(bounces), velocities)
    plt.title("Velocity Decay Over Bounces")
    plt.xlabel("Bounce Number")
    plt.ylabel("Velocity (m/s)")
    plt.show()

# Input from the user
try:
    coefficient_of_restitution = float(input("Enter the coefficient of restitution: "))
    initial_height = float(input("Enter the initial height in meters: "))
    planet_gravity = input("Enter the planet (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, or Neptune): ")
except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    if planet_gravity not in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        print("Invalid planet name. Please enter a valid planet.")
    else:
        calculate_bounces_and_distance(coefficient_of_restitution, initial_height, planet_gravity)
