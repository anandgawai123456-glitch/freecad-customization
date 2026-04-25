# ANAND-CAD (FreeCAD Customization)

## Overview
This project is based on the open-source FreeCAD software.  
I successfully built FreeCAD from source and performed basic customization and scripting within the environment.

## Work Done

### 1. Source Build
- Compiled FreeCAD from source on Windows
- Used tools: CMake, MSVC, Ninja, Qt, Boost
- Resolved build and dependency issues

### 2. Customization (ANAND-CAD)
- Modified application visuals (splash screen)
- Explored UI-level customization to reflect ANAND-CAD branding

### 3. Python Tool Development
- Created a custom Python script inside FreeCAD
- Implemented:
  - Pyramid creation (50mm x 50mm base, 100mm height)
  - Basic model handling using FreeCAD API

### 4. Understanding Gained
- Working with large C++ codebases
- Build systems and dependency management
- FreeCAD Python API and scripting
- Basic GUI customization concepts

## Project Structure
- `pyramid_tool.py` → Python script for model creation  
- `splash.png` → Custom splash screen  

## How to Run

1. Install and open FreeCAD  
2. Open Python Console  
3. Run the script:
   ```python
   exec(open("pyramid_tool.py").read())
Note

This project focuses on customization and scripting.
The full FreeCAD source code is not included.

Author

Anand Gawai
