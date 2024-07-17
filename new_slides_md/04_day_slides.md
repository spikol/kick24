---
title: Day 4 Kickstart
description: Day 4 - FSM
paginate: true
marp: true
---

# Kickstart-kursus i programmering 23 dag 4
**Daniel Spikol**  
*ds@di.ku.dk*

**DIKU \\ Københavns Universitet**  
**17. august 2023**

![height:1.5cm](ku_logo_dk)

---

# Recap from Wednesday
- Scoping
- Conditionals
- Projects

---

# Thursday IFOs
- Finite State Machines
- Wrapping up Things
- Projects and Demos

---

# Finite State Machines- FSM

- A Finite State Machine (FSM) is a mathematical model of computation used to design algorithms.
- In the context of computer games, FSMs are often used for character behaviour, where different states might represent actions like "idle", "attack", "defend", or "flee", and game events or conditions determine transitions between states.

---

# The STATES in a FSM
- **Discrete States:** An FSM consists of a limited or finite number of states. It can be in just one of these states at any given moment. Transitions define how it changes from one state to another based on inputs or conditions.
- **Transitions & Triggers:** Events or conditions trigger transitions between states. Each state specifies which state the machine will move to next for each possible input.
- **Start and End States:** Among the finite states, there is one initial state where the FSM begins its operation. Additionally, there can be one or more end states where the FSM is considered to be completed or final.

---

# The Classic Example

```tikz
\begin{tikzpicture}[shorten >=1pt, node distance=4cm, on grid, auto]
    \node[state, initial] (R)   {RED};
    \node[state] (Y) [right=of R] {YELLOW};
    \node[state] (G) [right=of Y] {GREEN};
    
    \path[->]
    (R) edge[bend right] node {to GREEN} (G)
    (G) edge[bend right] node {to YELLOW} (Y)
    (Y) edge[bend right] node {to RED} (R);
\end{tikzpicture}

---
# Mathematical Abstraction of the FSM

---
# Game States

---

# Mario States

---

# The Traffic Light Example


---
 # FSM Code Example


 ---
 # How do you add Yellow?

 ---
