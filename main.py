import numpy as np
import matplotlib.pyplot as plt

c = 3e8  #speed of light in m/s
G = 6.67430e-11  #gravitational constant

#check for CTC formation
def check_ctc(omega, rho, L, R):
    #Example condition for CTC formation (simplified for demonstration)
    #Real condition is much more complex and derived from general relativity
    ctc_condition = (2 * np.pi * omega * R) / c > 1
    return ctc_condition

#calculate riemann curvature tensor (simplified for demonstration)
def calculate_riemann_tensor(omega, rho, L, R):
    #simplified Riemann tensor calculation
    riemann_tensor = np.array([
        [0, -omega * R, 0, 0],
        [omega * R, 0, 0, 0],
        [0, 0, 0, rho * G],
        [0, 0, rho * G, 0]
    ])
    return riemann_tensor

#to assess stability
def assess_stability(omega, rho, L, R):
    #simplified stability condition
    stability_condition = (rho * G * L) / (R * c**2) < 1
    return stability_condition

#to optimize cylinder parameters
def optimize_parameters(criterion='maximize_ctc'):
    #simplified example to maximize CTC formation
    optimal_omega = 1.5 * c / (2 * np.pi * 1)
    optimal_rho = 1e17
    optimal_L = 1e7
    optimal_R = 1
    return optimal_omega, optimal_rho, optimal_L, optimal_R

#to plot CTC visualization
def plot_ctc(omega, rho, L, R):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = R * np.cos(theta)
    y = R * np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label="Possible CTC Region")
    plt.fill_between(x, y, color='lightblue', alpha=0.5)
    plt.title(f"CTC Visualization for omega={omega}, rho={rho}, L={L}, R={R}")
    plt.xlabel("X (meters)")
    plt.ylabel("Y (meters)")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

#to plot Riemann Curvature Tensor
def plot_riemann_tensor(riemann_tensor):
    plt.figure(figsize=(8, 6))
    plt.imshow(riemann_tensor, cmap='viridis', origin='lower')
    plt.colorbar(label='Value')
    plt.title("Riemann Curvature Tensor")
    plt.xlabel("Index j")
    plt.ylabel("Index k")
    plt.xticks(np.arange(4), ['0', '1', '2', '3'])
    plt.yticks(np.arange(4), ['0', '1', '2', '3'])
    plt.grid(False)
    plt.show()

#to plot time against space
def plot_time_vs_space(omega, rho, L, R):
    t = np.linspace(0, 10, 100)  #time var
    x = np.linspace(0, L, 100)   #space var

    X, T = np.meshgrid(x, t)
    Z = np.sin((2 * np.pi * omega * X) / L)  #example of time wrapping

    plt.figure(figsize=(10, 6))
    plt.contourf(X, T, Z, cmap='viridis', levels=50)
    plt.colorbar(label='Time Wrapping')
    plt.title(f"Time vs Space for omega={omega}, rho={rho}, L={L}, R={R}")
    plt.xlabel("Space (meters)")
    plt.ylabel("Time (arbitrary units)")
    plt.show()


def main():
    #recommended values that trigger CTC formation
    rec_omega = 71619724.3913529
    rec_rho = 1e17
    rec_L = 1e7
    rec_R = 1

    #inputs
    omega = float(input(f"Enter angular velocity (omega) in rad/s (recommended: {rec_omega}): ") or rec_omega)
    rho = float(input(f"Enter density (rho) in kg/m^3 (recommended: {rec_rho}): ") or rec_rho)
    L = float(input(f"Enter length (L) in meters (recommended: {rec_L}): ") or rec_L)
    R = float(input(f"Enter radius (R) in meters (recommended: {rec_R}): ") or rec_R)

    #check for CTC formation
    ctc_formation = check_ctc(omega, rho, L, R)
    print("\nCTC Formation:", "Yes" if ctc_formation else "No")

    #calculate Riemann curvature tensor
    riemann_tensor = calculate_riemann_tensor(omega, rho, L, R)
    print("\nRiemann Curvature Tensor:\n", riemann_tensor)

    #plot Riemann Curvature Tensor
    plot_riemann_tensor(riemann_tensor)

    #assess stability
    stability = assess_stability(omega, rho, L, R)
    print("\nStability:", "Stable\n" if stability else "Unstable")

    #plot CTC visualization
    if ctc_formation:
        plot_ctc(omega, rho, L, R)
    else:
        print("No CTC formation, skipping plot.")

    #if time travel is possible
    if ctc_formation:
        print("\nBased on the input parameters time travel is theoretically possible All aboard the AIC starship.\n")
    else:
        print("\nBased on the input parameters, time travel is not possible.\n")

    #plot time vs space
    plot_time_vs_space(omega, rho, L, R)

    #optimize parameters
    optimal_omega, optimal_rho, optimal_L, optimal_R = optimize_parameters()
    print("\nOptimal Parameters:")
    print(f"  Angular Velocity (omega): {optimal_omega} rad/s")
    print(f"  Density (rho): {optimal_rho} kg/m^3")
    print(f"  Length (L): {optimal_L} meters")
    print(f"  Radius (R): {optimal_R} meters")

if __name__ == "__main__":
    main()
