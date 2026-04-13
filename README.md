# 🚀 ISRO Moon Rover Navigation System

## 📌 Overview
This project simulates the navigation of robotic rovers deployed by ISRO on a rectangular plateau on the Moon.

---

## 🧠 Problem Statement
- Plateau grid: (0,0) to (maxX, maxY)
- Rover has:
  - Position (x, y)
  - Direction (N, E, S, W)

---

## 🔧 Instructions
- L → Turn Left
- R → Turn Right
- M → Move Forward

---

## 🖥️ Sample Input
5 5  
1 2 N  
LMLMLMLMM  
3 3 E  
MMRMMRMRRM  

---

## ✅ Sample Output
1 3 N  
5 1 E  

---

## ⚙️ Approach
- Use direction array [N, E, S, W]
- Rotate using modulo
- Maintain boundary conditions

---

## 📂 Files
- rover_navigation_fixed.py  
- Assignment_AnushikaGupta.pdf  
- README.md  

