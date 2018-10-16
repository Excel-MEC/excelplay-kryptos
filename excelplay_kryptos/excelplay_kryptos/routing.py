from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from api.consumers import updateLeaderboard

application = ProtocolTypeRouter({
		"websocket":URLRouter([
				path("ws/leaderboard/", updateLeaderboard)
			])
	})