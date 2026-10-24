import numpy as np
import matplotlib.pyplot as plt

def analyze_simply_supported_beam(L, P, a, E, I):
    """
    Analyzes a simply supported beam with a single point load.
    """
    b = L - a
    R1 = P * b / L  # Reaction force at left support
    R2 = P * a / L  # Reaction force at right support

    x = np.linspace(0, L, 1000)
    V = np.zeros_like(x)
    M = np.zeros_like(x)
    y = np.zeros_like(x)

    for i, xi in enumerate(x):
        if xi < a:
            V[i] = R1
            M[i] = R1 * xi
            y[i] = -(P * b * xi / (6 * E * I * L)) * (L**2 - b**2 - xi**2)
        else:
            V[i] = -R2
            M[i] = R2 * (L - xi)
            y[i] = -(P * a * (L - xi) / (6 * E * I * L)) * (L**2 - a**2 - (L - xi)**2)

    y_mm = y * 1000

    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    # Shear Force Diagram
    axs[0].plot(x, V / 1000, color='crimson', lw=2)
    axs[0].axhline(0, color='black', linewidth=0.8, linestyle='--')
    axs[0].set_ylabel('Shear Force (kN)')
    axs[0].set_title('Simply Supported Beam Analysis (Point Load)')
    axs[0].grid(True, linestyle=':', alpha=0.6)

    # Bending Moment Diagram
    axs[1].plot(x, M / 1000, color='royalblue', lw=2)
    axs[1].axhline(0, color='black', linewidth=0.8, linestyle='--')
    axs[1].set_ylabel('Bending Moment (kNm)')
    axs[1].grid(True, linestyle=':', alpha=0.6)

    # Deflection Profile
    axs[2].plot(x, y_mm, color='darkgreen', lw=2)
    axs[2].axhline(0, color='black', linewidth=0.8, linestyle='--')
    axs[2].set_xlabel('Beam Position x (m)')
    axs[2].set_ylabel('Deflection (mm)')
    axs[2].grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    plt.savefig("beam_deflection_plot.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    L = 5.0          # Beam length: 5 meters
    P = 10000.0      # Point load: 10 kN
    a = 2.0          # Load position: 2 meters from left support
    E = 210e9        # Young's Modulus: 210 GPa (Structural Steel)
    I = 8.33e-6      # Second moment of area (m^4)

    analyze_simply_supported_beam(L, P, a, E, I)
