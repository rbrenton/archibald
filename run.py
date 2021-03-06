from fantasyapi import *
from utils import *
from archie import Archibald

prod = raw_input("Production League? (y/n) ")

if prod == "y":
	# Values for production
	print "Using Production League"
	league_no = 597247
	team_no = 10
else:
	# Values for testing
	print "Using Test League"
	team_no = raw_input("Which team? [1-4]: ")
	league_no = 697783

# Generate keys for the desired leage / team
team_key = "%s.l.%s.t.%s" % (GAME_KEY, league_no, team_no) 
league_id = "%s.l.%s" % (GAME_KEY, league_no)

try:
	api = FantasyApi(league_id) 
	api.handler.refresh_token()
except:
	print "Failed to refresh token - register user"
 	FantasyApi.create_handler().reg_user()
	api = FantasyApi(league_id)

try:
	archie = Archibald(api, league_id, team_key)

	while True:
		try:
			archie.start()
		except AuthException, e:
			print "Error: %s" % e
			print "Retry in 30 minutes"
			archie.sleep(0, 0, 30)
except AuthException, e:
	print "Hit API error: %s" % e
	print "Status code: %s" % e.status
