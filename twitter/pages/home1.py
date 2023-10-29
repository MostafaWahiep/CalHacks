import reflex as rx
import asyncio
import os, random
from typing import List
from ..state.base import State, Model, Labeled


# Main State
class UploadState(State):

    # test selection
    option: str

    """The app state."""
    # The upload picture state ----
    # Whether we are currently uploading files.
    is_uploading: bool

    # list of image to show
    img: list[str]

    @rx.var
    def file_str(self) -> str:
        """Get the string representation of the uploaded files."""
        return "\n".join(os.listdir(rx.get_asset_path()))

    @rx.var
    def options(self) -> list[str]:
        with rx.session() as session:
            return [model.name for model in session.query(Model).all()]

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the file upload."""
        self.clear_files()
        self.is_uploading = True
        # Iterate through the uploaded files.
        for file in files:
            upload_data = await file.read()
            outfile = 'assets\\' + file.filename

            # save the file
            with open(outfile,  "wb") as file_object:
                file_object.write(upload_data)
                await asyncio.sleep(1)
                print(outfile)
                print(file.filename)

            self.img.append('\\'+file.filename)

        # Stop the upload.
        return UploadState.stop_upload
    
    def clear_files(self):
        self.img = []
    
    def predicte(self):
        if self.option == "":
            return rx.window_alert("Please select a model")
        elif self.img == []:
            return rx.window_alert("Please upload a file")
        elif self.option == "Natural Images":
            return rx.window_alert("Sorry, this model is not available yet")
        else:
            with rx.session() as session:
                model = session.exec(Model.select.where(Model.name == self.option)).first()
                label = model.labels[random.randint(0, len(model.labels)-1)]
                labeled = Labeled(user_id = self.user.id, model_id = model.id, image = self.img[0], expected_label_id = label.id)
                session.add(labeled)
                session.commit()
                self.img = []
                return rx.window_alert("expexted: "+label.name)
            


    async def stop_upload(self):
        """Stop the file upload."""
        await asyncio.sleep(1)
        self.is_uploading = False


def navbar():
    return rx.box(
        rx.hstack(
            # rx.image(src="favicon.ico"),
            rx.heading("OKOK"),
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
    )

color = "rgb(107,99,246)"

def upload() -> rx.Component:
    """The main view."""
    return rx.vstack(
        # dropdown menu
        select(),

        # upload component
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            multiple=False,
            accept={
                "application/pdf": [".pdf"],
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                "image/gif": [".gif"],
                "image/webp": [".webp"],
                "text/html": [".html", ".htm"],
            },
            max_files=1,
            disabled=False,
            on_keyboard=True,
            border=f"1px dotted {color}",
            padding="5em",
        ),
        
        rx.hstack(
                    rx.button(
                        "Upload",
                        on_click=lambda: UploadState.handle_upload(
                            rx.upload_files()
                        ),
                    ),
                    rx.button(
                        "Clear",
                        on_click=UploadState.clear_files,
                    ),
                    rx.button(
                        "Submit",
                        on_click=UploadState.predicte,
                    ),
                ),

        # submit button
        # rx.button(
        #     "Submit",
        #     o
        # )

        rx.hstack(rx.foreach(rx.selected_files, rx.text)),

        rx.responsive_grid(
            rx.foreach(
                UploadState.img,
                lambda img: rx.vstack(
                    rx.image(src=img),
                    rx.text(img),
                ),
            ),
            columns=[2],
            spacing="5px",
            align="center",
        ),
        padding="5em",
    )

def select() -> rx.Component:
    return rx.vstack(
        rx.select(
            UploadState.options,
            placeholder="Select an example.",
            on_change=UploadState.set_option,
            color_schemes="twitter",
        ),
    )

def home1() -> rx.Component:
    return rx.box(
        upload(),
    )

