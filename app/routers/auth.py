from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from .. import oauth2
from .. import database,schemas,models,utils

router = APIRouter(tags=['authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invaild Credentials")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
    return {"access_token": access_token , "token_type": "bearer"}
