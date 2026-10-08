from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from app.database import engine
from app.models import User

with Session(engine) as session:

    user = session.query(User).filter_by(id=1).first()

    if user:
        user.name = "Nagalakshmi"
        user.email = "admin@gmail.com"
        user.password = generate_password_hash("admin@123")
        user.role = "admin"

        session.commit()

        print("Admin user updated successfully.")
    else:
        user = User(
            name="Nagalakshmi",
            email="admin@gmail.com",
            password=generate_password_hash("admin@123"),
            role="admin"
        )

        session.add(user)
        session.commit()

        print("Admin user created successfully.")