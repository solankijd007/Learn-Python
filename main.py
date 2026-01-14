from fastapi import FastAPI, Request
from mockData import users
from tdos import UserTDO

app = FastAPI()


@app.get("/")
def home():
    return "Welocome to fastapi jd.."


@app.get("/contact")
def contact():
    return "Contact page.."


@app.get("/users")
def get_users():
    return users

## path params
@app.get("/users/{user_id}")
def get_user(user_id: int):
    
    user = None
    for one_user in users:
        if(one_user.get("id") == user_id):
            return one_user

    return {
        "message": "user not found.."
    }

@app.get("/greet")
def greet(request: Request):
    params = dict(request.query_params)
    return {
        "greet": f"Hello  {params['name']}, your age is {params['age']} "
    }

@app.post("/users/create")
def create_user(user_data:UserTDO):
    user_data = user_data.model_dump()
    users.append(user_data)
    
    return {
        "status": "User created.",
        "data": users
    }

@app.put("/users/update/{user_id}")
def update_user(user_data:UserTDO, user_id: int):
    for index, one_user in enumerate(users):
        if one_user.get("id") == user_id:
            users[index] = dict(user_data)
            return {
                "status": "User Updated..",
                "data": users
            }
    return {
        "status": "User Not Found.."
    }


@app.delete("/users/delete/{user_id}")
def delete_user(user_id:int):
    for index, one_user in enumerate(users):
        if one_user.get("id") == user_id:
            deleted_user = users.pop(index)
            return {
                "status": "User Deleted",
                "data": deleted_user
            }

    return {
        "status": "User not found for this id."
    }

