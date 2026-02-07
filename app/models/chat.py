from sqlalchemy import Column, Integer, String

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    role = Column(String)  # user / ai
    content = Column(String)
