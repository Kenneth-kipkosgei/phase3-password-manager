from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Password(Base):
    __tablename__ = 'passwords'
    
    id = Column(Integer, primary_key=True)
    site_name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    encrypted_password = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="passwords")
    category = relationship("Category", back_populates="passwords")
    
    def __repr__(self):
        return f"<Password(site='{self.site_name}', user='{self.username}')>"