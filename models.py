from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, text, Boolean


class Admins(Base):
    __tablename__ = "admins"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    image_name = Column(String, nullable=False, server_default="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxANEhAODg0NDw0NDg0PDQ4NEBANDQ4QFhEXFhUVFRMYHSggGBolGxMTITEhJikrLi4uFyAzODMsNygtLisBCgoKDQ0NEA0PDysZFRkrLTctNzctKysrLTcrKystKzc3LSsrNysrLSsrNysrKy0rKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAbAAEAAwEBAQEAAAAAAAAAAAAAAQQFBgMCB//EADQQAQACAAMEBQsFAQEAAAAAAAABAgMFEQQhMVESQVJhkhUiMjNxgaGxssHREyNCcpGCc//EABYBAQEBAAAAAAAAAAAAAAAAAAABAv/EABYRAQEBAAAAAAAAAAAAAAAAAAABEf/aAAwDAQACEQMRAD8A/RAG2QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfX6kgPkAAAAAAAAAAAAECpEAiQAAAAAAAAAAAAAAAAAAAAAAAIjXd1tHZMqm2+86R1RHF75TsMV/ctvtPCJ6mpozaqrhZfhU4V1nnOqxXDrH8Y/wAfQivO2BSeNY3qmPldLejHRnu4L4I5radjvhelGsdUxweDqsSkWiazwmJiXPbds04VtONZ31lqCsAqAAAAAAAAAAAAAAAAAAC5lezxiX3xrWu+VKW7kuHpTpab7SlVoRAkZVAlAAJBCtt2zxiVndvjfXuWkCOTnlyJWcxw4piWiI47+5Wa0AFQAAAAAAAAAAAAAAABDptirpSvV5sOZdRsvoU/rX5JVewhLKgAAACJSiQYudxpas6cYnXv4M1qZ9xw/Zb7MtUAGkAAAAAAAAAAAAAAAAQ6TLsTpYdZ5Rp/m5zjWyTHjzqTx4xySq1xCWVAAAAEJfN7aRMzwgGHnWLreK9mPnooQ9NqxOna1uczMa8nlDSJAVAQkAAAAAAAAAAAAAAB94GJNLRaOMS+CCq6jAxoxKxaJjv06pernNg2z9Gd+vRnjH3dBh4kWiJid0sK+wAAAGVm+17pw68d3S+axmG2xhRMRvvMTEadU85YFrTMzMzrM8VkR8pBpAAAAAAAAAAAAAAAAAAAgIFQ9tn2q+H6M7uU74eQg1tnznqvX3wsxm2F2p8Nvw58MG7fN8ONdNZ5bpj5qWLmuJbhpWO7izzUwfV7zaZmZmZnmhAqJAAAAAAAAAAAAAAAAAgB9YeHa86ViZ+S9sOW9PffWK7tI65bOFg1pGlaxGiarHwMptO+09HuXKZRhxxm8++Pw0BlVLyVhdmfFJ5LwuzPildAUvJWF2Z8Uo8lYXZnxSvAKPkrC7M+KTyVhdmfFK8Ao+SsLsz4pfNsow54TePZMfeGgAyb5LH8cSffXVUxssxa/wAelHOs6/Di6EXUxyVomN0xMTyndI6jH2emJGl6xPf1x7JYe3ZfbC86POpz649qyimAqAAAAAAAAAAENbLsu/nf3Qr5Ts3Tt0p4V+bfiGbViIhIIqEgAAAAAAAAAAAiY13TwlIDBzPYf0/Pr6Ezvjsz+FB1d6RaJrMaxMaTDmtrwJwrTWerfE846mpUeICoAAAAAAJpWbTERxmYiEL+TYPSv0p4UjX3zw+5VbGybPGFWKx755z1y9gYUAAAAAAAAAAAAAAAAZ2dYHSp04404/1lovjGp0q2r2qzHwByohLbIAAAAAA28ir5lp530/yI/LEb+TR+1Hfa0/HT7JVi8AyoAAAAAAAAAAAAAAAAADldorpe8cr2j4vh67X6zE/9L/VLybZAAAAAAHQ5R6qv/X1S550GUeqr7bfVKVYugMqAAAAAAAAAAAAAAAAAA5nbo/cxP72eCzmcaYt/bHyhWbQAEAAAAHQZR6qvtt9UglWLoDKgAAAAAAAAAAAAAAAIkhIDnc19bf8A5+mFQG4gAIAA/9k=")
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    image_name = Column(String, nullable=False, server_default="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxANEhAODg0NDw0NDg0PDQ4NEBANDQ4QFhEXFhUVFRMYHSggGBolGxMTITEhJikrLi4uFyAzODMsNygtLisBCgoKDQ0NEA0PDysZFRkrLTctNzctKysrLTcrKystKzc3LSsrNysrLSsrNysrKy0rKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAbAAEAAwEBAQEAAAAAAAAAAAAAAQQFBgMCB//EADQQAQACAAMEBQsFAQEAAAAAAAABAgMFEQQhMVESQVJhkhUiMjNxgaGxssHREyNCcpGCc//EABYBAQEBAAAAAAAAAAAAAAAAAAABAv/EABYRAQEBAAAAAAAAAAAAAAAAAAABEf/aAAwDAQACEQMRAD8A/RAG2QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfX6kgPkAAAAAAAAAAAAECpEAiQAAAAAAAAAAAAAAAAAAAAAAAIjXd1tHZMqm2+86R1RHF75TsMV/ctvtPCJ6mpozaqrhZfhU4V1nnOqxXDrH8Y/wAfQivO2BSeNY3qmPldLejHRnu4L4I5radjvhelGsdUxweDqsSkWiazwmJiXPbds04VtONZ31lqCsAqAAAAAAAAAAAAAAAAAAC5lezxiX3xrWu+VKW7kuHpTpab7SlVoRAkZVAlAAJBCtt2zxiVndvjfXuWkCOTnlyJWcxw4piWiI47+5Wa0AFQAAAAAAAAAAAAAAABDptirpSvV5sOZdRsvoU/rX5JVewhLKgAAACJSiQYudxpas6cYnXv4M1qZ9xw/Zb7MtUAGkAAAAAAAAAAAAAAAAQ6TLsTpYdZ5Rp/m5zjWyTHjzqTx4xySq1xCWVAAAAEJfN7aRMzwgGHnWLreK9mPnooQ9NqxOna1uczMa8nlDSJAVAQkAAAAAAAAAAAAAAB94GJNLRaOMS+CCq6jAxoxKxaJjv06pernNg2z9Gd+vRnjH3dBh4kWiJid0sK+wAAAGVm+17pw68d3S+axmG2xhRMRvvMTEadU85YFrTMzMzrM8VkR8pBpAAAAAAAAAAAAAAAAAAAgIFQ9tn2q+H6M7uU74eQg1tnznqvX3wsxm2F2p8Nvw58MG7fN8ONdNZ5bpj5qWLmuJbhpWO7izzUwfV7zaZmZmZnmhAqJAAAAAAAAAAAAAAAAAgB9YeHa86ViZ+S9sOW9PffWK7tI65bOFg1pGlaxGiarHwMptO+09HuXKZRhxxm8++Pw0BlVLyVhdmfFJ5LwuzPildAUvJWF2Z8Uo8lYXZnxSvAKPkrC7M+KTyVhdmfFK8Ao+SsLsz4pfNsow54TePZMfeGgAyb5LH8cSffXVUxssxa/wAelHOs6/Di6EXUxyVomN0xMTyndI6jH2emJGl6xPf1x7JYe3ZfbC86POpz649qyimAqAAAAAAAAAAENbLsu/nf3Qr5Ts3Tt0p4V+bfiGbViIhIIqEgAAAAAAAAAAAiY13TwlIDBzPYf0/Pr6Ezvjsz+FB1d6RaJrMaxMaTDmtrwJwrTWerfE846mpUeICoAAAAAAJpWbTERxmYiEL+TYPSv0p4UjX3zw+5VbGybPGFWKx755z1y9gYUAAAAAAAAAAAAAAAAZ2dYHSp04404/1lovjGp0q2r2qzHwByohLbIAAAAAA28ir5lp530/yI/LEb+TR+1Hfa0/HT7JVi8AyoAAAAAAAAAAAAAAAAADldorpe8cr2j4vh67X6zE/9L/VLybZAAAAAAHQ5R6qv/X1S550GUeqr7bfVKVYugMqAAAAAAAAAAAAAAAAAA5nbo/cxP72eCzmcaYt/bHyhWbQAEAAAAHQZR6qvtt9UglWLoDKgAAAAAAAAAAAAAAAIkhIDnc19bf8A5+mFQG4gAIAA/9k=")
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class Drinks(Base):
    __tablename__ = "drinks"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    kind = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
    image = Column(String, nullable=True)


class ChangePasswordCode(Base):
    __tablename__ = "changepasswordcodes"
    id = Column(Integer, nullable=False, primary_key=True)
    code = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, nullable=False, primary_key=True)
    message = Column(String, nullable=False)
    is_read = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


