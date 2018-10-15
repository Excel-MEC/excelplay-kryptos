import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .views import leaderboard

class updateLeaderboard(AsyncJsonWebsocketConsumer):
	async def connect(self):
		await self.accept()
		while 5:
			await asyncio.sleep(1)
			await self.send_json(leaderboard())