import eel  # type: ignore

# Initialize the Eel application with the folder name
eel.init('mywebsir')

@eel.expose
def App():  # Main function for the app
    print('Application running')

# Start the Eel application
App()
eel.start('index.html', size=(500, 600))  # Corrected the size parameter
