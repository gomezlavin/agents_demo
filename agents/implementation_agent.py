import os

class ImplementationAgent:
    def __init__(self, name, client):
        self.name = name
        self.client = client

    async def execute(self, message_history):
        print("Executing Implementation Agent...")  # Debugging

        # Generate the content for index.html and styles.css
        html_content = "<!DOCTYPE html>\n<html>\n<head>\n<link rel='stylesheet' href='styles.css'>\n</head>\n<body>\n<h1>Generated Page</h1>\n</body>\n</html>"
        css_content = "body { font-family: Arial, sans-serif; background-color: #f4f4f4; } h1 { color: #333; }"

        # Define the path to the artifacts folder
        artifacts_folder = "artifacts"

        # Ensure the folder exists
        if not os.path.exists(artifacts_folder):
            print(f"Creating artifacts folder at {artifacts_folder}...")  # Debugging
            os.makedirs(artifacts_folder)

        # Write the index.html file
        index_path = os.path.join(artifacts_folder, "index.html")
        with open(index_path, "w") as f:
            print(f"Writing index.html to {index_path}...")  # Debugging
            f.write(html_content)

        # Write the styles.css file
        css_path = os.path.join(artifacts_folder, "styles.css")
        with open(css_path, "w") as f:
            print(f"Writing styles.css to {css_path}...")  # Debugging
            f.write(css_content)

        return "Files created: index.html and styles.css"