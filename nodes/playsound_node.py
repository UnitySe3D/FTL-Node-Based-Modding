from node_editor.node import Node
from nodes.common_widgets import FloatLineEdit


class playsound_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "PlaySound"
        self.type_text = "XML Nodes"
        self.set_color(title_color=(255, 0, 0))

        self.add_pin(name="Ex In", is_output=False, execution=True)
        self.add_pin(name="Ex Out", is_output=True, execution=True)

        self.add_pin(name="AudioFile", is_output=False)
        self.build()
