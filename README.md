# Beam Deflection & Bending Moment Solver

A Python computational tool for analyzing simply supported beams under concentrated point loads, generating Shear Force Diagrams (SFD), Bending Moment Diagrams (BMD), and elastic deflection curves.

## 📌 Features
- **Reaction Forces:** Computes static support reactions ($R_1, R_2$).
- **Internal Forces:** Calculates continuous Shear Force ($V$) and Bending Moment ($M$) distributions using Macaulay's approach.
- **Deflection Analysis:** Computes elastic curve deflections under Euler-Bernoulli beam theory.
- **Technical Visualization:** Automatically outputs a 3-panel synchronized Matplotlib figure.

## 🛠️ Usage
1. Install dependencies:
   ```bash
   pip install numpy matplotlib
