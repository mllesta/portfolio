import json
from reflex.base import Base
from typing import List, Optional


class Media(Base):
    email: str
    cv: str
    github: str
    linkedin: str


class Technology(Base):
    icon: str
    name: str

        
class Info(Base):
    icon: str
    title: str
    subtitle: str
    description: str
    date: Optional[str] = ""
    certificate: Optional[str] = ""
    technologies: List[Technology] = []
    image: Optional[str] = ""
    url: Optional[str] = ""
    github: Optional[str] = ""


class Extra(Base):
    image: str
    title: str
    description: str
    url: str


class Data(Base):
    title: str
    description: str
    image: str
    avatar: str
    name: str
    skill: str
    location: str
    media: Media
    about: str
    technologies: List[Technology]
    experience: List[Info]
    projects: List[Info]
    training: List[Info]
    extras: List[Extra]
    

with open("assets/data/data.json") as file:
    json_data = json.load(file)


data = Data(**json_data)