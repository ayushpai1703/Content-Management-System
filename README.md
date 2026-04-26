🚀 ElectroLab – Django CMS

ElectroLab is a Content Management System (CMS) built using Django, designed to manage and publish blog-style content dynamically. It provides an intuitive admin interface for content management and a clean frontend for users to explore posts.

📌 Features
📝 Create, edit, and delete blog posts
🏷️ Slug-based URLs for posts
🖼️ Image upload support
📊 Post status control (Draft/Publish)
👤 Admin dashboard for content management
📄 Dynamic “About” section
🔐 Built-in authentication system
⚡ Clean and responsive frontend UI

🏗️ Tech Stack
Backend: Python, Django
Frontend: HTML, CSS (Bootstrap if used)
Database: SQLite
Others: Django Admin Panel

📂 Project Structure
gfgblog/
│── blog/              # Main app (models, views, templates)
│── gfgblog/           # Project settings
│── media/             # Uploaded images
│── db.sqlite3         # Database
│── manage.py          # Django control file

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create & activate virtual environment
python -m venv ENV
ENV\Scripts\activate   # Windows
3. Install dependencies
pip install django

(or use requirements.txt if available)

4. Apply migrations
python manage.py migrate
5. Create superuser
python manage.py createsuperuser
6. Run the server
python manage.py runserver

🌐 Usage
Open: http://127.0.0.1:8000/ → View website
Open: http://127.0.0.1:8000/admin/ → Admin panel

Use the admin panel to:

Add/edit blog posts
Upload images
Update About section

🧠 Key Concepts Demonstrated
Django MVT (Model-View-Template) architecture
CRUD operations
Admin panel customization
Media file handling
Dynamic content rendering
📸 Screenshots

(You can add your screenshots here later)

✨ Future Improvements
User authentication for frontend users
Comment system
Search & filtering
Rich text editor (CKEditor)
Deployment (AWS / Render / Vercel backend)
📜 License

This project is for learning and demonstration purposes.
