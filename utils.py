class Ad:
	def __init__(self, id, content: str, date: str, cost: str, contact: str):
		self.id = id
		self.content = content
		self.date = date
		self.cost = cost
		self.contact = contact


def init_cheque_handler():
	from fastapi import FastAPI, Response
	from pydantic import BaseModel
	from config import Config
	import motor.motor_asyncio
	import uvicorn

	app = FastAPI()

	class Cheque(BaseModel):
		content: str
		date: str
		cost: str
		contact: str
		active: bool

	@app.post('/sales/api/rest/v1/cheque')
	async def post(cheque: Cheque):
		client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_URI)
		collection = client[Config.MONGO_DATABASE][Config.MONGO_COLLECTION]

		await collection.insert_one(dict(cheque))

		return Response(content='OK', status_code=200)
	
	uvicorn.run(app, host='0.0.0.0', port=Config.CHEQUE_HANDLER_PORT)


if __name__ == "__main__":
	init_cheque_handler()
