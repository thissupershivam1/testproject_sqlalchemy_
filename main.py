
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.DB1.User import Base, User
from settings import SQLALCHEMY_DATABASE_URL1, LOG_FILE_PATH1,LOG_FILE_PATH2 , SQLALCHEMY_DATABASE_URL2
import logging,sys

from os.path import dirname, abspath
d=dirname(dirname(abspath(__file__)))
sys.path.append(d)
    



engine1 = create_engine(SQLALCHEMY_DATABASE_URL1)
engine2 = create_engine(SQLALCHEMY_DATABASE_URL2)



Base.metadata.create_all(bind=engine1)
Base.metadata.create_all(bind=engine2)
engine=engine1

if(engine==engine1):
    LOG_FILE_PATH=LOG_FILE_PATH1
else:
    LOG_FILE_PATH=LOG_FILE_PATH2    



logging.basicConfig(level=logging.INFO , filename= LOG_FILE_PATH, filemode="a",format='%(asctime)s %(message)s %(asctime)s - %(levelname)s ') 
logger = logging.getLogger(__name__)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def add_user(username, email, full_name):
    try:
        session = SessionLocal()
        user = User(username=username, email=email, full_name=full_name)
        session.add(user)
        session.commit()
        logger.info(f"Added user: {username}")
    except Exception as e:
        logger.error(f"Error adding user: {username}. Error: {str(e)}")
    finally:
        session.close()

def get_user(username):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.username == username).first()
        logger.info(f"Retrieved user: {username}")
        return user
    except Exception as e:
        logger.error(f"Error retrieving user: {username}. Error: {str(e)}")
    finally:
        session.close()

def update_user(username, new_email):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.username == username).first()
        if user:
            user.email = new_email
            session.commit()
            logger.info(f"Updated email for user: {username} is {new_email}")
        else:
            logger.warning(f"User not found: {username}")
    except Exception as e:
        logger.error(f"Error updating user: {username}. Error: {str(e)}")
    finally:
        session.close()

def upsert_user(username, email, full_name):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.username == username).first()
        if user:
            user.email = email
            user.full_name = full_name
            logger.info(f"Updated user: {username}")
        else:
            user = User(username=username, email=email, full_name=full_name)
            session.add(user)
            logger.info(f"Added user: {username}")
        session.commit()
    except Exception as e:
        logger.error(f"Error upserting user: {username}. Error: {str(e)}")
    finally:
        session.close()


if __name__ == "__main__":
    
    upsert_user("devang", "devang@gmail.com", "Devang Mishra")
    get_user("devang")
    # add_user("u2","u2@gmail.com","u2 kumar")
    # update_user("u2","u232@gmail.com")
    # add_user("abcd","a@gmail.com", "aa cd")
    # add_user("test", "test@gmail.com", "testing")
    add_user("test1", "t1@gmail.com","test world")
   
    
    
    
