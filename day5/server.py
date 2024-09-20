from fastapi.responses import HTMLResponse
@app.get("/", response_class=HTMLResponse)
def get_index():
  with open('index.html', 'r') as file:
    return file.read() 