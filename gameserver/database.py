from db_config import get_connection


async def init_db():
    async with get_connection() as conn:

        # creating the user table
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS User(
                id INTERGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL                   
            )
        """)

        await conn.commit()    



class UserDatabaseUtils:


    async def create_user(username: str, email: str, password: str):
        async with get_connection() as conn:
            await conn.execute("""
                    INSERT INTO User(username, email, password) VALUES
                    (:username,:email,:password)
                """, 
                {"username": username, "email": email, "password": password}
            )
        
            await conn.commit()
    

    async def get_user_by_email_id(user_email_id: int):
        async with get_connection() as conn:
            result = await conn.execute("""SELECT * from User where email=:email""", 
                                        {"email": user_email_id})
            row = result.fetchone()
            return row
    
    
