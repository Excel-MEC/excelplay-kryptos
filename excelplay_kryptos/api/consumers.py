import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .views import leaderboard

class updateLeaderboard(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		while 1:
			await asyncio.sleep(5)
			await self.send_json(leaderboard())