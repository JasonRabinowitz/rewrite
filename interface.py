try:
    import installer
    import toga
    from toga.style.pack import *
except ImportError:
    pass

def build(app):
    def installHandle(widget):
        import installer
        result_label.value = installer.full_install(package_input.value)
    #Ian Test code
    package_list = [
        {'Discord', 'Chat for Gamers'},
        {'Google Chrome', 'Web Browser'},
        {'Dropbox', 'Upload/Download Files'}
        ]
    left_container = toga.Table(headings=['Package', 'Description'], data=package_list)
    right_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))

    #Add content to right side
    packageBox = toga.Box()
    text_label = toga.Label('Package:')
    package_input = toga.TextInput()
    submit = toga.Button('Install Package', on_press=installHandle)
    packageBox.add(text_label)
    packageBox.add(package_input)
    packageBox.add(submit)
    resultBox = toga.Box()
    result_label = toga.TextInput(readonly = True)
    result_text = toga.Label('Status:')
    resultBox.add(result_text)
    resultBox.add(result_label)
    right_content.add(packageBox)
    right_content.add(resultBox)

    right_container = toga.ScrollContainer(horizontal=False)
    right_container.content = right_content

    split = toga.SplitContainer()
    split.content = [left_container, right_container]
    things = toga.Group('Things')






    return split

    #Current
    # def installHandle(widget):
    #     import installer
    #     resultInput.value = installer.full_install(packageInput.value)
    # box = toga.Box()
    # packageBox = toga.Box()
    # packageLabel = toga.Label('Package To Install:')
    # packageInput = toga.TextInput()
    # discordInput = 'discord'
    # submitBox = toga.Box()
    # install = toga.Button('Install Package', on_press=installHandle)
    # resultBox = toga.Box()
    # resultInput = toga.TextInput(readonly = True)
    # discordButton = toga.Button('Discord', on_press=installHandle)
    # chromeButton = toga.Button('Google Chrome', on_press=installHandle)

    ##packageBox.add(packageLabel)
    ##packageBox.add(packageInput)
    ##submitBox.add(install)
    ##resultBox.add(resultInput)
    ##box.add(packageBox)
    ##box.add(submitBox)
    ##box.add(resultBox)
    # box.add(discordButton)
    # box.add(chromeButton)
    #
    # box.style.update(direction=COLUMN, padding_top=10)
    # packageBox.style.update(direction=ROW, padding=5)
    # submitBox.style.update(direction=ROW, padding=5)
    # return box

def start():
    return toga.App('Yet Another Package Installer',
                    'org.YAPI.rewrite', startup=build).main_loop()

def main():
    start().main_loop()
