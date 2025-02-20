from node_editor.node import Node

class choice_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Choice"
        self.type_text = "XML Nodes"
        self.set_color(title_color=(255, 0, 0))

        self.add_pin(name="Ex In", is_output=False, execution=True)
        self.add_pin(name="Ex Out", is_output=True, execution=True)
        #TODO: add hidden and req options (required)
        self.add_pin(name="Choice Output0", is_output=True)
        self.add_pin(name="Choice Output1", is_output=True)
        self.add_pin(name="Choice Output2", is_output=True)
        self.add_pin(name="Choice Output3", is_output=True)
        self.add_pin(name="Choice Output4", is_output=True)
        self.add_pin(name="Choice Output5", is_output=True)
        self.add_pin(name="Choice Output6", is_output=True)
        self.build()


# Add more node classes for different XML tags

# Example usage:
# event_node = EventNode()
# choice_node = ChoiceNode()
# text_node = TextNode()
# play_sound_node = PlaySoundNode()
