# ADMM Notes, Implemetation and Application

## Basic Form and Scaled Form

2-block optimization problem:
$$
\begin{aligned}
    & \textmd{minimize} \ f(x)+g(z) \\
    & \textmd{s.t.} \ Ax+Bz=c
\end{aligned}
$$

Basic ADMM use the augmented Lagrangian:
$$
L_\rho (x,z,u)=f(x)+g(z)+u^T(Ax+Bz-c)+(\rho /2)\|Ax+Bz-c\|^2
$$
Scaled ADMM use such Lagrangian(equivalent to basic form):
$$
L_\rho (x,z,w)=f(x)+g(z)+(\rho /2)\|Ax+Bz-c+w\|^2-(\rho /2)\|w\|^2
$$
Iteration loop for scaled ADMM:
$$
\begin{aligned}
    & x^{k+1}:=\argmin{(f(x)+(\rho/2)\|Ax+Bz^k-c+w^k\|^2)}\\
    & z^{k+1}:=\argmin{(g(z)+(\rho/2)\|Ax^{k+1}+Bz-c+w^k\|^2)}\\
    & w^{k+1}:=w^k+Ax^{k+1}+Bz^{k+1}-c
\end{aligned}
$$

## Convergence and Termination Condition

We will make two assumptions first.

Assumption 1. The (extended-real-valued) functions $f: \mathbf{R}^n \to \mathbf{R} \cup \{+\infty\}$ and $g: \mathbf{R}^m \to \mathbf{R} \cup \{+\infty\}$ are closed, proper, and convex.

Assumption 2. The unaugmented Lagrangian $L_0$ has a saddle point.

Under assumptions 1 and 2, the ADMM iteration satisfy the following:

- Residual convergence. $r^k \to 0$ as $k \to \infty$, i.e., the iterates approach feasibility.
- Objective convergence. $f(x^k) + g(z^k) \to p^*$ as $k \to \infty$, i.e., the objective function of the iterates approaches the optimal value.
- Dual variable convergence. $y^k \to y^*$ as $k \to \infty$, where $y^*$ is a dual optimal point.

***Note that $x_k$ and $z_k$ need not converge to optimal values, although such results can be shown under additional assumptions!***

Terminal condition in practice(residual convergence):
$$
\|r^k\| \leq \epsilon^{pri} \ \textmd{and} \ \|s^k\| \leq \epsilon^{dual}
$$
where $\epsilon^{pri}$ and $\epsilon^{dual}$ are positive and ususally adaptive. These tolerances can be chosen using an absolute and relative criterion, such as

$$
\begin{aligned}\epsilon^{\mathrm{pri}}&=\sqrt{p}\:\epsilon^{\mathrm{abs}}+\epsilon^{\mathrm{rel}}\max\{\|x^k\|_2,\|z^k\|_2\},\\\epsilon^{\mathrm{dual}}&=\sqrt{n}\:\epsilon^{\mathrm{abs}}+\epsilon^{\mathrm{rel}}\|A^Ty^k\|_2,\end{aligned}
$$

Python code segment:

    # objective values: residual & target function value & dual variable convergence
    history['objval'] = np.append(history['objval'], objective_f(x, z, A, b, lamb))
    history['r_norm'] = np.append(history['r_norm'], np.linalg.norm(x - z))
    history['s_norm'] = np.append(history['s_norm'], np.linalg.norm(-rho * (z - zold)))
    history['eps_pri'] = np.append(history['eps_pri'], np.sqrt(n) * ABSTOL + RELTOL * max(np.linalg.norm(x), np.linalg.norm(-z)))
    history['eps_dual'] = np.append(history['eps_dual'], np.sqrt(n) * ABSTOL + RELTOL * np.linalg.norm(rho * u))

    # termination checks
    if history['r_norm'][k] < history['eps_pri'][k] and history['s_norm'][k] < history['eps_dual'][k]:
        break

## Proxiaml Operator

Definition: $\bold{prox}_{f,\rho}(v)=\argmin_{x}{(f(x)+(\rho/2)\|x-v\|^2)}$

Possible uses in quadratic objective functions:

- test
- run

## LASSO Problem

### $l_1$-Norm Problems

run2
