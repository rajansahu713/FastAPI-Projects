from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

count = 0
templates = Jinja2Templates(directory="templates")
tasks_db =[]


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", 
                                      {"request": request, 
                                       "tasks": tasks_db})


@app.post("/")
async def add_task(request: Request, task: str = Form(...), descriptions: str = Form(...)):
    global count
    data = {"id": count, 'title': task, "descriptions": descriptions}
    tasks_db.append(data)
    count += 1
    return RedirectResponse(url="/", status_code=303)


@app.post("/delete-task/", response_class=HTMLResponse)
async def delete_task(request: Request, task_index: int = Form(...)):
    for i, task in enumerate(tasks_db):
        if int(task['id']) == int(task_index):
            del tasks_db[i]
    return RedirectResponse(url="/table", status_code=303)


@app.get("/table", response_class=HTMLResponse)
async def read_data(request: Request):
    return templates.TemplateResponse("tables.html", 
                                      {"request": request, 
                                       "tasks": tasks_db})


@app.get("/update-task/", response_class=HTMLResponse)
async def update_task(request: Request, task_index: int = Query(...)):
    for task in tasks_db:
        if task['id'] == task_index:
            print(task)
            return templates.TemplateResponse("update.html", 
                                              {"request": request, 
                                               "tasks": task})
        

@app.post("/update-task")
async def add_task(request: Request, id: str = Form(...), title: str =Form(...), descriptions: str = Form(...)):
    for i, task in enumerate(tasks_db):
        if int(task['id']) == int(id):
            del tasks_db[i]

    data = {"id": int(id), 'title': title, "descriptions": descriptions}
    tasks_db.append(data)
    return RedirectResponse(url="/table", status_code=303)