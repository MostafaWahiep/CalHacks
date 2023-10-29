"""Base state for Twitter example. Schema is inspired by https://drawsql.app/templates/twitter."""
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

import reflex as rx
from datetime import datetime
from sqlmodel import Field, Relationship
from typing import Optional

class Follows(rx.Model, table=True):
    """A table of Follows. This is a many-to-many join table.

    See https://sqlmodel.tiangolo.com/tutorial/many-to-many/ for more information.
    """

    followed_username: str = Field(primary_key=True)
    follower_username: str = Field(primary_key=True)

class ValidatorModelLink(rx.Model, table=True):
    validator_id: int = Field(foreign_key="validator.id", primary_key=True, default=None)
    model_id: int = Field(foreign_key="model.id", primary_key=True, default=None)


class Validator(rx.Model, table=True):
    """A table of Validators."""
    id : Optional[int] = Field(default=None, primary_key=True)
    username: str = Field()
    password: str = Field()

    models: list["Model"] = Relationship(back_populates="validators", link_model=ValidatorModelLink)
    labeleds: list["Labeled"] = Relationship(back_populates="validators")


class User(rx.Model, table=True):
    """A table of Users."""
    id : Optional[int] = Field(default=None, primary_key=True)
    username: str = Field()
    password: str = Field()

    labeleds: list["Labeled"] = Relationship(back_populates="users")

class Label(rx.Model, table=True):
    """A table of Labels."""
    id : Optional[int] = Field(default=None, primary_key=True)
    name: str = Field()
    model_id: int = Field(foreign_key="model.id")

    models: Optional["Model"] = Relationship(back_populates="labels")
    labeleds: list["Labeled"] = Relationship(back_populates="labels")

class Model(rx.Model, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name: str = Field()
    dataset: str = Field()
    notebook: str = Field()
    model_file: str = Field()
    dataset_size: int = Field()
    last_update: str = Field(default=None)
    new_data_counter: int = Field(default=0)

    labels: list[Label] = Relationship(back_populates="models")
    labeleds: list["Labeled"] = Relationship(back_populates="models")
    validators: Optional[Validator] = Relationship(back_populates="models", link_model=ValidatorModelLink)


    def update(self):
        self.last_update = datetime.now()

    def increment(self):
        self.new_data_counter += 1

    def reset(self):
        self.new_data_counter = 0

    def __repr__(self):
        return f"<Model {self.name}>"
    



# Labeled: ID, user_id, model_id, image, expected_label_id, is_validated, validator_id, correct_label_id, is_pushed
class Labeled(rx.Model, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    model_id: int = Field(foreign_key="model.id")
    image: str = Field()
    expected_label_id: int = Field(default=None, foreign_key="label.id")
    is_validated: bool = Field(default=False)
    validator_id: int = Field(default=None, foreign_key="validator.id")
    #correct_label_id: int = Field(default=None, foreign_key="label.id")
    is_pushed: bool = Field(default=False)

    users: Optional["User"] = Relationship(back_populates="labeleds")
    models: Optional["Model"] = Relationship(back_populates="labeleds")
    labels: Optional["Label"] = Relationship(back_populates="labeleds")
    validators: Optional["Validator"] = Relationship(back_populates="labeleds")

    def __repr__(self):
        return f"<Labeled {self.id}>"


class Tweet(rx.Model, table=True):
    """A table of Tweets."""

    content: str = Field()
    created_at: str = Field()
    author: str = Field()
    favorite_count: int = Field()


engine = create_engine("sqlite:///reflex.db")
SQLModel.metadata.create_all(engine)

class State(rx.State):
    """The base state for the app."""

    user: Optional[User] = None
    usertype: Optional[str] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None
