# CPE106L_E01_3T24525
# 🌿 Mindful Balance

Mindful Balance is a minimalist desktop wellness application that allows users to log moods, write journal entries, and view emotional trends. Built using Python, Flet, and FastAPI, the app runs locally to prioritize privacy, simplicity, and ease of use.

---

## ⚙️ Setup Instructions

### 🔧 Ubuntu Virtual Machine (VM)

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd MindfulBalance

Install dependencies:
pip install fastapi uvicorn flet httpx bcrypt matplotlib

Start FastAPI backend:
uvicorn backend.api:app --reload

Run frontend:
python3 frontend/main.py


Windows Terminal
Clone the repository
:
git clone https://github.com/Donnmrc/CPE106L_E01_3T24525
cd MindfulBalance

Install dependencies:
pip install fastapi uvicorn flet httpx bcrypt matplotlib

Start FastAPI backend:
uvicorn backend.api:app --reload

How to Run the Application

    Ensure all dependencies are installed (see above).

    Run the backend server using Uvicorn.

    Launch the frontend using Python and Flet.

    The app opens directly to the mood input screen and follows a simple flow: Mood → Journal → Insights.
    
    
    Dependencies

    fastapi

    uvicorn

    flet

    httpx

    bcrypt

    matplotlib

    sqlite3 (built-in)
    
    
System Design
Frontend	Flet (Python)	Builds a simple desktop UI for mood input, journaling, and viewing insights.
Backend	FastAPI (Python)	Serves RESTful API endpoints for logging data and retrieving statistics.
Database	SQLite	Stores mood entries and journal logs locally without user authentication.
Communication	httpx (Python)	Facilitates HTTP requests between frontend and backend components.
Visualization	Matplotlib (optional)	Used for generating charts based on stored mood data.
Routing	Flet's View system	Enables screen transitions across Mood Input, Journal, and Insights views.
Design Theme	Minimalist, calm	Uses soft blues and greys, rounded inputs, and clean layout for focus and ease.


Team Members and Roles
Name	Roles
Ancheta	Coding, Document Creation, Database Creation
Lintag	Coding, Document Creation, Database Creation



