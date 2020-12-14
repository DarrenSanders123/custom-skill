from mycroft import MycroftSkill, intent_file_handler


class Custom(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('custom.intent')
    def handle_custom(self, message):
        self.speak_dialog('custom')


def create_skill():
    return Custom()

