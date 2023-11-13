import matplotlib.pyplot as plt
def simulate_bouncing_ball(initial_height_cm, cor):
    # Convert initial height to meters
    initial_height = initial_height_cm / 100

    # Gravitational acceleration (approximately 9.81 m/s^2)
    gravity = 9.81

    # Initialize variables
    velocities = []
    heights = []
    times = []
    velocity = 0
    current_height = initial_height

    # Stopping criteria (set a minimum height for stopping)
    min_height = 0.001  # Adjust as needed

    # Simulate bounces
    time_elapsed = 0
    while current_height > min_height:
        # Calculate velocity when hitting the floor
        velocity = (2 * gravity * current_height)**0.5

        # Apply energy decay
        velocity *= cor

        # Update current height
        current_height = (velocity ** 2) / (2 * gravity)

        # Store velocity, height, and time
        velocities.append(velocity)
        heights.append(current_height)
        times.append(time_elapsed)

        # Increment time elapsed
        time_elapsed += 2 * velocity / gravity

    return times, velocities, heights

# Input parameters
initial_height_cm = int(input('Enter an initial height: '))  # initial height in centimeters
cor = float(input('Enter coefficient of restitution:  '))  # coefficient of restitution (adjust as needed)

# Simulate bouncing ball
times, velocities, heights = simulate_bouncing_ball(initial_height_cm, cor)

# Plot velocity decay and height decay against time
fig, ax1 = plt.subplots()

# Plot velocity on the left y-axis
color = 'tab:blue'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Velocity (m/s)', color=color)
ax1.plot(times, velocities, color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for height
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Height (m)', color=color)
ax2.plot(times, heights, color=color, marker='x')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Velocity and Height Decay of Bouncing Ball')
plt.grid(True)

# Initial position of the ball
ball = plt.scatter(times[0], heights[0], c='blue', s=80)

plt.show()

