import os

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    password: str


app = FastAPI()

#systemctl restart nginx
@app.post("/deploy/")
async def deploy(item: Item):
	if item.name == "voejvb3niu23r2" and item.password == "34g234v0n3iv0":
		cmds = ["cd mion.web", "npm run build", "rm -rf /var/www/mion",
				"cp -r build /var/www/mion"]
		for cmd in cmds:
			os.system(cmd)
    	return {"message": "Success"}
    return {"message": "Wrong credits"}
