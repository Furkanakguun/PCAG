```
  ____   ____   ___   ____ 
 |  _ \ / ___| / _ \ / ___|
 | |_) | |    | |_| | |  _   
 |  __/| |___ |  _  | |_| | 
 |_|    \____||_| |_|\____|
                           
    Physics in Computer Animations and Games
```

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://pygame.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.19+-orange.svg)](https://numpy.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive educational project covering physics simulations and game development concepts using Python, Pygame, and NumPy. This repository contains interactive simulations, mathematical models, and practical implementations of various physics phenomena commonly used in computer animations and games.

## Project Overview

This project serves as a complete learning resource for understanding how physics principles are applied in computer graphics and game development. It covers fundamental concepts from basic motion to advanced multi-body dynamics, providing both theoretical knowledge and hands-on implementation experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Sections Overview](#sections-overview)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **12 Comprehensive Sections** covering physics fundamentals to advanced topics
- **Interactive Simulations** with real-time visualization using Pygame
- **Mathematical Modeling** with NumPy for accurate calculations
- **Educational Content** with detailed explanations and theory
- **Practical Examples** including sports ball physics, cloth simulation, and collision detection
- **Modular Design** allowing easy experimentation and learning

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/PCAG.git
   cd PCAG
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run a sample simulation:**
   ```bash
   python ball_collision_calculations.py
   ```

### Required Dependencies

```
pygame>=2.0.0
numpy>=1.19.0
matplotlib>=3.3.0
scipy>=1.7.0
pymunk>=6.0.0
```

## Project Structure

```
PCAG/
├── motion_in_one_dimension/          # 1D motion and free fall
├── motion_in_two_dimensions_and_gravity/  # 2D motion, projectiles, gravity
├── vectors_and_pygame/              # Vector mathematics and Pygame basics
├── forces_in_one_and_two_dimensions/ # Force calculations and dynamics
├── linear_momentum_impulse_and_collision/ # Momentum, impulse, collisions
├── rotational_motion/               # Angular motion, torque, rotation
├── spring_and_damper_in_modelling/  # Spring-mass-damper systems
├── multiparticle_systems/           # Multi-particle physics
├── cloth_simulatioon_with_particle_mechanics/ # Cloth simulation
├── trajectory_of_a_spinning_object/ # Magnus effect, spinning objects
├── multi_body_dynamics_with_control/ # Advanced dynamics and control
└── README.md
```

## Getting Started

### Quick Start

1. **Basic Ball Physics:**
   ```bash
   python ball_collision_calculations.py
   ```
   - Interactive ball collision simulation
   - Press SPACE to add balls
   - Press 'r' to toggle ray casting

2. **Cloth Simulation:**
   ```bash
   python cloth_simulatioon_with_particle_mechanics/particleDancer.py
   ```
   - Real-time cloth simulation
   - Mouse interaction supported

3. **Free Fall Analysis:**
   ```bash
   python motion_in_one_dimension/free_fall_object.py
   ```
   - Mathematical analysis of free fall
   - Position, velocity, acceleration plots

## Sections Overview

### 1. Motion in One Dimension
**Location:** `motion_in_one_dimension/`
- **Theory:** Kinematic equations, free fall, numerical integration
- **Features:** Position/velocity/acceleration analysis, data visualization
- **Applications:** Character movement, projectile physics, collision detection
- **Key Files:** `free_fall_object.py`, `ballDropcalc.py`, `distance_time.py`
- **Mathematical Focus:** v = v₀ + at, x = x₀ + v₀t + ½at²

### 2. Motion in Two Dimensions and Gravity
**Location:** `motion_in_two_dimensions_and_gravity/`
- **Theory:** Vector mathematics, projectile motion, gravity effects
- **Features:** 2D trajectory simulation, angle calculations, component analysis
- **Applications:** Sports simulations, ballistics, orbital mechanics
- **Key Files:** `soccer.py`, `euler.py`, `draw_angle_example_component_sum.py`
- **Mathematical Focus:** Vector operations, projectile equations

### 3. Vectors and Pygame
**Location:** `vectors_and_pygame/`
- **Theory:** Vector mathematics, coordinate systems, transformations
- **Features:** Interactive graphics, sprite programming, event handling
- **Applications:** Game development, interactive simulations, graphics programming
- **Key Files:** `vectors_pygame.py`, `spritePygame.py`, `bouncing_rectangle.py`
- **Mathematical Focus:** Dot product, cross product, vector normalization

### 4. Forces in One and Two Dimensions
**Location:** `forces_in_one_and_two_dimensions/`
- **Theory:** Newton's laws, force diagrams, friction, air resistance
- **Features:** Force calculations, boundary conditions, numerical integration
- **Applications:** Vehicle physics, character movement, realistic motion
- **Key Files:** `euler.py`, `bounceBallairdrag.py`, `boundry_ivp.py`
- **Mathematical Focus:** F = ma, force components, integration methods

### 5. Linear Momentum and Collision
**Location:** `linear_momentum_impulse_and_collision/`
- **Theory:** Momentum conservation, impulse, collision response
- **Features:** Collision detection, ray-sphere intersection, momentum transfer
- **Applications:** Ball physics, particle systems, realistic collisions
- **Key Files:** `momentum.py`, `raySphereIntersection.py`, `twoD_transformation.py`
- **Mathematical Focus:** p = mv, impulse-momentum theorem

### 6. Rotational Motion
**Location:** `rotational_motion/`
- **Theory:** Angular kinematics, torque, moment of inertia, angular momentum
- **Features:** Rotating objects, gyroscopic motion, rolling physics
- **Applications:** Spinning objects, vehicle dynamics, physics puzzles
- **Key Files:** `torque.py`, `rotPolygon.py`, `spritePygame.py`
- **Mathematical Focus:** τ = Iα, L = Iω, rotational energy

### 7. Spring and Damper Modeling
**Location:** `spring_and_damper_in_modelling/`
- **Theory:** Hooke's law, harmonic motion, resonance, damping
- **Features:** Mass-spring-damper systems, forced oscillations
- **Applications:** Cloth simulation, soft body physics, UI animations
- **Key Files:** `spring.py`, `forcedspringdamper.py`, `ODEvsEuler.py`
- **Mathematical Focus:** F = -kx, harmonic oscillator equations

### 8. Multi-Particle Systems
**Location:** `multiparticle_systems/`
- **Theory:** Center of mass, particle interactions, constraint systems
- **Features:** N-body simulations, collision detection, performance optimization
- **Applications:** Granular materials, molecular dynamics, crowd simulation
- **Key Files:** `dumbellPyGame.py`, `imageCG.py`, `dumbell.py`
- **Mathematical Focus:** Center of mass, particle interactions

### 9. Cloth Simulation
**Location:** `cloth_simulatioon_with_particle_mechanics/`
- **Theory:** Mass-spring models, Verlet integration, constraint satisfaction
- **Features:** Real-time cloth simulation, PyMunk integration, interactive demos
- **Applications:** Character clothing, flags, curtains, soft body physics
- **Key Files:** `particleDancer.py`, `verletCloth02.py`
- **Mathematical Focus:** Spring forces, Verlet integration, constraint solving

### 10. Trajectory of Spinning Objects
**Location:** `trajectory_of_a_spinning_object/`
- **Theory:** Magnus effect, lift forces, air resistance, spin effects
- **Features:** Sports ball physics, trajectory analysis, environmental factors
- **Applications:** Sports simulations, ballistics, aerodynamic effects
- **Key Files:** `tennisBall_np.py`, `minkowski.py`, `AxisAlignedBoundingBox.py`
- **Mathematical Focus:** Magnus force, drag equations, lift coefficients

### 11. Multi-Body Dynamics with Control
**Location:** `multi_body_dynamics_with_control/`
- **Theory:** Constraint-based dynamics, control systems, PID controllers
- **Features:** Advanced physics simulation, control algorithms, optimization
- **Applications:** Robotics, vehicle dynamics, biomechanical modeling
- **Key Files:** `pymunkPD.py`, `invertedPendulum.py`, `hs71.py`
- **Mathematical Focus:** Constraint equations, control theory, optimization

## Usage Examples

### Basic Collision Detection
```python
import pygame
import math

def check_collision(ball1, ball2):
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y
    distance = math.hypot(dx, dy)
    return distance < (ball1.radius + ball2.radius)

def resolve_collision(ball1, ball2):
    # Calculate collision normal
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.hypot(dx, dy)
    normal_x = dx / distance
    normal_y = dy / distance
    
    # Calculate relative velocity
    relative_velocity_x = ball2.change_x - ball1.change_x
    relative_velocity_y = ball2.change_y - ball1.change_y
    
    # Calculate impulse
    impulse = 2 * (relative_velocity_x * normal_x + relative_velocity_y * normal_y)
    impulse /= (1/ball1.mass + 1/ball2.mass)
    
    # Apply impulse
    ball1.change_x += impulse * normal_x / ball1.mass
    ball1.change_y += impulse * normal_y / ball1.mass
    ball2.change_x -= impulse * normal_x / ball2.mass
    ball2.change_y -= impulse * normal_y / ball2.mass
```

### Vector Operations and Physics
```python
import numpy as np
import pygame

class PhysicsObject:
    def __init__(self, x, y, mass=1.0):
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.array([0, 0], dtype=float)
        self.acceleration = np.array([0, 0], dtype=float)
        self.mass = mass
        self.force = np.array([0, 0], dtype=float)
    
    def apply_force(self, force):
        self.force += force
    
    def update(self, dt):
        # F = ma, so a = F/m
        self.acceleration = self.force / self.mass
        
        # Update velocity and position using Euler integration
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        
        # Reset forces for next frame
        self.force = np.array([0, 0], dtype=float)
    
    def apply_gravity(self, gravity=9.81):
        self.apply_force(np.array([0, gravity * self.mass]))
```

### Spring-Mass System
```python
def spring_force(particle1, particle2, rest_length, spring_constant):
    displacement = particle2.position - particle1.position
    current_length = np.linalg.norm(displacement)
    
    if current_length == 0:
        return np.array([0, 0])
    
    force_magnitude = spring_constant * (current_length - rest_length)
    force_direction = displacement / current_length
    return force_magnitude * force_direction

def damped_spring_force(particle1, particle2, rest_length, spring_constant, damping):
    # Spring force
    spring_force = spring_force(particle1, particle2, rest_length, spring_constant)
    
    # Damping force (proportional to relative velocity)
    relative_velocity = particle2.velocity - particle1.velocity
    displacement = particle2.position - particle1.position
    current_length = np.linalg.norm(displacement)
    
    if current_length > 0:
        damping_force = -damping * relative_velocity
        return spring_force + damping_force
    
    return spring_force
```

### Rotational Physics
```python
class RotatingObject:
    def __init__(self, x, y, mass, moment_of_inertia):
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.array([0, 0], dtype=float)
        self.angle = 0.0
        self.angular_velocity = 0.0
        self.mass = mass
        self.moment_of_inertia = moment_of_inertia
        self.torque = 0.0
    
    def apply_torque(self, torque):
        self.torque += torque
    
    def apply_force_at_point(self, force, point):
        # Apply linear force
        self.velocity += force / self.mass
        
        # Calculate torque
        r = point - self.position
        torque = np.cross(r, force)
        self.torque += torque
    
    def update(self, dt):
        # Linear motion
        self.position += self.velocity * dt
        
        # Angular motion
        angular_acceleration = self.torque / self.moment_of_inertia
        self.angular_velocity += angular_acceleration * dt
        self.angle += self.angular_velocity * dt
        
        # Reset torque
        self.torque = 0.0
```

### Cloth Simulation Setup
```python
import pygame
import numpy as np

class ClothSimulation:
    def __init__(self, width, height, rows, cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.particles = []
        self.springs = []
        
        # Create particle grid
        for i in range(rows):
            row = []
            for j in range(cols):
                x = j * (width / (cols - 1))
                y = i * (height / (rows - 1))
                particle = Particle(x, y)
                row.append(particle)
            self.particles.append(row)
        
        # Create springs
        self.create_springs()
    
    def create_springs(self):
        for i in range(self.rows):
            for j in range(self.cols):
                # Structural springs (horizontal and vertical)
                if j < self.cols - 1:
                    self.add_spring(self.particles[i][j], self.particles[i][j+1])
                if i < self.rows - 1:
                    self.add_spring(self.particles[i][j], self.particles[i+1][j])
                
                # Diagonal springs (shear resistance)
                if i < self.rows - 1 and j < self.cols - 1:
                    self.add_spring(self.particles[i][j], self.particles[i+1][j+1])
                    self.add_spring(self.particles[i][j+1], self.particles[i+1][j])
    
    def add_spring(self, p1, p2, rest_length=None, stiffness=100.0):
        if rest_length is None:
            rest_length = np.linalg.norm(p2.position - p1.position)
        
        spring = Spring(p1, p2, rest_length, stiffness)
        self.springs.append(spring)
    
    def update(self, dt):
        # Update all particles
        for row in self.particles:
            for particle in row:
                particle.update(dt)
        
        # Apply spring forces
        for spring in self.springs:
            spring.apply_force()
```

## Educational Value

This project is designed for:
- **Students** learning physics and computer science
- **Game developers** wanting to understand physics engines
- **Researchers** in computational physics
- **Educators** teaching physics through programming

### Learning Path
1. Start with basic motion simulations
2. Progress to force calculations and dynamics
3. Explore advanced topics like cloth simulation
4. Implement your own physics-based games

## Customization

### Adding New Simulations
1. Create a new Python file in the appropriate section
2. Follow the existing code structure and naming conventions
3. Include proper documentation and comments
4. Test with various parameters

### Modifying Existing Simulations
- Adjust physical parameters (gravity, friction, etc.)
- Change visual appearance (colors, sizes, shapes)
- Add new interaction methods (keyboard, mouse, gamepad)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Pygame community for excellent documentation
- NumPy team for powerful mathematical tools
- PyMunk developers for the physics engine
- All contributors who have helped improve this project

## Contact

For questions, suggestions, or collaboration opportunities, please open an issue or contact the maintainers.

---

**Happy Learning and Coding!**

*This project is continuously updated with new simulations and improvements. Star this repository to stay updated with the latest changes.*